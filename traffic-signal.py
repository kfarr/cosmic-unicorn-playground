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

# SIGNAL HEAD FUNCTION
def draw_signal_head(x, y, lamp="none"):
    # R
    graphics.set_pen(graphics.create_pen(15, 0, 0))
    if lamp == "R":
        graphics.set_pen(graphics.create_pen(255, 0, 0))
    graphics.pixel(x, y) 
    # Y
    graphics.set_pen(graphics.create_pen(15, 15, 0))
    if lamp == "Y":
        graphics.set_pen(graphics.create_pen(255, 255, 0))
    graphics.pixel(x, y + 1)
    # G
    graphics.set_pen(graphics.create_pen(0, 15, 0))
    if lamp == "G":
        graphics.set_pen(graphics.create_pen(0, 255, 0))
    graphics.pixel(x, y + 2)
        
def draw_row(n, y, state, state_ped):
    # ROW LABEL
    graphics.set_pen(graphics.create_pen(100, 100, 100))
    draw_char(str(n), 0, y, font3x5)

    # PED COUNTER BG
    graphics.set_pen(graphics.create_pen(15, 0, 0))
    draw_text("00", 10, y, font2x5)
    
    # SIGNALS MAST
    graphics.set_pen(graphics.create_pen(50, 50, 50))
    graphics.pixel(16, 5 + y)
    graphics.line(18, y - 1, 22, y - 1)
    graphics.line(22, y - 1, 22, 6 + y)
    
    # DRAW SIGNAL HEADS
    draw_signal_head(16, 2 + y, state)
    draw_signal_head(18, 0 + y, state)
    draw_signal_head(20, 0 + y, state)
    draw_signal_head(23, 2 + y, state)

    # PED SYMBOL
    if state_ped == "W":
        graphics.set_pen(graphics.create_pen(255, 255, 255))
        draw_char("🚶", 5, y, font3x5)
    if state_ped == "R":
        graphics.set_pen(graphics.create_pen(255, 0, 0))
        draw_char("✋", 5, y, font3x5)
    if state_ped == "F":
        invert_flash = 1 - (time_ms // 500) % 2
        graphics.set_pen(graphics.create_pen(255 * invert_flash, 0, 0))
        draw_char("✋", 5, y, font3x5)
# MAIN LOOP
while True:
    time_ms = time.ticks_ms()

    cycle_seconds = (time_ms // 1000) % 60

    graphics.set_pen(graphics.create_pen(0, 0, 0))
    graphics.clear()

    text = ""
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
        cu.adjust_brightness(+0.01)
        text = "Brite" + str(round(cu.get_brightness(),2))

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_DOWN):
        cu.adjust_brightness(-0.01)
        text = "Dark" + str(round(cu.get_brightness(),2))

    if cu.is_pressed(CosmicUnicorn.SWITCH_SLEEP):
        text = "Zzz..."

    phase2_timing = "GGGGGGGGGGGGGGGGGGGGYYYYRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
    phase2p_timing = "WWWWWFFFFFFFFFFFFFFRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWW"
    phase4_timing = "RRRRRRRRRRRRRRRRRRRRRRRRRRRRGGGGGGGGGGGGGGGGGGGGGGGYYYYRRRRR"
    phase4p_timing = "RRRRRRRRRRRRRRRRRRRRRRRRRRWWWWWWWWWFFFFFFFFFFFFFFFRRRRRRRRRR"

    draw_row(2, 1, phase2_timing[cycle_seconds], phase2p_timing[cycle_seconds])

    draw_row(4, 9, phase4_timing[cycle_seconds], phase4p_timing[cycle_seconds])
    
    graphics.set_pen(graphics.create_pen(100, 100, 100))

    draw_text(str(cycle_seconds),32,27,font3x5,-1)
    draw_text(text.upper(),0,20,font3x5)


    cu.update(graphics)

    # pause for a moment
#     time.sleep(0.1)

