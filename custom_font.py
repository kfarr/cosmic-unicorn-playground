# IMPORTS
import time
import math
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY
from bitmap_fonts import font2x5, font3x5, font4x5, font5x9

# INITIALISE GALACTIC UNICORN
cu = CosmicUnicorn()
graphics = PicoGraphics(DISPLAY)

width = CosmicUnicorn.WIDTH
height = CosmicUnicorn.HEIGHT


cu.set_brightness(0.3)

# DRAW A SINGLE BITMAP FONT CHARACTER
@micropython.native  # noqa: F821
def draw_char(d,x,y,f):
    # LOOP THROUGH ROWS
    for i in range(f[d]["h"]):
        # LOOP THROUGH COLUMNS
        for j in range(f[d]["w"]):
            # IF THIS BIT IS SET THEN DRAW A PIXEL
            if f[d]["data"] & (0b1 << ((i*f[d]["w"])+j)):
                graphics.pixel(f[d]["w"]-1-j+x,f[d]["h"]-1-i+y)

# DRAW A STRING WITH BITMAP FONT
@micropython.native  # noqa: F821
def draw_text(s,x,y,f,d=1):
    
    # LEFT JUSTIFIED
    if d == 1:
        for i in range(len(s)):
            draw_char(s[i],x,y,f)
            x += f[s[i]]["w"] + f[s[i]]["s"]
    else:
    # RIGHT JUSTIFIED
        for i in reversed(range(len(s))):
            x -= f[s[i]]["w"]
            draw_char(s[i],x,y,f)
            x -= f[s[i]]["s"]

paused = 0

# MAIN LOOP
while True:

    time_ms = time.ticks_ms()

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_UP):
        cu.adjust_brightness(+0.01)

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_DOWN):
        cu.adjust_brightness(-0.01)

    graphics.set_pen(graphics.create_pen(0, 0, 0))
    graphics.clear()

    text = "✋🚶"
    timer_text = str(time_ms)[3:]
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

    graphics.set_pen(graphics.create_pen(255, 255, 255))
    draw_text(timer_text,0,0,font2x5)

    draw_text(timer_text,0,6,font3x5)

    draw_text(timer_text,0,12,font4x5)

    draw_text(timer_text,0,16,font5x9)

    draw_text(text.upper(),6,26,font3x5)

    if paused:
        graphics.set_pen(graphics.create_pen(255, 0, 0))
        draw_char("-",(time_ms // 1000) % 2,21,font3x5)
    else:
        graphics.set_pen(graphics.create_pen(0, 255, 0))
        draw_char("-",(time_ms // 1000) % 2,23,font3x5)

    cu.update(graphics)

    # pause for a moment
#     time.sleep(0.1)

