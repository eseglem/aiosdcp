import asyncio

from .commands import VERSION, CATEGORY, COMMUNITY, COMMANDS


def create_message(action: str, command: str, data: str = "") -> bytes:
    data_length = ("00" + str(len(data) // 2))[-2:]
    hex_string = f"{VERSION}{CATEGORY}{COMMUNITY}{action}{command}{data_length}{data}"
    return bytes.fromhex(hex_string)


def parse_message(message: bytes) -> dict:
    response = {}
    response["community"] = message[2:6].decode()

    message = message.hex().upper()
    response["version"] = message[0:2]
    response["category"] = message[2:4]
    response["success"] = message[12:14] == "01"
    response["command"] = next(
        key for key, value in COMMANDS.items() if value == message[14:18]
    )
    response["data_length"] = int(message[18:20], 16)
    if response["data_length"] > 0:
        response["data"] = message[-response["data_length"] * 2 :]
    else:
        response["data"] = ""
    return response


async def send_message(
    ip: str, message: bytes, loop: asyncio.AbstractEventLoop
) -> bytes:
    reader, writer = await asyncio.open_connection(ip, 53484, loop=loop)
    print(f"Send: {message}")
    writer.write(message)
    data = await reader.read(20)
    print(f"Received: {data.decode()}")
    writer.close()
    return data
