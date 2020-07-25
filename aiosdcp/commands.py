VERSION = "02"
CATEGORY = "0A"
COMMUNITY = "534F4E59"  # Default to 'SONY'

ACTIONS = {
    "GET": "01",
    "SET": "00",
}

COMMANDS = {
    # Table 2-1 ITEM List For Picture Quality Setting
    "SET_POWER": "0130",  # Set only
    "CALIBRATION_PRESET": "0002",
    "CONTRAST": "0010",  # Range 0000 - 0064 (0 to 100)
    "BRIGHTNESS": "0011",  # Range 0000 - 0064 (0 to 100)
    "COLOR": "0012",  # Range 0000 - 0064 (0 to 100)
    "HUE": "0013",  # Range 0000 - 0064 (0 to 100)
    "SHARPNESS": "0014",  # Range 0000 - 0064 (0 to 100)
    "COLOR_TEMP": "0017",
    "LAMP_CONTROL": "001A",
    "CONTRAST_ENHANCER": "001C",
    "ADVANCED_IRIS": "001D",
    "FILM_MODE": "001F",
    "GAMMA_CORRECTION": "0022",
    "NR": "0025",
    "COLOR_SPACE": "003B",
    "USER_GAIN_RED": "0050",  # Range FFE2 - 001E (-30 to 30)
    "USER_GAIN_GREEN": "0051",  # Range FFE2 - 001E (-30 to 30)
    "USER_GAIN_BLUE": "0052",  # Range FFE2 - 001E (-30 to 30)
    "USER_BIAS_RED": "0053",  # Range FFE2 - 001E (-30 to 30)
    "USER_BIAS_GREEN": "0054",  # Range FFE2 - 001E (-30 to 30)
    "USER_BIAS_BLUE": "0055",  # Range FFE2 - 001E (-30 to 30)
    "IRIS_BRIGHTNESS": "0057",  # Range 0000 - 0064 (0 to 100)
    "MOTION_FLOW": "0059",
    "XV_COLOR": "0054",
    "REALITY_CREATION": "0067",
    "RESOLUTION": "0068",  # Range 0000 - 0064 (0 to 100)
    "NOISE_FILTER": "0069",  # Range 0000 - 0064 (0 to 100)
    "CLEAR_WHITE": "006B",
    "MPEG_NR": "006C",
    "SMOOTH_GRADATION": "006D",
    "REALITY_CREATION_DATABASE": "0075",
    # COLOR SPACE
    "COLOR_SPACE_CUSTOM_RED_CYAN_RED": "0076",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_SPACE_CUSTOM_RED_GREEN_MAGENTA": "0077",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_SPACE_CUSTOM_GREEN_CYAN_RED": "0078",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_SPACE_CUSTOM_GREEN_GREEN_MAGENTA": "0079",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_SPACE_CUSTOM_BLUE_CYAN_RED": "007A",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_SPACE_CUSTOM_BLUE_GREEN_MAGENTA": "007B",  # Range FFCE - 0032 (-50 to 50)
    "HDR": "007C",
    # COLOR CORRECTION
    "COLOR_CORRECTION": "0086",
    "COLOR_CORRECTION_RED_HUE": "0087",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_RED_COLOR": "0088",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_RED_BRIGHTNESS": "0089",  # Range FFE2 - 001E (-30 to 30)
    "COLOR_CORRECTION_YELLOW_HUE": "008A",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_YELLOW_COLOR": "008B",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_YELLOW_BRIGHTNESS": "008C",  # Range FFE2 - 001E (-30 to 30)
    "COLOR_CORRECTION_GREEN_HUE": "008D",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_GREEN_COLOR": "008E",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_GREEN_BRIGHTNESS": "008F",  # Range FFE2 - 001E (-30 to 30)
    "COLOR_CORRECTION_CYAN_HUE": "0090",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_CYAN_COLOR": "0091",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_CYAN_BRIGHTNESS": "0092",  # Range FFE2 - 001E (-30 to 30)
    "COLOR_CORRECTION_BLUE_HUE": "0093",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_BLUE_COLOR": "0094",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_BLUE_BRIGHTNESS": "0095",  # Range FFE2 - 001E (-30 to 30)
    "COLOR_CORRECTION_MAGENTA_HUE": "0096",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_MAGENTA_COLOR": "0097",  # Range FFCE - 0032 (-50 to 50)
    "COLOR_CORRECTION_MAGENTA_BRIGHTNESS": "0098",  # Range FFE2 - 001E (-30 to 30)
    "INPUT_LAG_REDUCTION": "0099",
    # Table 2-2 ITEM List For Screen Setting
    "PICTURE_POSITION": "0066",
    "ASPECT_RATIO": "0020",
    # Table 2-3 ITEM List For Initial Setting
    "INPUT": "0001",
    "PICTURE_MUTING": "0030",
    "HDMI1_HDR": "006E",
    "HDMI2_HDR": "006F",
    "SETTINGS_LOCK": "0073",
    # Table 2-4 ITEM List For 3D Setting
    "2D_3D_DISPLAY_SEL": "0060",
    "3D_FORMAT": "0061",
    "3D_DEPTH_ADJUST": "0062",  # Range FFFE - 0002 (-2 to 2)
    "SIMULATED_3D_EFFECT": "0063",
    "3D_BRIGHTNESS": "0072",
    # Table 2-5 ITEM List For Status, Get only
    "GET_STATUS_ERROR": "0101",
    "GET_STATUS_POWER": "0102",
    "GET_STATUS_LAMP_TIMER": "0113",  # Range 0000 - FFFF
    "GET_STATUS_ERROR_2": "0125",
}

OFF_ON = {
    "OFF": "0000",
    "ON": "0001",
}

