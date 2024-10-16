import network, time, machine
ssid = 'enter your wifi name'
password = 'enter your wifi password'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass
print('Connection successful')
print(station.ifconfig())
