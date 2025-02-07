### https://raw.githubusercontent.com/uArm-Developer/pyuarm/dev/pyuarm/protocol.py
# parameters

## SERVO NUMBER INDEX
SERVO_BOTTOM = 0
SERVO_LEFT = 1
SERVO_RIGHT = 2
SERVO_HAND = 3

## CALIBRATION FLAG
CONFIRM_FLAG = 0x80
CALIBRATION_FLAG = 10
CALIBRATION_LINEAR_FLAG = 11
CALIBRATION_SERVO_FLAG = 12
CALIBRATION_STRETCH_FLAG = 13

## OFFSET EEPROM ADDRESS
LINEAR_INTERCEPT_START_ADDRESS = 70
LINEAR_SLOPE_START_ADDRESS = 50
OFFSET_START_ADDRESS = 30
OFFSET_STRETCH_START_ADDRESS = 20

SERIAL_NUMBER_ADDRESS = 100

## EEPROM DATA TYPE INDEX
EEPROM_DATA_TYPE_BYTE = 1
EEPROM_DATA_TYPE_INTEGER = 2
EEPROM_DATA_TYPE_FLOAT = 4

## PROTOCOL MESSAGE
# READY & Response
READY                   = "@1"
OK                      = "OK"
# Set Command
SET_POSITION            = "G0 X{} Y{} Z{} F{}"
SET_POSITION_RELATIVE   = "G204 X{} Y{} Z{} F{}"
SET_SERVO_ANGLE         = "G202 N{} V{}"
STOP_MOVING             = "G203"
SET_PUMP                = "M231 V{}"
GET_PUMP                = "P231"
SET_GRIPPER             = "M232 V{}"
SET_BUZZER              = "M210 F{} T{}"
SET_POLAR               = "G201 S{} R{} H{} F{}"
ATTACH_SERVO            = "M201 N{}"
DETACH_SERVO            = "M202 N{}"
# SET_REPORT_BUTTON       = "M213 V{}" #1 Open #0 Close
# Get Command
GET_SIMULATION          = "M222 X{} Y{} Z{} P0"
GET_FIRMWARE_VERSION    = "P203"
GET_HARDWARE_VERSION    = "P202"
GET_COOR                = "P220"
GET_SERVO_STATUS        = "M203"
GET_SERVO_ANGLE         = "P200"
GET_IS_MOVE             = "M200"
GET_TIP_SENSOR          = "P233"
GET_POLAR               = "P221"
GET_GRIPPER             = "P232"
GET_EEPROM              = "M211 N0 A{} T{}"
SET_EEPROM              = "M212 N0 A{} T{} V{}"
GET_ANALOG              = "P241 N{}"
GET_DIGITAL             = "P240 N{}"

# Report Command
SET_REPORT_POSITION     = "M120 V{}"
REPORT_POSITION_PREFIX  = "@3"
# REPORT_BUTTON_PRESSED   = "@4"
# BUTTON_MENU             = "B0"
# BUTTON_PLAY             = "B1"


