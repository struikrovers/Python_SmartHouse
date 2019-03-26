import board
import busio
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")
pca = PCA9685(i2c)

pca.frequency = 0

pca9685Addr = 0x81
subaddr1 = 0xE2
subaddr2 = 0xE4
subaddr3 = 0xE8


def ledbrightness(led, dutycycle: int = 4096):
    pca.channels[led].duty_cycle = dutycycle
