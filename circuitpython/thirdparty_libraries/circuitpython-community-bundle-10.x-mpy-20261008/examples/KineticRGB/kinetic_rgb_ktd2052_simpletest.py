# SPDX-FileCopyrightText: 2026 Alexander Huey for Kinetic Technologies, Inc.
#
# SPDX-License-Identifier: MIT

"""
#################################################
# README ########################################
#################################################
# KTD2052 Line Example Software
#     by Alexander Huey, Kinetic Technologies
#     Revision 1.00 - March 12th, 2026
#
# This file contains example QTPY RP2040 code using the
#   Kinetic RGB driver for the KTD2052 Product Line.
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
from kinetic_rgb import KTD2052A  ## Import Product Class

_i2cbus = busio.I2C(board.SCL1, board.SDA1, frequency=100000)
ktd2052 = KTD2052A(_i2cbus)  ## Assign Bus to Class


# Functions Begin =================================================================================
def allrgb_normalmode(fade_rate0):
    # KineticRGB.global_control(
    # enableMode=EnableMode.MODE_DAY,
    # brightExtend=1,
    # coolExtend=CoolExtendTemp.DEGREES_105C,
    # fadeRate=fade_rate0
    # )
    ktd2052.global_control(EnableMode.MODE_DAY, fade_rate0=fade_rate0)


def allrgb_nightmode(fade_rate0):
    # KineticRGB.global_control(
    # enableMode=EnableMode.MODE_NIGHT,
    # brightExtend=1,
    # coolExtend=CoolExtendTemp.DEGREES_105C,
    # fadeRate=fade_rate0
    # )
    ktd2052.global_control(EnableMode.MODE_NIGHT, fade_rate0=fade_rate0)


def allrgb_off(fade_rate0):
    # KineticRGB.global_control(
    # enableMode=EnableMode.MODE_GLOBAL_OFF,
    # brightExtend=1,
    # coolExtend=CoolExtendTemp.DEGREES_105C,
    # fadeRate=fade_rate0
    # )
    ktd2052.global_control(EnableMode.MODE_GLOBAL_OFF, fade_rate0=fade_rate0)


def global_reset():
    ktd2052.global_reset_to_defaults()


def srgb_example(r0, g0, b0, r1, g1, b1):  # noqa: PLR0917, PLR0913
    color0 = r0 << 16 | g0 << 8 | b0  # create the RGB hexcode
    color1 = r1 << 16 | g1 << 8 | b1  # create the RGB hexcode
    allrgb_off(FadeRate.RATE_125MS)
    # color 0 and color 1 with/without SRGB
    ktd2052.set_rgbx_color(color0, KTD2052RGBModuleSelect.RGB_MODULE_1, True)
    ktd2052.set_rgbx_color(color0, KTD2052RGBModuleSelect.RGB_MODULE_2, False)
    ktd2052.set_rgbx_color(color1, KTD2052RGBModuleSelect.RGB_MODULE_3, True)
    ktd2052.set_rgbx_color(color1, KTD2052RGBModuleSelect.RGB_MODULE_4, False)
    allrgb_normalmode(FadeRate.RATE_125MS)

    time.sleep(2)
    for _ in range(5):
        r0 = min(255, r0 + 10)  # show behavior when increasing (max 255)
        g0 = min(255, g0 + 10)  # show behavior when increasing (max 255)
        b0 = min(255, b0 + 10)  # show behavior when increasing (max 255)
        color0 = r0 << 16 | g0 << 8 | b0

        r1 = max(0, r1 - 10)  # show behavior when decreasing (min 0)
        g1 = max(0, g1 - 10)  # show behavior when decreasing (min 0)
        b1 = max(0, b1 - 10)  # show behavior when decreasing (min 0)
        color1 = r1 << 16 | g1 << 8 | b1

        ktd2052.set_rgbx_color(color0, KTD2052RGBModuleSelect.RGB_MODULE_1, True)
        ktd2052.set_rgbx_color(color0, KTD2052RGBModuleSelect.RGB_MODULE_2, False)
        ktd2052.set_rgbx_color(color1, KTD2052RGBModuleSelect.RGB_MODULE_3, True)
        ktd2052.set_rgbx_color(color1, KTD2052RGBModuleSelect.RGB_MODULE_4, False)
        time.sleep(1)


def brightness_adjustment_example(fade, delay):
    allrgb_off(FadeRate.RATE_125MS)
    ktd2052.set_rgbx_color(0xFFFFFF)  # default is all LEDs

    allrgb_normalmode(fade)
    time.sleep(5)
    for _ in range(5):
        ktd2052.set_colorx_led_brightness(
            RGBSelectLed.MODULE, KTD2052RGBModuleSelect.RGB_MODULE_1, 50
        )  # decrease blue current brightness by 50%
        ktd2052.set_colorx_led_brightness(
            RGBSelectLed.RED, KTD2052RGBModuleSelect.RGB_MODULE_2, 50
        )  # decrease red current brightness by 50%
        ktd2052.set_colorx_led_brightness(
            RGBSelectLed.GREEN, KTD2052RGBModuleSelect.RGB_MODULE_3, 50
        )  # decrease green current brightness by 50%
        ktd2052.set_colorx_led_brightness(
            RGBSelectLed.BLUE, KTD2052RGBModuleSelect.RGB_MODULE_4, 50
        )  # decrease blue current brightness by 50%
        time.sleep(delay)

    for _ in range(5):
        ktd2052.set_colorx_led_brightness(
            RGBSelectLed.MODULE, KTD2052RGBModuleSelect.RGB_MODULE_1, 150
        )  # Restore decreased overall current brightness by 50%
        ktd2052.set_colorx_led_brightness(
            RGBSelectLed.RED, KTD2052RGBModuleSelect.RGB_MODULE_2, 150
        )  # Restore decreased red current brightness by 50%
        ktd2052.set_colorx_led_brightness(
            RGBSelectLed.GREEN, KTD2052RGBModuleSelect.RGB_MODULE_3, 150
        )  # Restore decreased green current brightness by 50%
        ktd2052.set_colorx_led_brightness(
            RGBSelectLed.BLUE, KTD2052RGBModuleSelect.RGB_MODULE_4, 150
        )  # Restore decreased blue current brightness by 50%
        time.sleep(delay)

    allrgb_off(fade)


def pattern_generator_example(cycles, fade1):
    allrgb_off(FadeRate.RATE_125MS)
    ktd2052.set_rgbx_color(0xFFFFFF)  # default is all LEDs
    ktd2052.pattern_gen_control(
        patterngen_mode=KTD2052PatternGenModes.GENERATE_8_PATTERNS,
        pattern_duration=KTD2052PatternTimeLen.DURATION_188MS,
        patterngen_fade_rate1=fade1,
    )
    # use fade1 for all 8 pattern slots, can also use fade0 if desired
    ktd2052.pattern_slot_fade_selection(0b11111111)

    ktd2052.pattern_configuration_rgb(
        rgb_module=KTD2052RGBModuleSelect.RGB_MODULE_1, pattern_config=0b10000001
    )  # control RGB1 on/off in each patern slot (7 -> 0)
    ktd2052.pattern_configuration_rgb(
        rgb_module=KTD2052RGBModuleSelect.RGB_MODULE_2, pattern_config=0b01000010
    )  # control RGB2 on/off in each patern slot (7 -> 0)
    ktd2052.pattern_configuration_rgb(
        rgb_module=KTD2052RGBModuleSelect.RGB_MODULE_3, pattern_config=0b00100100
    )  # control RGB3 on/off in each patern slot (7 -> 0)
    ktd2052.pattern_configuration_rgb(
        rgb_module=KTD2052RGBModuleSelect.RGB_MODULE_4, pattern_config=0b00011000
    )  # control RGB4 on/off in each patern slot (7 -> 0)

    # Alternate way to configure the patterns by slot for visualization/convenience
    # KineticRGB.pattern_configuration_slot(
    #   patternSlot = 7,
    #   rgb1On = True,
    #   rgb2On = False,
    #   rgb3On = False,
    #   rgb4On = False
    # )
    # KineticRGB.pattern_configuration_slot(
    #   patternSlot = 6,
    #   rgb1On = False,
    #   rgb2On = True,
    #   rgb3On = False,
    #   rgb4On = False
    # )
    # KineticRGB.pattern_configuration_slot(
    #   patternSlot = 5,
    #   rgb1On = False,
    #   rgb2On = False,
    #   rgb3On = True,
    #   rgb4On = False
    # )
    # KineticRGB.pattern_configuration_slot(
    #   patternSlot = 4,
    #   rgb1On = False,
    #   rgb2On = False,
    #   rgb3On = False,
    #   rgb4On = True
    # )
    # KineticRGB.pattern_configuration_slot(
    #   patternSlot = 3,
    #   rgb1On = False,
    #   rgb2On = False,
    #   rgb3On = False,
    #   rgb4On = True)
    #   # Config RGB Status for Slot 3
    # KineticRGB.pattern_configuration_slot(
    #   patternSlot = 2,
    #   rgb1On = False,
    #   rgb2On = False,
    #   rgb3On = True,
    #   rgb4On = False
    # )
    # KineticRGB.pattern_configuration_slot(
    #   patternSlot = 1,
    #   rgb1On = False,
    #   rgb2On = True,
    #   rgb3On = False,
    #   rgb4On = False
    # )
    # KineticRGB.pattern_configuration_slot(
    #   patternSlot = 0,
    #   rgb1On = True,
    #   rgb2On = False,
    #   rgb3On = False,
    #   rgb4On = False
    # )

    # WDT must be set BEFORE control On -> otherwise cycle count will be off
    ktd2052.pattern_cycles_config_wdt(cycles)  # (255 = continue forever)
    allrgb_normalmode(FadeRate.RATE_125MS)  # sets fade0 (global Fade) & sets to normal Enable

    while 1:  # pattern generator will independently run cycles
        time.sleep(5)
        cycles_left = ktd2052.check_pattern_cycles_remaining()
        if cycles_left == 0:
            global_reset()  # clean regs
            break
        elif cycles_left == 40:
            ktd2052.set_rgbx_color(0x0000FF)  # colors can be changed mid cycle


global_reset()
ktd2052.global_control(
    enable_mode=EnableMode.MODE_DAY,
    bright_ext=1,
    cool_ext=CoolExtendTemp.DEGREES_105C,
    fade_rate0=None,
)

ktd2052.check_device_status()
allrgb_normalmode(FadeRate.RATE_125MS)  # sets fade0 (global Fade) & sets to normal Enable
allrgb_off(FadeRate.RATE_125MS)
while True:
    print("No Pattern Generatior, SRGB (Standard Red Green Blue) Adjustment Example")
    srgb_example(127, 127, 127, 90, 70, 60)
    time.sleep(5)
    print("No Pattern Generatior, Brightness Adjustment Example")
    brightness_adjustment_example(FadeRate.RATE_63MS, 3)
    time.sleep(5)
    print("Pattern Generator Example")
    pattern_generator_example(50, FadeRate.RATE_63MS)
    time.sleep(5)
