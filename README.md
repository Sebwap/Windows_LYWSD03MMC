# Windows_LYWSD03MMC
A simple python example to read values from Xiaomi LYWSD03MMC sensor device from a Windows 10 PC.

It use bleak as library to communicate with Bluetooth LE driver.

Many thanks to:

https://github.com/hbldh/bleak for wonderfull work on Bleak !

Feel free to make a better code of this, it was just made in a few hours just to see if it was possible under Windows 10.

# Sample result below:
```
Name: LYWSD03MMC
Battery level: 99 %
Temperature: 22.78 °C
Moisture: 51 %
Temperature: 22.77 °C
Moisture: 51 %
Temperature: 22.79 °C
Moisture: 50 %
```
# Issues

Unfortunately, sometimes, the result is only
`bleak.exc.BleakError: Device with address XX:XX:XX:XX:XX:XX was not found.`
I don't know why the device seem to be invisible sometimes.
