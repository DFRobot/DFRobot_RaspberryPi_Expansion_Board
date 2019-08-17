# DFRobot IO expansion HAT for Pi 

This RaspberryPi expansion board can communicate with RaspberryPi via I2C. <br>
It has 10 GPIOs, 1 SPI, 4 I2Cs and 1 uart. <br>
And it contains 4 ADC (12 bits) ports, ADC values can be read from on board stm32. <br>
Compatible with gravity interfaces developed by DFRobot. <br>

## DFRobot DC Motor Driver HAT Library for RaspberryPi

To provide a Raspberry Pi library for DFRobot IO expansion HAT modules.

## Table of Contents

* [Summary](#summary)
* [Feature](#feature)
* [Installation](#installation)
* [Methods](#methods)
* [Credits](#credits)

## Summary

Io expansion hat.

## Feature

1. Read 12 bits ADC value. <br>
2. Set PWM frequency. <br>
3. Set PWM duty. <br>
4. Drive digital RGB LED. <br>
5. Drive 180 degree servo. <br>

## Installation

This sensor should work with DFRobot_Raspberry_Extension_Board on RaspberryPi. <br>
Run the program:

```
$> python2 demo_basic.py
```

## Methods

```py

class DFRobot_Expansion_Board:

  ''' Enum board Analog channels '''
  A0 = 0x00
  A1 = 0x01
  A2 = 0x02
  A3 = 0x03

  ''' Board status '''
  STA_OK = 0x00
  STA_ERR = 0x01
  STA_ERR_DEVICE_NOT_DETECTED = 0x02
  STA_ERR_SOFT_VERSION = 0x03
  STA_ERR_PARAMETER = 0x04

  ''' last operate status, users can use this variable to determine the result of a function call. '''
  last_operate_status = STA_OK

  ''' Global variables '''
  ALL = 0xffffffff

  def begin(self):
    '''
      @brief    Board begin
      @return   Board status
    '''

  def set_addr(self, addr):
    '''
      @brief    Set board controler address, reboot module to make it effective
      @param address: int    Address to set, range in 1 to 127
    '''

  def set_pwm_enable(self):
    '''
      @brief    Set pwm enable, pwm channel need external power
    '''

  def set_pwm_disable(self):
    '''
      @brief    Set pwm disable
    '''

  def set_pwm_frequency(self, freq):
    '''
      @brief    Set pwm frequency
      @param freq: int    Frequency to set, in range 1 - 1000
    '''

  def set_pwm_duty(self, chan, duty):
    '''
      @brief    Set selected channel duty
      @param chan: list     One or more channels to set, items in range 1 to 4, or chan = self.ALL
      @param duty: float    Duty to set, in range 0.0 to 100.0
    '''

  def set_adc_enable(self):
    '''
      @brief    Set adc enable
    '''

  def set_adc_disable(self):
    '''
      @brief    Set adc disable
    '''

  def get_adc_value(self, chan):
    '''
      @brief    Get adc value
      @param chan: int    Channel to get, in range 1 to 4, or self.ALL
      @return :list       List of value
    '''

  def detecte(self):
    '''
      @brief    If you forget address you had set, use this to detecte them, must have class instance
      @return   Board list conformed
    '''

class DFRobot_Epansion_Board_Digital_RGB_LED():

  def __init__(self, board):
    '''
      @param board: DFRobot_Expansion_Board   Board instance to operate digital rgb led, test LED: https://www.dfrobot.com/product-1829.html
                                              Warning: LED must connect to pwm channel, otherwise may destory Pi IO
    '''

  def begin(self, chan_r, chan_g, chan_b):
    '''
      @brief    Set digital rgb led color channel, these parameters not repeat
      @param chan_r: int    Set color red channel id, in range 1 to 4
      @param chan_g: int    Set color green channel id, in range 1 to 4
      @param chan_b: int    Set color blue channel id, in range 1 to 4
    '''

  def color888(self, r, g, b):
    '''
      @brief    Set LED to true-color
      @param r: int   Color components red
      @param g: int   Color components green
      @param b: int   Color components blue
    '''

  def color24(self, color):
    '''
      @brief    Set LED to 24-bits color
      @param color: int   24-bits color
    '''

  def color565(self, color):
    '''
      @brief    Set LED to 16-bits color
      @param color: int   16-bits color
    '''

class DFRobot_Expansion_Board_Servo():

  def __init__(self, board):
    '''
      @param board: DFRobot_Expansion_Board   Board instance to operate servo, test servo: https://www.dfrobot.com/product-255.html
                                              Warning: servo must connect to pwm channel, otherwise may destory Pi IO
    '''

  def begin(self):
    '''
      @brief    Board servo begin
    '''

  def move(self, id, angle):
    '''
      @brief    Servos move
      @param id: list     One or more servos to set, items in range 1 to 4, or chan = self.ALL
      @param angle: int   Angle to move, in range 0 to 180
    '''

class DFRobot_Expansion_Board_IIC(DFRobot_Expansion_Board):

  def __init__(self, bus_id, addr):
    '''
      @param bus_id: int   Which bus to operate
      @oaram addr: int     Board controler address
    '''

```

## Credits

·author [Frank jiehan.guo@dfrobot.com]
