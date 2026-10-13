"""Raw GT911 points only — no display dependency."""

import time

from m5paper_epd import Touch

touch = Touch(orientation="landscape")
print("GT911 @ 0x%02X  %dx%d" % (touch.address, touch.width, touch.height))

while True:
    pts = touch.touches()
    if pts:
        for x, y, size, tid in pts:
            print("finger", tid, "x=", x, "y=", y, "size=", size)
    time.sleep(0.05)
