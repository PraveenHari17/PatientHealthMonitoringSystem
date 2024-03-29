import time
import board
import adafruit_sht31d

# Create the I2C bus
i2c = board.I2C()

# Create a sensor instance
sensor = adafruit_sht31d.SHT31D(i2c, address=0x45)

while True:
    print('Temperature: {:.2f} degrees C'.format(sensor.temperature))
    print('Humidity: {:.2f}%'.format(sensor.relative_humidity))
   
    # Pause for a second before next reading
    time.sleep(1)
