#Based on
#https://github.com/vrachieru/xiaomi-flower-care-api/ for Xiaomi Flower Care protocol
#and 
#https://bleak.readthedocs.io/en/latest/index.html and https://github.com/hbldh/bleak
# for bleak example

import platform
import logging
import asyncio
import time

from bleak import BleakClient
from bleak import _logger as logger


_BYTE_ORDER = 'little'

_UUID_NAME     ="00002a00-0000-1000-8000-00805f9b34fb"
_UUID_FIRM_BATT="00002a19-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_UUID="ebe0ccc1-7a0a-4b0c-8a1a-6ff2997da3a6"

def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    temperature = int.from_bytes(data[:2], _BYTE_ORDER) / 100
    print("Temperature:",temperature,"°C")
    moisture = data[2]
    print("Moisture:",moisture,"%")
    
async def run(address, loop, debug=False):
    if debug:
        import sys

        loop.set_debug(True)
        l = logging.getLogger("asyncio")
        l.setLevel(logging.DEBUG)
        h = logging.StreamHandler(sys.stdout)
        h.setLevel(logging.DEBUG)
        l.addHandler(h)

    client = BleakClient(address, loop=loop)
    x= await client.connect(timeout=10.0)

    value = await client.read_gatt_char(_UUID_NAME)
    print("Name:",''.join(map(chr, value)))
    
    value = await client.read_gatt_char(_UUID_FIRM_BATT)
    print("Battery level:",value[0],"%")

    # souscription notifications
    await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

    await asyncio.sleep(20.0, loop=loop)
    await client.stop_notify(CHARACTERISTIC_UUID)


    #end
    x= await client.disconnect()

    
if __name__ == "__main__":
    import os

    os.environ["PYTHONASYNCIODEBUG"] = str(1)
    address = (
        "XX:XX:XX:XX:XX:XX" #sensor address
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address, loop, False))  # switch debug