SET_POWER = OFF_ON

CALIBRATION_PRESET = {
    "CINEMA_FILM_1": "0000",
    "CINEMA_FILM_2": "0001",
    "REF": "0002",
    "TV": "0003",
    "PHOTO": "0004",
    "GAME": "0005",
    "BRT_CINE": "0006",
    "BRT_TV": "0007",
    "USER": "0008",
}

COLOR_TEMP = {
    "D93": "0000",
    "D75": "0001",
    "D65": "0002",
    "CUSTOM1": "0003",
    "CUSTOM2": "0004",
    "CUSTOM3": "0005",
    "CUSTOM4": "0006",
    "CUSTOM5": "0008",
    "D55": "0009",
}

LAMP_CONTROL = {
    "LOW": "0000",
    "HIGH": "0001",
}

CONTRAST_ENHANCER = {
    "OFF": "0000",
    "LOW": "0001",
    "HIGH": "0002",
    "MIDDLE": "0003",
}

ADVANCED_IRIS = {
    "OFF": "0000",
    "FULL": "0002",
    "LIMITED": "0003",
}

FILM_MODE = {
    "OFF": "0000",
    "AUTO": "0002",
}

GAMMA_CORRECTION = {
    "OFF": "0000",
    "1.8": "0001",
    "2.0": "0002",
    "2.1": "0003",
    "2.2": "0004",
    "2.4": "0005",
    "2.6": "0006",
    "GAMMA7": "0007",
    "GAMMA8": "0008",
    "GAMMA9": "0009",
    "GAMMA10": "000A",
}

NR = {
    "OFF": "0000",
    "LOW": "0001",
    "MIDDLE": "0002",
    "HIGH": "0003",
    "AUTO": "0004",
}

COLOR_SPACE = {
    "BT.709": "0000",
    "COLOR_SPACE1": "0003",
    "COLOR_SPACE2": "0004",
    "COLOR_SPACE3": "0005",
    "CUSTOM": "0006",
    "BT.2020": "0008",
}

MOTION_FLOW = {
    "OFF": "0000",
    "SMOOTH_HIGH": "0001",
    "SMOOTH_LOW": "0002",
    "IMPULSE": "0003",
    "COMBINATION": "0004",
    "TRUE_CINEMA": "0005",
}

XV_COLOR = OFF_ON

REALITY_CREATION = OFF_ON

CLEAR_WHITE = {
    "OFF": "0000",
    "LOW": "0001",
    "HIGH": "0002",
}

MPEG_NR = {
    "OFF": "0000",
    "LOW": "0001",
    "MIDDLE": "0002",
    "HIGH": "0003",
    "AUTO": "0004",
}

SMOOTH_GRADATION = {
    "OFF": "0000",
    "LOW": "0001",
    "MIDDLE": "0002",
    "HIGH": "0003",
}

REALITY_CREATION_DATABASE = {"MASTERED_IN_4K": "0000", "NORMAL": "0001"}

HDR = {
    "OFF": "0000",
    "ON": "0001",
    "AUTO": "0002",
}

COLOR_CORRECTION = OFF_ON

INPUT_LAG_REDUCTION = OFF_ON

# Table 2-2 ITEM List For Screen Setting
PICTURE_POSITION = {
    "1.85": "0000",
    "2.35": "0001",
    "CUSTOM1": "0002",
    "CUSTOM2": "0003",
    "CUSTOM3": "0004",
}

ASPECT_RATIO = {
    "NORMAL": "0001",
    "V_STRETCH": "000B",
    "1.85_ZOOM": "000C",
    "2.35_ZOOM": "000D",
    "STRETCH": "000E",
    "SQUEEZE": "000F",
}

# Table 2-3 ITEM List For Initial Setting
INPUT = {
    "HDMI1": "0002",
    "HDMI2": "0003",
}

PICTURE_MUTING = OFF_ON

HDMI1_HDR = {
    "AUTO": "0000",
    "LIMIT": "0001",
    "FULL": "0002",
}

HDMI2_HDR = {
    "AUTO": "0000",
    "LIMIT": "0001",
    "FULL": "0002",
}

SETTINGS_LOCK = {
    "OFF": "0000",
    "LEVEL_A": "0001",
    "LEVEL_B": "0002",
}

# Table 2-4 ITEM List For 3D Setting
# TODO: Better names that don't need _ ?
_2D_3D_DISPLAY_SEL = {
    "AUTO": "0000",
    "3D": "0001",
    "2D": "0002",
}

_3D_FORMAT = {
    "SIMULATED_3D": "0000",
    "SIDE_BY_SIDE": "0001",
    "OVER_UNDER": "0002",
}

SIMULATED_3D_EFFECT = {
    "HIGH": "0000",
    "MIDDLE": "0001",
    "LOW": "0002",
}

_3D_BRIGHTNESS = {
    "HIGH": "0000",
    "STANDARD": "0001",
}

# Table 2-5 ITEM List For Status
STATUS_ERROR = {
    "NO_ERROR",
    "0000",
    "LAMP_ERROR",
    "0001",
    "FAN_ERROR",
    "0002",
    "COVER_ERROR",
    "0004",
    "TEMP_ERROR",
    "0008",
    "D5V_ERROR",
    "0010",
    "POWER_ERROR",
    "0020",
    "TEMP_WARNING",
    "0040",
}

POWER_STATUS = {
    "STANDBY": "0000",
    "START_UP": "0001",
    "START_UP_LAMP": "0002",
    "POWER_ON": "0003",
    "COOLING": "0004",
    "COOLING2": "0005",
}

STATUS_ERROR_2 = {
    "NO_ERROR",
    "0000",
    "HIGHLAND_WARNING",
    "0020",
}
