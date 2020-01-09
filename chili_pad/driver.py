#pylint: disable=no-member
import RPi.GPIO as GPIO
from chili_pad.pwm_power import PwmPower

class Driver:

    DEFAULT_COLD_PIN = 16
    DEFAULT_HOT_PIN = 18
    DEFAULT_PUMP_PIN = 22

    def __init__(
            self,
            cold_pin=DEFAULT_COLD_PIN,
            hot_pin=DEFAULT_HOT_PIN,
            pump_pin=DEFAULT_PUMP_PIN,
    ):
        self.cool_pin = cold_pin
        self.heat_pin = hot_pin
        self.pump_pin = pump_pin
        self.output_pins = [self.cool_pin, self.heat_pin, self.pump_pin]
        self.setup_pins()
        self.pwm_power = PwmPower()


    def setup_pins(self):
        GPIO.setmode(GPIO.BOARD)
        for pin in self.output_pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def pump_on(self):
        GPIO.output(self.pump_pin, True)
        return self

    def pump_off(self):
        GPIO.output(self.pump_pin, False)
        return self

    def get_pump(self):
        return GPIO.input(self.pump_pin)

    def heat(self):
        GPIO.output(self.heat_pin, True)
        GPIO.output(self.cool_pin, False)
        return self

    def cool(self):
        GPIO.output(self.cool_pin, True)
        GPIO.output(self.heat_pin, False)

    def off(self):
        GPIO.output(self.heat_pin, False)
        GPIO.output(self.cool_pin, False)
        self.pwm_power.set_power(0)

    def get_heat_cool(self):
        h = GPIO.input(self.heat_pin)
        c = GPIO.input(self.cool_pin)
        result = 'off'

        if h and not c:
            result = 'heat'
        elif c and not h:
            result = 'cool'

        return result

    def set_power(self, power: int):
        self.pwm_power.set_power(power)

    def get_power(self):
        return self.pwm_power.get_power()

    def set_abs_power(self, power: int):
        '''
        Set power as an integer between -100 and 100.
        Turns on heat or cool and sets the power appropriately
        '''
        if power < 0:
            self.cool()
        elif power > 0:
            self.heat()
        else:
            self.off()

        self.set_power(abs(power))

if __name__ == '__main__':
    cp = Driver()

    pass

    print(cp.get_pump())
    cp.pump_on()
    print(cp.get_pump())
    cp.pump_off()
    print(cp.get_pump())

    print(cp.get_heat_cool())
    cp.heat()
    cp.set_power(50)
    print(cp.get_heat_cool())
    print(cp.get_power())

    cp.cool()
    cp.set_power(100)
    print(cp.get_heat_cool())
    print(cp.get_power())

    cp.off()
    print(cp.get_heat_cool())
    print(cp.get_power())

    pass
