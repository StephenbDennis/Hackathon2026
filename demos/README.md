# Circuit Playground Bluefruit demos

## How to run a demo

1. Plug in the board. It shows up as a USB drive called `CIRCUITPY`.
2. Copy everything in [`demos/lib/`](lib/) into the `lib` folder on
   `CIRCUITPY`. It holds every library the demos need, taken from
   the 10.x bundle in `circuitpython/standard_libraries/lib/`.
3. Copy the demo's `code.py` to the root of `CIRCUITPY` (replace the one
   that's there). The board will flash green for a while then restart.

## What's in `lib/`

Every demo needs these:

- `adafruit_circuitplayground/` (folder)
- `adafruit_bus_device/` (folder)
- `adafruit_lis3dh.mpy`
- `adafruit_thermistor.mpy`
- `neopixel.mpy`

`ble_color_picker` also needs:

- `adafruit_ble/` (folder)
- `adafruit_bluefruit_connect/` (folder)

`servo_tilt` also needs:

- `adafruit_motor/` (folder)

For the Bluetooth demo, install **Adafruit Bluefruit LE Connect**
app on your phone (Whould be available for iOS or android).
