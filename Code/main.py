import umail
import time
import machine

# Email configuration
sender_email = 'enter your senders email'
sender_name = 'enter your senders name'
sender_app_password = 'app passcode' # This can be obatined by usnig attached document as guide
recipient_email = 'enter recipient email'
email_subject = 'Soil Moisture Level' # enter your subject

# Initialize capacitive touch sensor (adjust the pin as necessary)
touch_pin = machine.Pin(32)  # Replace with the actual pin used for the touch sensor
touch_sensor = machine.TouchPad(touch_pin)

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
            touch_value = touch_sensor.read()
            if touch_value < 500:  # Adjust threshold as needed
                print("Touch detected! Pausing for 30 seconds.")
                time.sleep(30)  # Pause for 30 seconds
            else:
                # Read soil moisture sensor value
                moisture_value = moisture_adc.read()  # Use ADC to read the analog value
                print("Soil Moisture Level:", moisture_value)

                # Send email with moisture value
                send_email(moisture_value)
                time.sleep(5)  # Wait for 5 seconds before the next reading

        except ValueError as e:
            print("Touch pad error:", e)
            time.sleep(1)  # Pause briefly before retrying

except KeyboardInterrupt:
    print("Program stopped.")
