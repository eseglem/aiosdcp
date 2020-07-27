from enum import Enum

import values

VERSION = "02"
CATEGORY = "0A"
COMMUNITY = "534F4E59"  # Default to 'SONY'


class ACTIONS(Enum):
    GET = "01"
    SET = "00"


COMMANDS = {
    # Table 2-1 ITEM List For Picture Quality Setting
    "SET_POWER": ("0130", values.OFF_ON),
    "CALIBRATION_PRESET": ("0002", values.CALIBRATION_PRESET),
    "CONTRAST": ("0010", values.Zero_OneHundred),
    "BRIGHTNESS": ("0011", values.Zero_OneHundred),
    "COLOR": ("0012", values.Zero_OneHundred),
    "HUE": ("0013", values.Zero_OneHundred),
    "SHARPNESS": ("0014", values.Zero_OneHundred),
    "COLOR_TEMP": ("0017", values.COLOR_TEMP),
    "LAMP_CONTROL": ("001A", values.LAMP_CONTROL),
    "CONTRAST_ENHANCER": ("001C", values.CONTRAST_ENHANCER),
    "ADVANCED_IRIS": ("001D", values.ADVANCED_IRIS),
    "FILM_MODE": ("001F", values.FILM_MODE),
    "GAMMA_CORRECTION": ("0022", values.GAMMA_CORRECTION),
    "NR": ("0025", values.NR),
    "COLOR_SPACE": ("003B", values.COLOR_SPACE),
    "USER_GAIN_RED": ("0050", values.NegThirty_Thirty),
    "USER_GAIN_GREEN": ("0051", values.NegThirty_Thirty),
    "USER_GAIN_BLUE": ("0052", values.NegThirty_Thirty),
    "USER_BIAS_RED": ("0053", values.NegThirty_Thirty),
    "USER_BIAS_GREEN": ("0054", values.NegThirty_Thirty),
    "USER_BIAS_BLUE": ("0055", values.NegThirty_Thirty),
    "IRIS_BRIGHTNESS": ("0057", values.Zero_OneHundred),
    "MOTION_FLOW": ("0059", values.MOTION_FLOW),
    "XV_COLOR": ("0054", values.OFF_ON),
    "REALITY_CREATION": ("0067", values.OFF_ON),
    "RESOLUTION": ("0068", values.Zero_OneHundred),
    "NOISE_FILTER": ("0069", values.Zero_OneHundred),
    "CLEAR_WHITE": ("006B", values.CLEAR_WHITE),
    "MPEG_NR": ("006C", values.NR),
    "SMOOTH_GRADATION": ("006D", values.SMOOTH_GRADATION),
    "REALITY_CREATION_DATABASE": ("0075", values.REALITY_CREATION_DATABASE),
    # COLOR SPACE
    "COLOR_SPACE_CUSTOM_RED_CYAN_RED": ("0076", values.NegFifty_Fifty),
    "COLOR_SPACE_CUSTOM_RED_GREEN_MAGENTA": ("0077", values.NegFifty_Fifty),
    "COLOR_SPACE_CUSTOM_GREEN_CYAN_RED": ("0078", values.NegFifty_Fifty),
    "COLOR_SPACE_CUSTOM_GREEN_GREEN_MAGENTA": ("0079", values.NegFifty_Fifty),
    "COLOR_SPACE_CUSTOM_BLUE_CYAN_RED": ("007A", values.NegFifty_Fifty),
    "COLOR_SPACE_CUSTOM_BLUE_GREEN_MAGENTA": ("007B", values.NegFifty_Fifty),
    "HDR": ("007C", values.HDR),
    # COLOR CORRECTION
    "COLOR_CORRECTION": ("0086", values.OFF_ON),
    "COLOR_CORRECTION_RED_HUE": ("0087", values.NegFifty_Fifty),
    "COLOR_CORRECTION_RED_COLOR": ("0088", values.NegFifty_Fifty),
    "COLOR_CORRECTION_RED_BRIGHTNESS": ("0089", values.NegThirty_Thirty),
    "COLOR_CORRECTION_YELLOW_HUE": ("008A", values.NegFifty_Fifty),
    "COLOR_CORRECTION_YELLOW_COLOR": ("008B", values.NegFifty_Fifty),
    "COLOR_CORRECTION_YELLOW_BRIGHTNESS": ("008C", values.NegThirty_Thirty),
    "COLOR_CORRECTION_GREEN_HUE": ("008D", values.NegFifty_Fifty),
    "COLOR_CORRECTION_GREEN_COLOR": ("008E", values.NegFifty_Fifty),
    "COLOR_CORRECTION_GREEN_BRIGHTNESS": ("008F", values.NegThirty_Thirty),
    "COLOR_CORRECTION_CYAN_HUE": ("0090", values.NegFifty_Fifty),
    "COLOR_CORRECTION_CYAN_COLOR": ("0091", values.NegFifty_Fifty),
    "COLOR_CORRECTION_CYAN_BRIGHTNESS": ("0092", values.NegThirty_Thirty),
    "COLOR_CORRECTION_BLUE_HUE": ("0093", values.NegFifty_Fifty),
    "COLOR_CORRECTION_BLUE_COLOR": ("0094", values.NegFifty_Fifty),
    "COLOR_CORRECTION_BLUE_BRIGHTNESS": ("0095", values.NegThirty_Thirty),
    "COLOR_CORRECTION_MAGENTA_HUE": ("0096", values.NegFifty_Fifty),
    "COLOR_CORRECTION_MAGENTA_COLOR": ("0097", values.NegFifty_Fifty),
    "COLOR_CORRECTION_MAGENTA_BRIGHTNESS": ("0098", values.NegThirty_Thirty),
    "INPUT_LAG_REDUCTION": ("0099", values.OFF_ON),
    # Table 2-2 ITEM List For Screen Setting
    "PICTURE_POSITION": ("0066", values.PICTURE_POSITION),
    "ASPECT_RATIO": ("0020", values.ASPECT_RATIO),
    # Table 2-3 ITEM List For Initial Setting
    "INPUT": ("0001", values.INPUT),
    "PICTURE_MUTING": ("0030", values.OFF_ON),
    "HDMI1_HDR": ("006E", values.HDMI_HDR),
    "HDMI2_HDR": ("006F", values.HDMI_HDR),
    "SETTINGS_LOCK": ("0073", values.SETTINGS_LOCK),
    # Table 2-4 ITEM List For 3D Setting
    "2D_3D_DISPLAY_SEL": ("0060", values._2D_3D_DISPLAY_SEL),
    "3D_FORMAT": ("0061", values._3D_FORMAT),
    "3D_DEPTH_ADJUST": ("0062", values.NegTwo_Two),
    "SIMULATED_3D_EFFECT": ("0063", values.SIMULATED_3D_EFFECT),
    "3D_BRIGHTNESS": ("0072", values._3D_BRIGHTNESS),
    # Table 2-5 ITEM List For Status, Get only
    "GET_STATUS_ERROR": ("0101", values.STATUS_ERROR),
    "GET_STATUS_POWER": ("0102", values.STATUS_POWER),
    "GET_STATUS_LAMP_TIMER": ("0113", None),  # Range 0000 - FFFF
    "GET_STATUS_ERROR_2": ("0125", values.STATUS_ERROR_2),
    # Table 2-6 List for Technical Applications
    "STATUS": ("00A4", values.OFF_ON),
    "LANGUAGE": ("00A5", values.LANGUAGES),
    "MENU_POSITION": ("00A6", values.MENU_POSITION),
    "HIGH_ALTITUDE_MODE": ("00A7", values.OFF_ON),
    "POWER_SAVING": ("00AA", values.POWER_SAVING),
    "TEST_PATTERN": ("00AB", values.OFF_ON),
    "IMAGE_FLIP": ("00AD", values.IMAGE_FLIP),
    "LENS_CONTROL": ("00AE", values.OFF_ON),
    "IR_RECIEVER": ("00AF", values.IR_RECIEVER),
    "BLANKING_LEFT": ("00B0", values.Zero_Fifty),
    "BLANKING_RIGHT": ("00B1", values.Zero_Fifty),
    "BLANKING_UP": ("00B2", values.Zero_Fifty),
    "BLANKING_DOWN": ("00B3", values.Zero_Fifty),
    "TRIGGER_SLECT_1": ("00C2", values.TRIGGER_SLECT),
    "TRIGGER_SELECT_2": ("00C3", values.TRIGGER_SLECT),
    "ANAMORPHIC_LENS": ("00C4", values.ANAMORPHIC_LENS),
    "BLANKING": ("00C8", values.OFF_ON),
    "PANEL_ALIGNMENT": ("00EC", values.OFF_ON),
    "SET_SETTINGS_RESET": ("016A", values.SET_SETTINGS_RESET),
    "SET_MAINTENANCE_COMPLETE": ("01D2", values.SET_MAINTENANCE_COMPLETE),
    # "SET_MAINSOFTWARE_VERSION": ("011H",),
    # "FPGA_DEVICE_VERSION": ("013A",),
}

COMMANDS_REVERSE = {value[0]: key for key, value in COMMANDS.items()}
