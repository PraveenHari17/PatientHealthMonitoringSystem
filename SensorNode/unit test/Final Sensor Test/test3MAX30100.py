import max30100

# Initialize the sensor
sensor = max30100.MAX30100()
sensor.enable_spo2()
try:
    while True:
        sensor.read_sensor()
        print('Raw IR:', sensor.ir)
        print('Raw red:', sensor.red)
except KeyboardInterrupt:
    print('Interrupted by user')
