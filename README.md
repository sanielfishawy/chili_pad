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
cp.heat()
print(cp.get_heat_cool())
cp.cool()
print(cp.get_heat_cool())
cp.off()
print(cp.get_heat_cool())
```

[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
