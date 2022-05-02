import asyncio
import time

from bleak import BleakScanner
from bleak import BleakClient
_UUID_FIRM_BATT = "00002a19-0000-1000-8000-00805f9b34fb"
_BYTE_ORDER = 'little'
CHARACTERISTIC_UUID = "ebe0ccc1-7a0a-4b0c-8a1a-6ff2997da3a6"
def notification_handler(sender, data):
    print(222, time.time())
    """Simple notification handler which prints the data received."""
    temperature = int.from_bytes(data[:2], _BYTE_ORDER) / 100
    print("Temperature:", temperature, "°C")
    moisture = data[2]
    print("Moisture:", moisture, "%")

async def main():
    devices = await BleakScanner.discover(timeout=20)
    for d in devices:
        print(d)
        if d.address == 'A4:C1:38:0E:FF:80': # MAC address of your device ## China NO.1
            client = BleakClient(d.address)
            await client.connect(timeout=20)
            print(client.is_connected)
            # await client.write_gatt_char(0x0038, b'\x01\x00', True)
            # await client.write_gatt_char(0x0046, b'\xf4\x01\x00', True)
            # data = await client.read_gatt_char('00002a24-0000-1000-8000-00805f9b34fb')
            value = await client.read_gatt_char(_UUID_FIRM_BATT)
            print("Battery level:", value[0], "%")
            await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
            await asyncio.sleep(20.0)
            await client.stop_notify(CHARACTERISTIC_UUID)

            # end
            x = await client.disconnect()

asyncio.run(main())
