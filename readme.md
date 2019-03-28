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
* [Compatibility](#compatibility)
* [Credits](#credits)

## Summary

Io expansion hat.

## Feature

1. Read 12 bits ADC value.<br>
2. Set PWM frequency.<br>
3. Set PWM duty.<br>

## Installation

This sensor should work with DFRobot_Raspberry_Extension_Board on RaspberryPi. <br>
Run the program:

```
$> python2 demo_basic.py
```

## Methods

```py

class DFRobot_Extension_Board:

  ''' Board status '''
  STA_OK = 0x00
  STA_ERR = 0x01
  STA_ERR_DEVICE_NOT_DETECTED = 0x02
  STA_ERR_SOFT_VERSION = 0x03
  STA_ERR_PARAMETER = 0x04

  ''' The last operate status, users can use this variable to determine the result of a function call. '''
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
      @brief    Set board controller address, reboot module to make it effective.
      @param address: int    Address to set, range from 1 to 127.
    '''

  def set_pwm_enable(self):
    '''
      @brief    Enable pwm 
    '''

  def set_pwm_disable(self):
    '''
      @brief    Disable pwm 
    '''

  def set_pwm_frequency(self, freq):
    '''
      @brief    Set pwm frequency
      @param freq: int    Frequency to set, in range 1 - 1000
    '''

  def set_pwm_duty(self, chan, duty):
    '''
      @brief    Set selected channel duty, Attention: PWM voltage depends on independent power supply
      @param chan: list     One or more channels to set, items range from 1 to 4, or chan = self.ALL
      @param duty: float    Duty to set, in range 0.0 to 99.0
    '''
  
  def set_adc_enable(self):
    '''
      @brief   Enable adc 
    '''

  def set_adc_disable(self):
    '''
      @brief    Disable adc 
    '''

  def get_adc_value(self, chan):
    '''
      @brief    Get adc value
      @param chan: int    One or more channels to set, items range from 1 to 4, or chan = self.ALL
      @return :list       List of value
    '''

  def detecte(self):
    '''
      @brief    If you forget address that set before, please donot forget class instance when detecting.
      @return   Board list conformed
    '''

class DFRobot_Extension_Board_IIC(DFRobot_Extension_Board):

  def __init__(self, bus_id, addr):
    '''
      @param bus_id: int   Which bus to operate
      @oaram addr: int     Board controler address
    '''

```

## Credits

·author [Frank jiehan.guo@dfrobot.com]
