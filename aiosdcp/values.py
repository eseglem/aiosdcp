from enum import Enum
from typing import Callable


def new_clipper(smallest: int, largest: int) -> Callable:
    def clip(n: int) -> int:
        return max(smallest, min(n, largest))

    return clip


Zero_OneHundred = new_clipper(0, 100)
NegThirty_Thirty = new_clipper(-30, 30)
NegFifty_Fifty = new_clipper(-50, 50)
NegTwo_Two = new_clipper(-2, 2)


# TODO: Better names that don't need _ ?


class OFF_ON(Enum):
    OFF = "0000"
    ON = "0001"


class CALIBRATION_PRESET(Enum):
    CINEMA_FILM_1 = "0000"
    CINEMA_FILM_2 = "0001"
    REF = "0002"
    TV = "0003"
    PHOTO = "0004"
    GAME = "0005"
    BRT_CINE = "0006"
    BRT_TV = "0007"
    USER = "0008"


class COLOR_TEMP(Enum):
    D93 = "0000"
    D75 = "0001"
    D65 = "0002"
    CUSTOM1 = "0003"
    CUSTOM2 = "0004"
    CUSTOM3 = "0005"
    CUSTOM4 = "0006"
    CUSTOM5 = "0008"
    D55 = "0009"


class LAMP_CONTROL(Enum):
    LOW = "0000"
    HIGH = "0001"


class CONTRAST_ENHANCER(Enum):
    OFF = "0000"
    LOW = "0001"
    HIGH = "0002"
    MIDDLE = "0003"


class ADVANCED_IRIS(Enum):
    OFF = "0000"
    FULL = "0002"
    LIMITED = "0003"


class FILM_MODE(Enum):
    OFF = "0000"
    AUTO = "0002"


class GAMMA_CORRECTION(Enum):
    OFF = "0000"
    _1_8 = "0001"
    _2_0 = "0002"
    _2_1 = "0003"
    _2_2 = "0004"
    _2_4 = "0005"
    _2_6 = "0006"
    GAMMA7 = "0007"
    GAMMA8 = "0008"
    GAMMA9 = "0009"
    GAMMA10 = "000A"


class NR(Enum):
    OFF = "0000"
    LOW = "0001"
    MIDDLE = "0002"
    HIGH = "0003"
    AUTO = "0004"


class COLOR_SPACE(Enum):
    BT709 = "0000"
    COLOR_SPACE1 = "0003"
    COLOR_SPACE2 = "0004"
    COLOR_SPACE3 = "0005"
    CUSTOM = "0006"
    BT2020 = "0008"


class MOTION_FLOW(Enum):
    OFF = "0000"
    SMOOTH_HIGH = "0001"
    SMOOTH_LOW = "0002"
    IMPULSE = "0003"
    COMBINATION = "0004"
    TRUE_CINEMA = "0005"


class CLEAR_WHITE(Enum):
    OFF = "0000"
    LOW = "0001"
    HIGH = "0002"


class SMOOTH_GRADATION(Enum):
    OFF = "0000"
    LOW = "0001"
    MIDDLE = "0002"
    HIGH = "0003"


class REALITY_CREATION_DATABASE(Enum):
    MASTERED_IN_4K = "0000"
    NORMAL = "0001"


class HDR(Enum):
    OFF = "0000"
    ON = "0001"
    AUTO = "0002"


# Table 2-2 ITEM List For Screen Setting
class PICTURE_POSITION(Enum):
    _1_85 = "0000"
    _2_35 = "0001"
    CUSTOM1 = "0002"
    CUSTOM2 = "0003"
    CUSTOM3 = "0004"


class ASPECT_RATIO(Enum):
    NORMAL = "0001"
    V_STRETCH = "000B"
    _1_85_ZOOM = "000C"
    _2_35_ZOOM = "000D"
    STRETCH = "000E"
    SQUEEZE = "000F"


# Table 2-3 ITEM List For Initial Setting
class INPUT(Enum):
    HDMI1 = "0002"
    HDMI2 = "0003"


class HDMI_HDR(Enum):
    AUTO = "0000"
    LIMIT = "0001"
    FULL = "0002"


class SETTINGS_LOCK(Enum):
    OFF = "0000"
    LEVEL_A = "0001"
    LEVEL_B = "0002"


# Table 2-4 ITEM List For 3D Setting
class _2D_3D_DISPLAY_SEL(Enum):
    AUTO = "0000"
    _3D = "0001"
    _2D = "0002"


class _3D_FORMAT(Enum):
    SIMULATED_3D = "0000"
    SIDE_BY_SIDE = "0001"
    OVER_UNDER = "0002"


class SIMULATED_3D_EFFECT(Enum):
    HIGH = "0000"
    MIDDLE = "0001"
    LOW = "0002"


class _3D_BRIGHTNESS(Enum):
    HIGH = "0000"
    STANDARD = "0001"


# Table 2-5 ITEM List For Status
class STATUS_ERROR(Enum):
    NO_ERROR = "0000"
    LAMP_ERROR = "0001"
    FAN_ERROR = "0002"
    COVER_ERROR = "0004"
    TEMP_ERROR = "0008"
    D5V_ERROR = "0010"
    POWER_ERROR = "0020"
    TEMP_WARNING = "0040"


class STATUS_POWER(Enum):
    STANDBY = "0000"
    START_UP = "0001"
    START_UP_LAMP = "0002"
    POWER_ON = "0003"
    COOLING = "0004"
    COOLING2 = "0005"


class STATUS_ERROR_2(Enum):
    NO_ERROR = "0000"
    HIGHLAND_WARNING = "0020"
