import time

from adafruit_circuitplayground import cp

NUM_PIXELS = 10

# Higher value = less sensitive to sound. Lower value = more sensitive to sound.
sensitivity = 400
MIN_SENSITIVITY = 50
MAX_SENSITIVITY = 2000

cp.pixels.brightness = 0.2
cp.pixels.auto_write = False  # we are calling show()

def meter_color(i):
    if i < 5:
        return (0, 255, 0) # Green
    if i < 8:
        return (255, 150, 0) # Yellow
    return (255, 0, 0) # Red

# Get initial volume reading
cp.pixels.fill((40, 40, 40))
cp.pixels.show()
time.sleep(1)

readings = []
for _ in range(20):
    readings.append(cp.sound_level)
    time.sleep(0.02)
background = sum(readings) / len(readings)
print("Initial level:", background)

while True:
    level = cp.sound_level

    # Turn the sound level into a number of pixels to light (0 to 10).
    loudness = (level - background) / sensitivity
    lit = int(loudness * NUM_PIXELS)
    lit = max(0, min(lit, NUM_PIXELS))

    # Draw the meter.
    for i in range(NUM_PIXELS):
        if i < lit:
            cp.pixels[i] = meter_color(i)
        else:
            cp.pixels[i] = (0, 0, 0)

    cp.pixels.show()

    # Change the sensitivity
    if cp.button_a:
        sensitivity = max(MIN_SENSITIVITY, sensitivity - 50)
        print("Increase sensitivity:", sensitivity)
        time.sleep(0.2)
    if cp.button_b:
        sensitivity = min(MAX_SENSITIVITY, sensitivity + 50)
        print("Decrease sensitivity:", sensitivity)
        time.sleep(0.2)
