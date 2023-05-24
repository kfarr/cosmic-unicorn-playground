# IMPORTS
import time
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

paused = 0
TEST_TEXT = "1234567890"

# MAIN LOOP
while True:

    time_ms = time.ticks_ms()

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_UP):
        cu.adjust_brightness(+0.01)

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_DOWN):
        cu.adjust_brightness(-0.01)

    graphics.set_pen(graphics.create_pen(0, 0, 0))
    graphics.clear()

#    text = "✋🚶"
#    timer_text = str(time_ms)[3:]
    text = "BITFONTS"
    if paused:
        text = "PICOFONTS"

    if cu.is_pressed(CosmicUnicorn.SWITCH_A):
        text = "A"
        paused = not paused

    if cu.is_pressed(CosmicUnicorn.SWITCH_B):
        text = "B"
        paused = not paused

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

    if not paused:
        bitfont.draw_text(TEST_TEXT,0,0,font2x5)
        bitfont.draw_text(TEST_TEXT,0,6,font3x5)
        bitfont.draw_text(TEST_TEXT,0,12,font4x5)
        bitfont.draw_text(TEST_TEXT,0,16,font5x9)
        bitfont.draw_text(text.upper(),0,26,font3x5)
    else:
        graphics.set_font('bitmap6')
        graphics.text(TEST_TEXT,0,-1,scale=1)
        graphics.set_font('bitmap8')
        graphics.text(TEST_TEXT,0,6,scale=1)
        graphics.set_font('bitmap14_outline')
        graphics.text(TEST_TEXT,0,12,scale=1)
        graphics.set_font('bitmap6')
        graphics.text(text.upper(),0,26,scale=1)
    
    cu.update(graphics)

    time.sleep(0.1)
