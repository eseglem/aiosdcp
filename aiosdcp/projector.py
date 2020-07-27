import asyncio
import struct
from enum import Enum, EnumMeta
from typing import Union

import commands
import values


async def int_to_data(i: int) -> str:
    return struct.pack(">i", i).hex()[-4:].upper()


async def data_to_int(s: str) -> int:
    s = "0000" + s
    return struct.unpack(">i", bytes.fromhex(s))


async def create_message(
    action: str,
    command: str,
    data: str = "",
    version=commands.VERSION,
    category=commands.CATEGORY,
    community=commands.COMMUNITY,
) -> bytes:
    # Probably never need to change version or category, but available if needed.
    # Zero pad the data length to two characters
    data_length = f"{(len(data) // 2):02}"
    command_hex, checker = commands.COMMANDS[command]
    hex_string = (
        f"{version}{category}{community}{action.value}{command_hex}{data_length}{data}"
    )
    return bytes.fromhex(hex_string)


async def parse_message(message: bytes) -> dict:
    response = dict()
    response["community"] = message[2:6].decode()

    message = message.hex().upper()
    response["version"] = message[0:2]
    response["category"] = message[2:4]
    response["success"] = message[12:14] == "01"
    response["command"] = commands.COMMANDS_REVERSE[message[14:18]]
    response["data_length"] = int(message[18:20], 16)
    if response["data_length"] > 0:
        data = message[-response["data_length"] * 2 :]
        if not response["success"]:
            try:
                response["data"] = values.ERROR_CODE(data)
            except ValueError:
                response["data"] = data
        else:
            response["data"] = await parse_data(response["command"], data)
    else:
        response["data"] = None
    return response


async def parse_data(command: str, data: bytes) -> Union[Enum, int]:
    # print(command, data)
    if command == "GET_STATUS_LAMP_TIMER":
        return int(data, 16)
    checker = commands.COMMANDS[command][1]
    if isinstance(checker, EnumMeta):
        return checker(data)
    if callable(checker):
        # return await (data_to_int(data))
        return data


async def send_message(
    ip: str, message: bytes, loop: asyncio.AbstractEventLoop
) -> bytes:
    # TODO: Modern way of doing this
    reader, writer = await asyncio.open_connection(ip, 53484, loop=loop)
    # print(f"Send: {message}")
    writer.write(message)
    data = await reader.read(20)
    # print(f"Received: {data}")
    writer.close()
    return data
