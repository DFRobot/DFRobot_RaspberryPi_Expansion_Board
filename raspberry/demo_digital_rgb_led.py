# -*- coding:utf-8 -*-

'''
  # demo_digital_rgb_led.py
  #
  # Connect board with raspberryPi.
  # Run this demo.
  #
  # Connect LED pin r to pwm channel 2, pin g to pwm channel 1, pin b to pwm channel 3
  # LED will change to red, then green, then blue, then loop
  # Test LED: https://www.dfrobot.com/product-1829.html
  # Warning: LED must connect to pwm channel, otherwise may destory Pi IO
  #
  # Copyright   [DFRobot](http://www.dfrobot.com), 2016
  # Copyright   GNU Lesser General Public License
  #
  # version  V1.0
  # date  2019-3-28
'''

import time

from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board
from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Epansion_Board_Digital_RGB_LED as RGB_LED

board = Board(1, 0x10)    # Select i2c bus 1, set address to 0x10
led = RGB_LED(board)

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

  ''' Set color components channel and led begin '''
  led.begin(1, 0, 2) #pwm1/pwm0/pwm2

  while True:
    print("set color to red")
    led.color24(0xff0000)     # red
    time.sleep(1)
    print("set color to green")
    led.color565(0x07e0)      # green
    time.sleep(1)
    print("set color to blue")
    led.color888(0, 0, 255)   # blue
    time.sleep(1)
