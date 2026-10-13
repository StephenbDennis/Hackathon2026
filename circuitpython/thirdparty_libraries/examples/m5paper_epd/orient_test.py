"""Test orientation paysage / portrait — meme motif logique.

Change ORIENT puis copie vers code.py (ou importe depuis code.py).
"""

from m5paper_epd import EPD, MODE_GC16

# "landscape" ou "portrait"
ORIENT = "landscape"


def draw_test(epd):
    W, H = epd.width, epd.height
    epd.fill(15)

    # Cadre
    epd.rect(2, 2, W - 4, H - 4, 0, thickness=2)

    # Coins: formes differentes pour les reconnaitre
    S = 32
    M = 8
    # TL: carre plein
    epd.fill_rect(M, M, S, S, 0)
    # TR: deux barres horizontales
    epd.fill_rect(W - M - S, M, S, 10, 0)
    epd.fill_rect(W - M - S, M + 22, S, 10, 0)
    # BL: barre verticale
    epd.fill_rect(M, H - M - S, 12, S, 0)
    # BR: cadre (plein + trou blanc)
    epd.fill_rect(W - M - S, H - M - S, S, S, 0)
    epd.fill_rect(W - M - S + 8, H - M - S + 8, S - 16, S - 16, 15)

    # Croix centrale
    cx, cy = W // 2, H // 2
    epd.hline(cx - 40, cy, 80, 0)
    epd.vline(cx, cy - 40, 80, 0)
    epd.fill_circle(cx, cy, 6, 0)

    # Axes depuis l'origine
    epd.hline(M + S + 4, M + S // 2, 60, 0)  # +X
    epd.vline(M + S // 2, M + S + 4, 60, 0)  # +Y

    # Texte
    epd.text(ORIENT.upper(), M, H // 2 - 20, 0, scale=2)
    epd.text("%dx%d" % (W, H), M, H // 2 + 10, 0, scale=2)
    epd.text("TL", M + 4, M + S + 4, 0, scale=1)
    epd.text("BR", W - M - 20, H - M - S - 12, 0, scale=1)


def run(orient=ORIENT):
    epd = EPD(orientation=orient, invert=False)
    print("orient", epd.orientation, epd.width, "x", epd.height)
    epd.init_clear()
    draw_test(epd)
    print("show...")
    epd.show(mode=MODE_GC16, partial=False)
    print("done")
    return epd


if __name__ == "__main__":
    run()
