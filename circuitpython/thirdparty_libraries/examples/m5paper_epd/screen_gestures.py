"""Screen manager demo: click / hold / drag / swipe."""

from m5paper_epd import MODE_DU, MODE_GC16, Screen

screen = Screen(orientation="landscape", invert=False)
epd = screen.epd
W, H = screen.width, screen.height

epd.init_clear()
epd.fill(15)
epd.text("SCREEN GESTURES", 20, 20, 0, scale=2)
epd.text("click  hold  drag  swipe", 20, 60, 0, scale=1)
epd.show(mode=MODE_GC16, partial=False)

status_y = H - 40


def _status(msg):
    epd.fill_rect(0, status_y, W, 40, 15)
    epd.text(msg[:40], 16, status_y + 10, 0, scale=2)
    epd.show(mode=MODE_DU, partial=True)


@screen.on_click
def on_click(e):
    epd.fill_circle(e.x, e.y, 10, 0)
    epd.show(mode=MODE_DU, partial=True)
    _status("CLICK %d,%d" % (e.x, e.y))


@screen.on_hold
def on_hold(e):
    epd.rect(e.x - 18, e.y - 18, 36, 36, 0, thickness=3)
    epd.show(mode=MODE_DU, partial=True)
    _status("HOLD %d,%d" % (e.x, e.y))


@screen.on_drag
def on_drag(e):
    epd.line(e.x - e.dx, e.y - e.dy, e.x, e.y, 0)
    epd.show(mode=MODE_DU, partial=True)


@screen.on_swipe
def on_swipe(e):
    _status("SWIPE %s  d=%d" % (e.direction, e.distance))


screen.on(
    "drag_end",
    lambda e: _status("DRAG END %d,%d" % (e.x, e.y)),
)

print("gestures ready")
screen.run()
