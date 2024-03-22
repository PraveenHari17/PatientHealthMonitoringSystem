import RPi.GPIO as GPIO
import time

class TestGPIO:
    def __init__(self, test_pin):
        self.test_pin = test_pin

    def run_test(self):
        try:
            # Set up GPIO mode and pin
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.test_pin, GPIO.OUT)

            # Test GPIO pin by setting it to high
            GPIO.output(self.test_pin, GPIO.HIGH)
            time.sleep(1)  # Wait for 1 second
            if GPIO.input(self.test_pin) != GPIO.HIGH:
                return False

            # Test GPIO pin by setting it to low
            GPIO.output(self.test_pin, GPIO.LOW)
            time.sleep(1)  # Wait for 1 second
            if GPIO.input(self.test_pin) != GPIO.LOW:
                return False

        except Exception as e:
            print("Error:", e)
            return False

        finally:
            # Clean up GPIO
            GPIO.cleanup()
        
        return True

# Define the GPIO pin to test
test_pin = 17
# Create an instance of the test case and run the test
test = TestGPIO(test_pin)
result = test.run_test()
print("Test result:", result)

test_pin = 26
# Create an instance of the test case and run the test
test = TestGPIO(test_pin)
result = test.run_test()
print("Test result:", result)

test_pin = 12
# Create an instance of the test case and run the test
test = TestGPIO(test_pin)
result = test.run_test()
print("Test result:", result)
