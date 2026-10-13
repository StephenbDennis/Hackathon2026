"""Exemple minimal — à copier dans code.py ou lancer via REPL."""

from m5paper_epd import EPD, MODE_GC16

epd = EPD(rotation=90)
epd.init_clear()
epd.clear(15)
epd.text("Hello M5Paper", 30, 80, color=0, scale=3)
epd.show(mode=MODE_GC16)
