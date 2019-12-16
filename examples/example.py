#pylint: disable=no-name-in-module, import-error, invalid-name

#Ivoke from top level director using: python3 -m examples.example

from chili_pad.driver import Driver as CP

cp = CP()
print(cp.get_pump()) # Gets the on/off state of the pump
# Turns the pump on. Be sure pad is attached and full of water before turning on.
cp.pump_on()
print(cp.get_pump())
cp.pump_off()
print(cp.get_pump())

# Get the heat/cool/off status of the heater
print(cp.get_heat_cool())
cp.heat()
print(cp.get_heat_cool())
cp.cool()
print(cp.get_heat_cool())
cp.off()
print(cp.get_heat_cool())