# DFRobot IO expansion HAT for Pi 

* [中文](./README_CN.md)

This RaspberryPi expansion board can communicate with RaspberryPi via I2C. <br>
It has 10 GPIOs, 1 SPI, 4 I2Cs and 1 uart. <br>
And it contains 4 ADC (12 bits) ports, ADC values can be read from on board stm32. <br>
Compatible with gravity interfaces developed by DFRobot. <br>

![产品效果图](resources/images/DFR0566.png)


## 产品链接（[https://www.dfrobot.com/product-1930.html](https://www.dfrobot.com/product-1930.html)）
    SKU: DFR0566

## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary

This is a Raspberry Pi peripherals expansion hat, its feature:

1. Read 12 bits ADC value. 
2. Set PWM frequency. 
3. Set PWM duty. 
4. Drive digital RGB LED. 
5. Drive 180 degree servo. 

## Installation

1. To use this library, first download the library file<br>
```python1
sudo git clone https://github.com/DFRobot/DFRobot_RaspberryPi_Expansion_Board
```
2. Open and run the routine. To execute a routine demo_x.py, enter python demo_x.py in the command line. For example, to execute the demo_adc.py routine, you need to enter :<br>

```python
python demo_adc.py 
or
python2 demo_adc.py
```

## Methods

```python

  '''!
    @brief    Board begin
    @return   Board status
  '''
  def begin(self):
    
  '''!
    @brief    Set board controler address, reboot module to make it effective
    @param address: int    Address to set, range in 1 to 127
  '''
  def set_addr(self, addr):
    
  '''!
    @brief    Set pwm enable, pwm channel need external power
  '''
  def set_pwm_enable(self):
    
  '''!
    @brief    Set pwm disable
  '''
  def set_pwm_disable(self):
    
  '''!
    @brief    Set pwm frequency
    @param freq: int    Frequency to set, in range 1 - 1000
  '''
  def set_pwm_frequency(self, freq):
    
  '''!
    @brief    Set selected channel duty
    @param chan: list     One or more channels to set, items in range 1 to 4, or chan = self.ALL
    @param duty: float    Duty to set, in range 0.0 to 100.0
  '''
  def set_pwm_duty(self, chan, duty):
    
  '''!
    @brief    Set adc enable
  '''
  def set_adc_enable(self):
    
  '''!
    @brief    Set adc disable
  '''
  def set_adc_disable(self):
    
  '''!
    @brief    Get adc value
    @param chan: int    Channel to get, in range 1 to 4, or self.ALL
    @return :list       List of value
  '''
  def get_adc_value(self, chan):
    
  '''!
    @brief    If you forget address you had set, use this to detecte them, must have class instance
    @return   Board list conformed
  '''
  def detecte(self):
    

class DFRobot_Epansion_Board_Digital_RGB_LED():
  '''!
    @param board: DFRobot_Expansion_Board   Board instance to operate digital rgb led, test LED: https://www.dfrobot.com/product-1829.html
                                            Warning: LED must connect to pwm channel, otherwise may destory Pi IO
  '''
  def __init__(self, board):
    
  '''!
    @brief    Set digital rgb led color channel, these parameters not repeat
    @param chan_r: int    Set color red channel id, in range 1 to 4
    @param chan_g: int    Set color green channel id, in range 1 to 4
    @param chan_b: int    Set color blue channel id, in range 1 to 4
  '''
  def begin(self, chan_r, chan_g, chan_b):
    
  '''!
    @brief    Set LED to true-color
    @param r: int   Color components red
    @param g: int   Color components green
    @param b: int   Color components blue
  '''
  def color888(self, r, g, b):
    
  '''!
    @brief    Set LED to 24-bits color
    @param color: int   24-bits color
  '''
  def color24(self, color):
    
  '''!
    @brief    Set LED to 16-bits color
    @param color: int   16-bits color
  '''
  def color565(self, color):
    

class DFRobot_Expansion_Board_Servo():
  '''!
    @param board: DFRobot_Expansion_Board   Board instance to operate servo, test servo: https://www.dfrobot.com/product-255.html
                                            Warning: servo must connect to pwm channel, otherwise may destory Pi IO
  '''
  def __init__(self, board):
    
  '''!
    @brief    Board servo begin
  '''
  def begin(self):
    
  '''!
    @brief    Servos move
    @param id: list     One or more servos to set, items in range 1 to 4, or chan = self.ALL
    @param angle: int   Angle to move, in range 0 to 180
  '''
  def move(self, id, angle):
    

class DFRobot_Expansion_Board_IIC(DFRobot_Expansion_Board):
  '''!
    @param bus_id: int   Which bus to operate
    @oaram addr: int     Board controler address
  '''
  def __init__(self, bus_id, addr):
    

```

## Compatibility

| 主板         | 通过 | 未通过 | 未测试 | 备注 |
| ------------ | :--: | :----: | :----: | :--: |
| RaspberryPi2 |      |        |   √    |      |
| RaspberryPi3 |      |        |   √    |      |
| RaspberryPi4 |  √   |        |        |      |

* Python 版本

| Python  | 通过 | 未通过 | 未测试 | 备注 |
| ------- | :--: | :----: | :----: | ---- |
| Python2 |  √   |        |        |      |
| Python3 |     |        |   √     |      |

## History

- 2019/03/28 - Version 1.0.0 released.

## Credits

Written by Frank(jiehan.guo@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))

