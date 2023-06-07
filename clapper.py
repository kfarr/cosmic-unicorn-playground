# IMPORTS
import time
import machine
import math
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY
from bitfonts import BitFont, font2x5, font3x5, font4x5, font5x9

# INITIALISE GALACTIC UNICORN
cu = CosmicUnicorn()
graphics = PicoGraphics(DISPLAY)
bitfont = BitFont(graphics)

width = CosmicUnicorn.WIDTH
height = CosmicUnicorn.HEIGHT

cu.set_brightness(1)

WHITE = graphics.create_pen(255, 255, 255)
RED = graphics.create_pen(255, 0, 0)
DARK_RED = graphics.create_pen(100, 0, 0)
LIGHT_GRAY = graphics.create_pen(120, 120, 120)

# create the rtc object
rtc = machine.RTC()

paused = 0

# CLAPPER HEADER
@micropython.native  # noqa: F821
def clapper_row(y=-1,x_offset=4):
    graphics.set_pen(LIGHT_GRAY)
    for tie in range(11):
        graphics.line(4*tie+x_offset, y+1, 4*tie+2+x_offset, y+1)
        graphics.line(4*tie+x_offset+1, y+2, 4*tie+2+x_offset+1, y+2)
        graphics.line(4*tie+x_offset+2, y+3, 4*tie+2+x_offset+2, y+3)

        graphics.line(4*tie+x_offset+2, y+5, 4*tie+2+x_offset+2, y+5)
        graphics.line(4*tie+x_offset+1, y+6, 4*tie+2+x_offset+1, y+6)
        graphics.line(4*tie+x_offset, y+7, 4*tie+2+x_offset, y+7)

# CLAPPER HEADER
@micropython.native  # noqa: F821
def dot_separators(y=12,x_offset=7):
    graphics.set_pen(DARK_RED)
    for tie in range(3):
        graphics.pixel(8*tie+x_offset, y+1)

year, month, day, wd, hour, minute, second, subsecond = rtc.datetime()

last_second = second;
last_second_tick = time.ticks_ms();

# MAIN LOOP
while True:
    year, month, day, wd, hour, minute, second, subsecond = rtc.datetime()

    if last_second != second:
        last_second = second
        last_second_tick = (time.ticks_diff(time.ticks_ms(), 0));

    time_ms = time.ticks_ms()
    time_ms_since_last_second = str(time.ticks_diff(time_ms, last_second_tick) / 1000)

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_UP):
        cu.adjust_brightness(+0.01)

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_DOWN):
        cu.adjust_brightness(-0.01)

    graphics.set_pen(graphics.create_pen(0, 0, 0))
    graphics.clear()

    text = "✋🚶"
    timer_text = "{:02}{:02}{:02}{:02}".format(hour, minute, second, time_ms_since_last_second[2:5])
    date_text = " 07 JUN"

    if paused:
        timer_text = "0123456789"

    if cu.is_pressed(CosmicUnicorn.SWITCH_A):
        text = "A"

    if cu.is_pressed(CosmicUnicorn.SWITCH_B):
        text = "B"

    if cu.is_pressed(CosmicUnicorn.SWITCH_C):
        text = "Play"
        paused = 0

    if cu.is_pressed(CosmicUnicorn.SWITCH_D):
        text = "Pause"
        paused = 1

    if cu.is_pressed(CosmicUnicorn.SWITCH_VOLUME_UP):
        text = "Louder!"

    if cu.is_pressed(CosmicUnicorn.SWITCH_VOLUME_DOWN):
        text = "Quieter"

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_UP):
        text = "Brighter!"

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_DOWN):
        text = "Darker"

    if cu.is_pressed(CosmicUnicorn.SWITCH_SLEEP):
        text = "Zzz... zzz..."

    graphics.set_pen(RED)

    bitfont.draw_text(timer_text,0,8,font3x5)

    bitfont.draw_text(str(date_text),0,14,font3x5)

 #   bitfont.draw_text(timer_text,0,16,font5x9)

    bitfont.draw_text(text.upper(),6,26,font3x5)

    clapper_row()
    dot_separators()
    if paused:
        graphics.set_pen(graphics.create_pen(255, 0, 0))
        bitfont.draw_char("-",(time_ms // 1000) % 2,21,font3x5)
    else:
        graphics.set_pen(graphics.create_pen(0, 255, 0))
        bitfont.draw_char("-",(time_ms // 1000) % 2,23,font3x5)

    cu.update(graphics)

    # pause for a moment
#     time.sleep(0.1)

