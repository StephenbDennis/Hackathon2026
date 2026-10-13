"""Touch paint demo for M5Paper GT911 + m5paper_epd."""

import time

from m5paper_epd import EPD, MODE_DU, MODE_GC16, Touch

ORIENT = "landscape"  # or "portrait"

epd = EPD(orientation=ORIENT, invert=False)
touch = Touch.from_epd(epd)
W, H = epd.width, epd.height

epd.init_clear()
epd.fill(15)
epd.text("TOUCH DEMO", 20, 20, 0, scale=3)
epd.text("Tap / drag to draw", 20, 60, 0, scale=2)
epd.text("addr=0x%02X  %dx%d" % (touch.address, W, H), 20, 100, 0, scale=1)
epd.fill_rect(W - 160, 16, 140, 48, 0)
epd.text("CLEAR", W - 140, 28, 15, scale=2)
epd.show(mode=MODE_GC16, partial=False)

clear_box = (W - 160, 16, 140, 48)
last = None

while True:
    pts = touch.touches()
    if not pts:
        last = None
        time.sleep(0.02)
        continue

    x, y, size, tid = pts[0]
    # CLEAR button
    bx, by, bw, bh = clear_box
    if bx <= x < bx + bw and by <= y < by + bh:
        epd.fill(15)
        epd.text("TOUCH DEMO", 20, 20, 0, scale=3)
        epd.text("cleared", 20, 60, 0, scale=2)
        epd.fill_rect(bx, by, bw, bh, 0)
        epd.text("CLEAR", W - 140, 28, 15, scale=2)
        epd.show(mode=MODE_GC16, partial=False)
        last = None
        time.sleep(0.3)
        continue

    r = 6 if size < 20 else 10
    epd.fill_circle(x, y, r, 0)
    if last is not None:
        epd.line(last[0], last[1], x, y, 0)
    last = (x, y)
    epd.show(mode=MODE_DU, partial=True)
    time.sleep(0.03)
