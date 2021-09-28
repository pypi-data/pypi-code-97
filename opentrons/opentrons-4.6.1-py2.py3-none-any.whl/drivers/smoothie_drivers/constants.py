from enum import Enum

from typing_extensions import Final


class GCODE(str, Enum):
    HOME = "G28.2"
    MOVE = "G0"
    DWELL = "G4"
    CURRENT_POSITION = "M114.2"
    LIMIT_SWITCH_STATUS = "M119"
    PROBE = "G38.2"
    ABSOLUTE_COORDS = "G90"
    RELATIVE_COORDS = "G91"
    RESET_FROM_ERROR = "M999"
    PUSH_SPEED = "M120"
    POP_SPEED = "M121"
    SET_SPEED = "G0"
    STEPS_PER_MM = "M92"
    READ_INSTRUMENT_ID = "M369"
    WRITE_INSTRUMENT_ID = "M370"
    READ_INSTRUMENT_MODEL = "M371"
    WRITE_INSTRUMENT_MODEL = "M372"
    SET_MAX_SPEED = "M203.1"
    SET_CURRENT = "M907"
    DISENGAGE_MOTOR = "M18"
    HOMING_STATUS = "G28.6"
    ACCELERATION = "M204"
    WAIT = "M400"
    PIPETTE_RETRACT = "M365.3"
    PIPETTE_DEBOUNCE = "M365.2"
    PIPETTE_MAX_TRAVEL = "M365.1"
    PIPETTE_HOME = "M365.0"
    MICROSTEPPING_B_ENABLE = "M52"
    MICROSTEPPING_B_DISABLE = "M53"
    MICROSTEPPING_C_ENABLE = "M54"
    MICROSTEPPING_C_DISABLE = "M55"
    VERSION = "version"


HOMED_POSITION: Final = {
    "X": 418.0,
    "Y": 353.0,
    "Z": 218.0,
    "A": 218.0,
    "B": 19.0,
    "C": 19.0,
}

Y_BOUND_OVERRIDE: Final = 370

SMOOTHIE_COMMAND_TERMINATOR = "\r\n\r\n"

SMOOTHIE_ACK = "ok\r\nok\r\n"

PLUNGER_BACKLASH_MM = 0.3

LOW_CURRENT_Z_SPEED = 30

CURRENT_CHANGE_DELAY = 0.005

PIPETTE_READ_DELAY = 0.1

Y_SWITCH_BACK_OFF_MM = 28

Y_SWITCH_REVERSE_BACK_OFF_MM = 10

Y_BACKOFF_LOW_CURRENT = 0.8

Y_BACKOFF_SLOW_SPEED = 50

Y_RETRACT_SPEED = 8

Y_RETRACT_DISTANCE = 3

UNSTICK_DISTANCE = 1

UNSTICK_SPEED = 1

DEFAULT_AXES_SPEED = 400

XY_HOMING_SPEED = 80

HOME_SEQUENCE = ["ZABC", "X", "Y"]

AXES = "".join(HOME_SEQUENCE)

DISABLE_AXES = ""
"""Ignore these axis when sending move or home command"""

MOVEMENT_ERROR_MARGIN = 1 / 160  # Largest movement in mm for any step

SEC_PER_MIN = 60

DEFAULT_ACK_TIMEOUT = 5

DEFAULT_EXECUTE_TIMEOUT = 12000

DEFAULT_SMOOTHIE_TIMEOUT = 1

DEFAULT_MOVEMENT_TIMEOUT = 30

SMOOTHIE_BOOT_TIMEOUT = 3

DEFAULT_STABILIZE_DELAY = 0.1

DEFAULT_COMMAND_RETRIES = 3

MICROSTEPPING_GCODES = {
    "B": {
        "ENABLE": GCODE.MICROSTEPPING_B_ENABLE,
        "DISABLE": GCODE.MICROSTEPPING_B_DISABLE,
    },
    "C": {
        "ENABLE": GCODE.MICROSTEPPING_C_ENABLE,
        "DISABLE": GCODE.MICROSTEPPING_C_DISABLE,
    },
}

GCODE_ROUNDING_PRECISION = 3
"""Number of digits after the decimal point for coordinates being sent to Smoothie"""
