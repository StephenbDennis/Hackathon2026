# SPDX-FileCopyrightText: 2026 Alexander Huey for Kinetic Technologies, Inc.
#
# SPDX-License-Identifier: MIT

"""
#################################################
# README ########################################
#################################################
# KTD2061 Line Example Software
#     by Alexander Huey, Kinetic Technologies
#     Revision 1.00 - March 12th, 2026
#
# This file contains example QTPY RP2040 code using the
#   Kinetic RGB driver for the KTD2061 Product Line.
#
# Refer to Kinetic_RGB.py for all definitions for KineticRGB.<FunctionName>
# Additionally, Kinetic_RGB.py handles all input validation for function inputs
# For quick modifications, search up "##"
#   All important lines to be changed are marked with said symbol
"""

# module imports
import time

import board
import busio

from kinetic_rgb import *
from kinetic_rgb import KTD2061  ## Import Product Class

_i2cbus = busio.I2C(board.SCL1, board.SDA1, frequency=100000)
KineticRGB = KTD2061(_i2cbus)  ## Assign Bus to Class


# Functions Begin =================================================================================
def allrgb_normalmode(fade_rate0):
    # KineticRGB.global_control(
    # enableMode=EnableMode.MODE_DAY,
    # brightExtend=1,
    # coolExtend=CoolExtend_Temp.DEGREES_105C,
    # fadeRate=fadeRate
    # )
    KineticRGB.global_control(EnableMode.MODE_DAY, fade_rate0=fade_rate0)


def allrgb_nightmode(fade_rate0):
    # KineticRGB.global_control(
    # enableMode=EnableMode.MODE_NIGHT,
    # brightExtend=1,
    # coolExtend=CoolExtend_Temp.DEGREES_105C,
    # fadeRate=fadeRate
    # )
    KineticRGB.global_control(EnableMode.MODE_NIGHT, fade_rate0=fade_rate0)


def allrgb_off(fade_rate0):
    # KineticRGB.global_control(
    #     enableMode=EnableMode.MODE_GLOBAL_OFF,
    #     brightExtend=1,
    #     coolExtend=CoolExtend_Temp.DEGREES_105C,
    #     fadeRate=fadeRate
    # )
    KineticRGB.global_control(EnableMode.MODE_GLOBAL_OFF, fade_rate0=fade_rate0)
    KineticRGB.set_rgb_module_to_off(KTD2061RGBModuleSelect.RGB_MODULE_ALL)


def global_reset():
    KineticRGB.global_reset_to_defaults()


def color_mix_example(fade, delay, r0, g0, b0, r1, g1, b1):  # noqa: PLR0917, PLR0913
    color0 = r0 << 16 | g0 << 8 | b0  # create the RGB hex code
    color1 = r1 << 16 | g1 << 8 | b1  # create the RGB hex code

    allrgb_off(fade)  # Have all LEDs off
    for i in range(8):  # Set up all 8 color options
        blu_option = (i >> 0) & 1
        grn_option = (i >> 1) & 1
        red_option = (i >> 2) & 1

        module_num = i + 2 if (i < 4) else i + 4  # 8 Options -> Modules 2, 3, 4, 5, 8, 9, 10, 11
        KineticRGB.set_rgb_module_color_mix(module_num, red_option, grn_option, blu_option)
        KineticRGB.set_rgb_module_to_on(module_num)

    print("Showing SRGB Adjustment")
    KineticRGB.set_color0(color0, True)
    KineticRGB.set_color1(color1, True)
    allrgb_normalmode(fade)  # Show SRGB colors in normal mode
    time.sleep(delay)
    allrgb_nightmode(fade)  # Show SRGB colors in night mode
    time.sleep(delay)

    print("Showing no SRGB Adjustment")
    allrgb_normalmode(fade)
    KineticRGB.set_color0(color0, False)
    KineticRGB.set_color1(color1, False)
    time.sleep(delay)
    allrgb_nightmode(fade)
    time.sleep(delay)

    allrgb_off(fade)


def brightness_adjustment_example(fade, delay):
    allrgb_off(fade)
    KineticRGB.set_color1(0xFFFFFF)
    KineticRGB.set_rgb_module_color_mix(KTD2061RGBModuleSelect.RGB_MODULE_ALL, 1, 1, 1)
    KineticRGB.set_rgb_module_to_on(KTD2061RGBModuleSelect.RGB_MODULE_ALL, fade_rate=fade)
    allrgb_normalmode(fade)

    # remember, blue > green > red in terms of intensity/strength
    print("Decrease current blue brightness by 50%")
    for _ in range(3):
        KineticRGB.set_color1_led_brightness(RGBSelectLed.BLUE, 50)
        time.sleep(delay)

    print("Decrease current green brightness by 50%")
    for _ in range(3):
        KineticRGB.set_color1_led_brightness(RGBSelectLed.GREEN, 50)
        time.sleep(delay)

    print("Decrease current red brightness by 50%")
    for _ in range(3):
        KineticRGB.set_color1_led_brightness(RGBSelectLed.RED, 50)
        time.sleep(delay)

    print("Restore to original color by increasing brightness")
    for _ in range(3):
        KineticRGB.set_color1_led_brightness(RGBSelectLed.MODULE, 150)
        time.sleep(delay)

    allrgb_off(fade)


# SetUp Defaults
global_reset()
KineticRGB.global_control(
    enable_mode=EnableMode.MODE_DAY,
    bright_ext=1,
    cool_ext=CoolExtendTemp.DEGREES_105C,
    fade_rate0=None,
)
KineticRGB.check_device_status()
allrgb_off(FadeRate.RATE_63MS)
while True:
    print("All Combinations of Color0 and Color1 Example (with and without SRGB)")
    color_mix_example(FadeRate.RATE_63MS, 2, 127, 127, 127, 255, 255, 255)
    time.sleep(5)
    print("Brightness Adjustment Example")
    brightness_adjustment_example(FadeRate.RATE_63MS, 1)
