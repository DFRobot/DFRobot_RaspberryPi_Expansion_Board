# -*- coding:utf-8 -*-

'''
  # demo_pwm.py
  #
  # Connect board with raspberryPi.
  # Run this demo.
  #
  # All pwm channel will set frequency to 1000HZ, duty to 50%, attention: PWM voltage depends on independent power supply
  # If there is DC motors connect to pwm channle, they will move slow to fast, then loop
  #
  # Copyright   [DFRobot](http://www.dfrobot.com), 2016
  # Copyright   GNU Lesser General Public License
  #
  # version  V1.0
  # date  2019-3-28
'''

import time

from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board

board = Board(1, 0x10)    # Select i2c bus 1, set address to 0x10

def board_detect():
  l = board.detecte()
  print("Board list conform:")
  print(l)

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

  board_detect()    # If you forget address you had set, use this to detected them, must have class instance

  # Set board controler address, use it carefully, reboot module to make it effective
  '''
  board.set_addr(0x10)
  if board.last_operate_status != board.STA_OK:
    print("set board address faild")
  else:
    print("set board address success")
  '''

  while board.begin() != board.STA_OK:    # Board begin and check board status
    print_board_status()
    print("board begin faild")
    time.sleep(2)
  print("board begin success")

  board.set_pwm_enable()                # Pwm channel need external power
  # board.set_pwm_disable()
  board.set_pwm_frequency(1000)         # Set frequency to 1000HZ, Attention: PWM voltage depends on independent power supply

  while True:
    print("set all pwm channels duty to 30%")
    board.set_pwm_duty(board.ALL, 30)   # Set all pwm channels duty
    time.sleep(1)

    print("set part pwm channels duty to 60%")
    board.set_pwm_duty(0, 60)   # Set pwm0 channels duty
    #board.set_pwm_duty(1, 70)  # Set pwm1 channels duty
    #board.set_pwm_duty(2, 80)  # Set pwm2 channels duty
    #board.set_pwm_duty(3, 90)  # Set pwm3 channels duty
    time.sleep(1)
