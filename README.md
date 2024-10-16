# Sending Data from ESP to Email Account

This project demonstrates how to send data from an ESP8266/ESP32 microcontroller to an email account. It's particularly useful for IoT projects, where devices need to communicate information such as sensor data to users via email. The code leverages the SMTP protocol to send emails with sensor data, which can be used in various applications like smart agriculture, home automation, weather monitoring, and more.

## Features
- **ESP8266/ESP32 Integration**: Easily send sensor data (e.g., temperature, humidity, soil moisture) from ESP microcontrollers.
- **SMTP Email Service**: Utilizes the Simple Mail Transfer Protocol to send emails from your IoT device.
- **IoT Applications**: Perfect for smart agriculture, home automation, remote weather stations, and other IoT-related use cases.
- **Flexible Configuration**: Allows you to modify email settings such as recipients, subject, and email body.
- **Simple Setup**: Easily customizable for different sensors and applications.

## Applications
- **Smart Agriculture**: Monitor soil moisture, temperature, and other environmental factors, and receive email alerts for timely irrigation and crop management.
- **Home Automation**: Track household sensor data like indoor temperature, humidity, and air quality and send updates via email.
- **Weather Monitoring**: Collect outdoor environmental data (temperature, humidity, pressure) and send periodic reports to your email.
- **Security Alerts**: Use motion detectors or door/window sensors to trigger email alerts for home security systems.

## Requirements
- **Hardware:**
  - ESP8266 or ESP32 microcontroller
  - Sensors (e.g., DHT11/DHT22 for temperature and humidity, Soil Moisture Sensor, etc.)
  
- **Software:**
  - Arduino IDE (for code development and flashing the ESP)
  - ESP8266/ESP32 Core installed in Arduino IDE
  - WiFi connection
  - Gmail account or another SMTP-enabled email service

## Libraries
You will need the following Arduino libraries:
- `WiFi.h` (for ESP32) or `ESP8266WiFi.h` (for ESP8266)
- `SMTPClient.h` or any other email client library (such as ESP-Mail-Client)

## Getting Started
1. **Hardware Setup**:
   - Connect your ESP microcontroller to sensors like DHT11/DHT22 for temperature and humidity or a soil moisture sensor for monitoring plant conditions.

2. **Software Setup**:
   - Install the required libraries in your Arduino IDE.
   - Configure your WiFi credentials and email settings in the Arduino sketch.

3. **Deploy the Code**:
   - Upload the Arduino sketch to your ESP8266/ESP32.

4. **Run the Project**:
   - Once the ESP is running, it will collect sensor data and send it to your email address periodically or based on certain triggers (e.g., if the soil moisture is too low).

## How It Works
- The ESP microcontroller reads data from sensors connected to it.
- When certain conditions are met (e.g., high/low temperature or soil moisture), the ESP sends the sensor data to a specified email account.
- The system can be configured to send periodic updates or event-triggered emails, making it highly flexible for various IoT applications.

## Future Improvements
- **Expand to Multiple Recipients**: Allow emails to be sent to multiple users.
- **Data Visualization**: Send emails with attachments like CSV files or images for better data representation.
- **SMS Integration**: Add SMS alerts alongside email notifications.

## Contribution
Feel free to submit issues or pull requests if you have ideas for improvements or find bugs in the current setup.

---

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
