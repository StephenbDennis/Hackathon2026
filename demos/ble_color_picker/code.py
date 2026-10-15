from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_bluefruit_connect.button_packet import ButtonPacket
from adafruit_bluefruit_connect.color_packet import ColorPacket
from adafruit_bluefruit_connect.packet import Packet
from adafruit_circuitplayground import cp

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

# Which 3 pixels to light for each arrow (hold the board with USB at the top)
ARROW_PIXELS = {
    ButtonPacket.UP: [9, 0, 1],
    ButtonPacket.DOWN: [4, 5, 6],
    ButtonPacket.LEFT: [1, 2, 3],
    ButtonPacket.RIGHT: [6, 7, 8],
}

cp.pixels.brightness = 0.2
color = (255, 255, 255)  # The last color picked in the app
print("Bluetooth name:", ble.name)  # Find this name in the Bluefruit Connect app

while True:
    # Blue = waiting for a phone to connect
    cp.pixels.fill((0, 0, 40))
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Green = connected. Use Controller > Color Picker or Control Pad in the app
    cp.pixels.fill((0, 40, 0))
    while ble.connected:
        packet = Packet.from_stream(uart)

        if isinstance(packet, ColorPacket):
            color = packet.color
            cp.pixels.fill(color)

        elif isinstance(packet, ButtonPacket) and packet.pressed:
            if packet.button in ARROW_PIXELS:
                # Arrow: light up the 3 pixels on that side
                cp.pixels.fill((0, 0, 0))
                for i in ARROW_PIXELS[packet.button]:
                    cp.pixels[i] = color
            else:
                # Number buttons 1, 2, 3 and 4
                print("Button", packet.button, "pressed")
