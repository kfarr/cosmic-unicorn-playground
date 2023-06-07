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

cu.set_brightness(0.8)

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
        
def draw_signal_row(n, y, state, state_ped):
    # ROW LABEL
    graphics.set_pen(graphics.create_pen(100, 100, 100))
    bitfont.draw_char(str(n), 0, y, font3x5)

    # PED COUNTER BG
    if state_ped:
        graphics.set_pen(graphics.create_pen(15, 0, 0))
        bitfont.draw_text("00", 10, y, font2x5)
    
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
        bitfont.draw_char("🚶", 5, y, font3x5)
    if state_ped == "R":
        graphics.set_pen(graphics.create_pen(255, 0, 0))
        bitfont.draw_char("✋", 5, y, font3x5)
    if state_ped == "F":
        invert_flash = 1 - (time_ms // 500) % 2
        graphics.set_pen(graphics.create_pen(255 * invert_flash, 0, 0))
        bitfont.draw_char("✋", 5, y, font3x5)

def ped_timing_count_Fs(s):
    start_index = s.find('F')
    end_index = s.rfind('F')
    count = s.count('F')

    return count, start_index, end_index

def ped_timer_string(count, start_index, end_index, cycle_seconds):
    if cycle_seconds < start_index or cycle_seconds > end_index:
        return ""
    else:
        return str(end_index - cycle_seconds)



# INITIAL STATE
paused = 0
scene = 'A'

# TIMING
phase2_timing = "GGGGGGGGGGGGGGGGGGGGYYYYRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
phase2p_timing = "WWWWWFFFFFFFFFFFFFFRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRWW"
phase4_timing = "RRRRRRRRRRRRRRRRRRRRRRRRRRRRGGGGGGGGGGGGGGGGGGGGGGGYYYYRRRRR"
phase4p_timing = "RRRRRRRRRRRRRRRRRRRRRRRRRRWWWWWWWWWFFFFFFFFFFFFFFFRRRRRRRRRR"

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
        text = "Scene A"
        scene = 'A'

    if cu.is_pressed(CosmicUnicorn.SWITCH_B):
        text = "Scene B"
        scene = 'B'

    if cu.is_pressed(CosmicUnicorn.SWITCH_C):
        text = "Scene C"
        scene = 'C'

    if cu.is_pressed(CosmicUnicorn.SWITCH_D):
        text = "Scene D"
        scene = 'D'

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

    if scene == 'A':
        # DRAW SIGNALS
        draw_signal_row(2, 1, phase2_timing[cycle_seconds], phase2p_timing[cycle_seconds])
        draw_signal_row(4, 26, phase4_timing[cycle_seconds], phase4p_timing[cycle_seconds])
        # PED COUNTERS
        graphics.set_pen(graphics.create_pen(255, 0, 0))
        count, start_index, end_index = ped_timing_count_Fs(phase2p_timing)
        bitfont.draw_text(ped_timer_string(count, start_index, end_index, cycle_seconds),15,1,font2x5,-1)
        count4, start_index4, end_index4 = ped_timing_count_Fs(phase4p_timing)
        bitfont.draw_text(ped_timer_string(count4, start_index4, end_index4, cycle_seconds),15,26,font2x5,-1)
        # GLOBAL TIMER
        graphics.set_pen(graphics.create_pen(100, 100, 100))
        bitfont.draw_text(str(cycle_seconds),32,13,font3x5,-1)
    if scene == 'B':
        draw_signal_row(' ', 26, phase2_timing[cycle_seconds],'')
        # RED
        graphics.set_pen(graphics.create_pen(15, 0, 0))
        if phase2_timing[cycle_seconds] == 'R':
            graphics.set_pen(graphics.create_pen(255, 0, 0))
        graphics.circle(25, 6, 6)
        # YELLOW
        graphics.set_pen(graphics.create_pen(15, 15, 0))
        if phase2_timing[cycle_seconds] == 'Y':
            graphics.set_pen(graphics.create_pen(255, 255, 0))
        graphics.circle(15, 16, 6)
        # GREEN
        graphics.set_pen(graphics.create_pen(0, 15, 0))
        if phase2_timing[cycle_seconds] == 'G':
            graphics.set_pen(graphics.create_pen(0, 255, 0))
        graphics.circle(6, 25, 6)
        # GLOBAL TIMER
        graphics.set_pen(graphics.create_pen(50, 50, 50))
        bitfont.draw_text(str(cycle_seconds),32,27,font3x5,-1)
    if scene == 'C':
        draw_signal_row(' ', 26, phase2_timing[cycle_seconds],'')
        # RED
        graphics.set_pen(graphics.create_pen(15, 0, 0))
        if phase2_timing[cycle_seconds] == 'R':
            graphics.set_pen(graphics.create_pen(255, 0, 0))
        graphics.circle(15, 10, 10)
        # YELLOW
        graphics.set_pen(graphics.create_pen(15, 15, 0))
        if phase2_timing[cycle_seconds] == 'Y':
            graphics.set_pen(graphics.create_pen(255, 255, 0))
        graphics.circle(15, 31, 10)
        # GLOBAL TIMER
        graphics.set_pen(graphics.create_pen(50, 50, 50))
        bitfont.draw_text(str(cycle_seconds),32,27,font3x5,-1)

    if scene == 'D':
        # YELLOW
        graphics.set_pen(graphics.create_pen(15, 15, 0))
        if phase2_timing[cycle_seconds] == 'Y':
            graphics.set_pen(graphics.create_pen(255, 255, 0))
        graphics.circle(15, 0, 10)
        # GREEN
        graphics.set_pen(graphics.create_pen(0, 15, 0))
        if phase2_timing[cycle_seconds] == 'G':
            graphics.set_pen(graphics.create_pen(0, 255, 0))
        graphics.circle(15, 21, 10)
        # GLOBAL TIMER
        graphics.set_pen(graphics.create_pen(50, 50, 50))
        bitfont.draw_text(str(cycle_seconds),32,27,font3x5,-1)
    # STATUS TEXT
    bitfont.draw_text(text.upper(),0,20,font3x5)

    cu.update(graphics)

    # pause for a moment
#     time.sleep(0.1)


