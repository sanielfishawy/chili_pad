# chili_pad

## Description
This is a driver class for the chili_pad modified by Sani replacing the the control board and the powersupply.

## Installation
```
pip install -U git+https://github.com/sanielfishawy/chili_pad
```

## Usage
```python
from chili_pad.driver import Driver as CP

cp = CP()

# Gets the on/off state of the pump
print(cp.get_pump())

# Turns the pump on. Be sure pad is attached and full of water before turning on.
cp.pump_on()
print(cp.get_pump())
cp.pump_off()
print(cp.get_pump())

# Get the heat/cool/off status of the heater.
print(cp.get_heat_cool())

# Turns the heater on.
# Power can be set from 0 - 100
cp.heat()
cp.set_power(50) # set power 0 - 100
print(cp.get_heat_cool())
print(cp.get_power())

cp.cool()
cp.set_power(100)
print(cp.get_heat_cool())
print(cp.get_power())

cp.off()
print(cp.get_heat_cool())
print(cp.get_power())
```

[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
