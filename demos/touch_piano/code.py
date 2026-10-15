from adafruit_circuitplayground import cp

# One note and one color for each pad: A1, A2, A3, A4, A5, A6, TX
NOTES = [262, 294, 330, 349, 392, 440, 494]
COLORS = [
    (255, 0, 0),  # Red
    (255, 80, 0),  # Orange
    (255, 200, 0),  # Yellow
    (0, 255, 0),  # Green
    (0, 200, 255),  # Light blue
    (0, 0, 255),  # Blue
    (160, 0, 255),  # Violet
]

cp.pixels.brightness = 0.2
cp.play_tone(523, 0.1)  # Beep so we know the program started

playing = None  # The pad being played right now

while True:
    pads = [cp.touch_A1, cp.touch_A2, cp.touch_A3, cp.touch_A4, cp.touch_A5, cp.touch_A6, cp.touch_TX]

    touched = None
    if True in pads:
        touched = pads.index(True)

    # Only change the sound when a different pad is touched
    if touched != playing:
        cp.stop_tone()
        if touched is None:
            cp.pixels.fill((0, 0, 0))
        else:
            cp.start_tone(NOTES[touched])
            cp.pixels.fill(COLORS[touched])
        playing = touched
