# JETSON library

- DC motor controller using L298N
- 6-DoF Robot arm controller via UART

## Installation

```bash
pip install git+https://github.com/nhthai173/JETSON
```

## DCMotor

```python
from JETSON import DCMotor
from time import sleep

# Motor 1
m1 = DCMotor(7, 11) # channel A connect to Pin 7 and 11
# Motor 2
m2 = DCMotor(12, 13) # channel B connect to Pin 12 and 13

while True:
    try:
        m1.forward()
        m2.forward()
        sleep(5)

        m1.stop()
        m2.stop()

        m1.backward()
        m2.backward()
    except:
        break

GPIO.cleanup()
```

## RARM

```python
from JETSON import RARM

# Channel on RTRobot 32 servo controller module
channels = ['9', '12', '17', '21', '24', '28']

# Using on Windows
arm = RARM(channels, port = 'COM13') 

# Using on linux
# Default port is '/dev/ttyACM0'
# arm = RARM(channels)

while True:
    arm.setPos([1765, 2214, 1520, 2133, 1482, 1765])
    sleep(2)
    arm.setPos([2050, 2050, 1153, 2133, 1480, 1357])
    sleep(2)
    arm.setPos([1520, 2255, 745, 2010, 1480, 1600])
    sleep(2)
    arm.setPos([1031, 1806, 1398, 2133, 1480, 1888])
    sleep(2)
```