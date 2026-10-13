"""Demo graphique de reference (paysage) — version validee impeccable."""

from m5paper_epd import EPD, MODE_GC16


def run():
    epd = EPD(orientation="landscape", invert=False)
    W, H = epd.width, epd.height

    epd.init_clear()
    epd.fill(15)

    epd.text("m5paper_epd", 20, 16, 0, scale=3)
    epd.text("test graphisme", 20, 56, 0, scale=2)

    epd.text("gris 0..15", 20, 100, 0, scale=1)
    seg = (W - 40) // 16
    bar_y, bar_h = 120, 48
    for i in range(16):
        epd.fill_rect(20 + i * seg, bar_y, seg, bar_h, i)
        if i in (0, 5, 10, 15):
            epd.text(str(i), 20 + i * seg + 4, bar_y + bar_h + 4, 0, scale=1)

    y0 = 200
    epd.rect(20, y0, 120, 80, 0, thickness=2)
    epd.fill_rect(40, y0 + 20, 80, 40, 8)
    epd.text("rect", 40, y0 + 90, 0, scale=1)

    epd.circle(220, y0 + 40, 36, 0)
    epd.fill_circle(220, y0 + 40, 18, 4)
    epd.text("circle", 190, y0 + 90, 0, scale=1)

    epd.line(300, y0, 420, y0 + 80, 0)
    epd.line(300, y0 + 80, 420, y0, 0)
    epd.hline(300, y0 + 40, 120, 0)
    epd.vline(360, y0, 80, 0)
    epd.text("lines", 330, y0 + 90, 0, scale=1)

    epd.text("Aa1 size1", 20, 340, 0, scale=1)
    epd.text("Aa1 size2", 20, 360, 0, scale=2)
    epd.text("Aa1 size3", 20, 400, 0, scale=3)

    epd.fill_rect(8, 8, 16, 16, 0)
    epd.fill_rect(W - 24, H - 24, 16, 16, 0)
    epd.text("TL", 28, 10, 0, scale=1)
    epd.text("BR", W - 48, H - 22, 0, scale=1)

    epd.show(mode=MODE_GC16, partial=False)
    return epd


if __name__ == "__main__":
    run()
