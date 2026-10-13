"""Demo vitrine m5paper_epd — paysage.

Modifie GIT_URL ci-dessous avec ton depot.
"""

from m5paper_epd import EPD, MODE_GC16

# <<< ton lien git (affiche tel quel, sans https:// si trop long)
GIT_URL = "github.com/Freyr86/m5paper_epd"
LIB_VER = "0.2.0"


def run(git_url=GIT_URL):
    epd = EPD(orientation="landscape", invert=False)
    W, H = epd.width, epd.height

    epd.init_clear()
    epd.fill(15)

    # --- Bandeau haut ---
    epd.fill_rect(0, 0, W, 72, 0)
    epd.text("M5PAPER", 24, 18, 15, scale=3)
    epd.text("e-paper", W - 200, 28, 15, scale=2)

    # --- Accroche ---
    epd.text("m5paper_epd", 24, 96, 0, scale=3)
    epd.text("CircuitPython  ·  IT8951  ·  16 gris", 24, 140, 0, scale=1)
    epd.text("v%s" % LIB_VER, W - 120, 100, 0, scale=2)

    # Ligne fine
    epd.hline(24, 168, W - 48, 0)

    # --- Ramp gris ---
    epd.text("GRAYSCALE", 24, 188, 0, scale=1)
    seg = (W - 48) // 16
    for i in range(16):
        epd.fill_rect(24 + i * seg, 208, seg - 2, 36, i)
        epd.rect(24 + i * seg, 208, seg - 2, 36, 0, thickness=1)

    # --- Formes deco ---
    epd.text("PRIMITIVES", 24, 268, 0, scale=1)
    epd.rect(24, 290, 100, 70, 0, thickness=2)
    epd.fill_rect(40, 306, 68, 38, 6)
    epd.circle(200, 325, 32, 0)
    epd.fill_circle(200, 325, 16, 0)
    epd.line(260, 290, 360, 360, 0)
    epd.line(260, 360, 360, 290, 0)
    epd.hline(260, 325, 100, 0)
    epd.vline(310, 290, 70, 0)

    # Petit panneau info
    epd.rect(400, 290, W - 424, 70, 0, thickness=2)
    epd.text("540 x 960 / 960 x 540", 416, 304, 0, scale=1)
    epd.text("INIT DU GC16 A2", 416, 324, 0, scale=1)
    epd.text("partial ~370ms", 416, 344, 0, scale=1)

    # --- Pied: git ---
    epd.fill_rect(0, H - 88, W, 88, 0)
    epd.text("SOURCE", 24, H - 72, 15, scale=1)
    # URL en blanc sur noir — tronquer si besoin
    url = git_url
    if len(url) > 40:
        epd.text(url[:40], 24, H - 48, 15, scale=2)
        epd.text(url[40:], 24, H - 24, 15, scale=2)
    else:
        epd.text(url, 24, H - 44, 15, scale=2)

    # Coins discrets
    epd.fill_rect(W - 18, 80, 10, 10, 0)
    epd.fill_rect(W - 18, H - 106, 10, 10, 0)

    epd.show(mode=MODE_GC16, partial=False)
    return epd


if __name__ == "__main__":
    run()
