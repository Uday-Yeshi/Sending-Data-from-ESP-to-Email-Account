import umail
import time
import machine
from machine import Pin

# Email configuration
sender_email = 'pojectstudy@gmail.com'
sender_name = 'ESP32'
sender_app_password = 'xkfc ysid tsqz tlso'
recipient_email = 'uday.yeshi23@spit.ac.in'
email_subject = 'Soil Moisture Level'

# Initialize TTP223B touch sensor (adjust the pin as necessary)
touch_pin = Pin(4, Pin.IN)  # Replace with the actual pin used for the touch sensor

# Initialize soil moisture sensor (analog pin)
moisture_sensor_pin = machine.Pin(34)  # Replace with the actual pin used for the moisture sensor
moisture_adc = machine.ADC(moisture_sensor_pin)

def send_email(moisture_value):
    try:
        smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)  # Gmail's SSL port
        smtp.login(sender_email, sender_app_password)
        smtp.to(recipient_email)
        smtp.write("From: " + sender_name + "<" + sender_email + ">\n")
        smtp.write("Subject: " + email_subject + "\n")
        smtp.write(f"Hello ESP32\nSoil Moisture Level: {moisture_value}\n")
        smtp.send()
        smtp.quit()
        print("Email sent!")
    except Exception as e:
        print("Failed to send email:", e)

# Main loop
try:
    while True:
        try:
            # Check if the touch sensor is triggered
            if touch_pin.value() == 1:
                print("Touch detected! Pausing for 30 seconds.")
                time.sleep(30)  # Pause for 30 seconds
            else:
                # Read soil moisture sensor value
                moisture_value = moisture_adc.read()  # Use ADC to read the analog value
                print("Soil Moisture Level:", moisture_value)
                print("Please on the motor")

                # Send email with moisture value
                send_email(moisture_value)
                time.sleep(5)  # Wait for 5 seconds before the next reading

        except ValueError as e:
            print("Sensor error:", e)
            time.sleep(1)  # Pause briefly before retrying

except KeyboardInterrupt:
    print("Program stopped.")

