# -*- coding:utf-8 -*-

'''
  # demo_servo.py
  #
  # Connect board with raspberryPi.
  # Run this demo.
  #
  # Connect servo to one of pwm channels
  # All or part servos will move to 0 degree, then move to 180 degree, then loop
  # Test Servo: https://www.dfrobot.com/product-255.html
  # Warning: Servos must connect to pwm channel, otherwise may destory Pi IO
  #
  # Copyright   [DFRobot](http://www.dfrobot.com), 2016
  # Copyright   GNU Lesser General Public License
  #
  # version  V1.0
  # date  2019-3-28
'''

import time

from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board
from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_Servo as Servo

board = Board(1, 0x10)    # Select i2c bus 1, set address to 0x10
servo = Servo(board)

''' print last operate status, users can use this variable to determine the result of a function call. '''
def print_board_status():
  if board.last_operate_status == board.STA_OK:
    print("board status: everything ok")
  elif board.last_operate_status == board.STA_ERR:
    print("board status: unexpected error")
  elif board.last_operate_status == board.STA_ERR_DEVICE_NOT_DETECTED:
    print("board status: device not detected")
  elif board.last_operate_status == board.STA_ERR_PARAMETER:
    print("board status: parameter error")
  elif board.last_operate_status == board.STA_ERR_SOFT_VERSION:
    print("board status: unsupport board framware version")

if __name__ == "__main__":

  while board.begin() != board.STA_OK:    # Board begin and check board status
    print_board_status()
    print("board begin faild")
    time.sleep(2)
  print("board begin success")

  servo.begin()   # servo control begin

  while True:
    print("servo move to 0")
    servo.move(board.ALL, 0)
    time.sleep(1)
    print("servo move to 180")
    servo.move(board.ALL, 180)
    time.sleep(1)

    print("part servos move to 0")
    servo.move(0, 0)  #pwm0
    #servo.move(1, 0)  #pwm1
    #servo.move(2, 0)  #pwm2
    #servo.move(3, 0)  #pwm3
    time.sleep(1)
    print("part servos move to 180")
    servo.move(0, 180)  #pwm0
    #servo.move(1, 180)  #pwm1
    #servo.move(2, 180)  #pwm2
    #servo.move(3, 180)  #pwm3
    time.sleep(1)
