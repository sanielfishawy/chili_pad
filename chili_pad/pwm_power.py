#pylint: disable=no-member
import RPi.GPIO as GPIO

class PwmPower:

    DEFAULT_PWM_PIN = 12  #GPIO.BOARD pin
    DEFAULT_FREQUENCY = 20  #Hz do not set above 20 Hz or may overheat the FET

    def __init__(
            self,
            pwm_pin=DEFAULT_PWM_PIN,
    ):
        self.pwm_pin = pwm_pin
        self.power = 0
        self.pwm = self.setup_pins()

    def setup_pins(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pwm_pin, GPIO.OUT, initial=GPIO.HIGH)
        pwm = GPIO.PWM(self.pwm_pin, PwmPower.DEFAULT_FREQUENCY)
        pwm.start(self.get_duty_cycle())
        return pwm

    def get_duty_cycle(self):
        return 100 - self.power

    def normalize_power(self, power):
        if power > 100:
            return 100
        elif power < 0:
            return 0
        else:
            return int(power)

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = self.normalize_power(power)
        self.pwm.ChangeDutyCycle(self.get_duty_cycle())

