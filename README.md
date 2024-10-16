Sending Data from ESP to Email Account
This project demonstrates how to send data from an ESP8266/ESP32 microcontroller to an email account. It's particularly useful for IoT projects, where devices need to communicate information such as sensor data to users via email. The code leverages the SMTP protocol to send emails with sensor data, which can be used in various applications like smart agriculture, home automation, weather monitoring, and more.

Features
ESP8266/ESP32 Integration: Easily send sensor data (e.g., temperature, humidity, soil moisture) from ESP microcontrollers.
SMTP Email Service: Utilizes the Simple Mail Transfer Protocol to send emails from your IoT device.
IoT Applications: Perfect for smart agriculture, home automation, remote weather stations, and other IoT-related use cases.
Flexible Configuration: Allows you to modify email settings such as recipients, subject, and email body.
Simple Setup: Easily customizable for different sensors and applications.
Applications
Smart Agriculture: Monitor soil moisture, temperature, and other environmental factors, and receive email alerts for timely irrigation and crop management.
Home Automation: Track household sensor data like indoor temperature, humidity, and air quality and send updates via email.
Weather Monitoring: Collect outdoor environmental data (temperature, humidity, pressure) and send periodic reports to your email.
Security Alerts: Use motion detectors or door/window sensors to trigger email alerts for home security systems.
Requirements
Hardware:
ESP8266 or ESP32 microcontroller
Sensors (e.g., DHT11/DHT22 for temperature and humidity, Soil Moisture Sensor, etc.)
Software:
Arduino IDE (for code development and flashing the ESP)
ESP8266/ESP32 Core installed in Arduino IDE
WiFi connection
Gmail account or another SMTP-enabled email service
Libraries
You will need the following Arduino libraries:

WiFi.h (for ESP32) or ESP8266WiFi.h (for ESP8266)
SMTPClient.h or any other email client library (such as ESP-Mail-Client)
