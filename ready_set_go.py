import time
import math
from cosmic import CosmicUnicorn, Channel
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY

'''
Displays some text, gradients and colours and demonstrates button use.

You can adjust the brightness with LUX + and -.
'''

cu = CosmicUnicorn()
graphics = PicoGraphics(DISPLAY)

width = CosmicUnicorn.WIDTH
height = CosmicUnicorn.HEIGHT

seconds = -1

boopety_beepety = cu.synth_channel(0)
# boopety_beepety.configure(
#     waveforms=Channel.SQUARE | Channel.SINE,
#     attack=0.1,
#     decay=0.1,
#     sustain=0,
#     release=0.1,
#     volume=1.0
# )

# Configure the beeper waveform and envelope
boopety_beepety.configure(
    waveforms=Channel.SINE + Channel.SQUARE,
    attack=0.05,
    decay=0.5,
    sustain=0,
    release=0,
    volume=1.0
)
boopety_beepety.frequency(262)

cu.play_synth()

last_action = time.ticks_ms()

def debounce(duration=1000):
    global last_action
    if time.ticks_ms() - last_action > duration:
        last_action = time.ticks_ms()
        return True
    return False

def gradient(r, g, b):
    for y in range(0, height):
        for x in range(0, width):
            graphics.set_pen(graphics.create_pen(int((r * (height - y)) / 32), int((g * (height - y)) / 32), int((b * (height - y)) / 32)))
            graphics.pixel(x, y)


def grid(r, g, b):
    for y in range(0, height):
        for x in range(0, width):
            if (x + y) % 2 == 0:
                graphics.set_pen(graphics.create_pen(r, g, b))
            else:
                graphics.set_pen(0)
            graphics.pixel(x, y)

def grid_gradient(r, g, b):
    for y in range(0, height):
        for x in range(0, width):
            if (x + y) % 2 == 0:
                graphics.set_pen(graphics.create_pen(int((r * (height - y)) / 32), int((g * (height - y)) / 32), int((b * (height - y)) / 32)))
            else:
                graphics.set_pen(0)
            graphics.pixel(x, y)

def outline_text(text):
    ms = time.ticks_ms()

    graphics.set_font("bitmap8")
    v = int((math.sin(ms / 100.0) + 1.0) * 127.0)
    w = graphics.measure_text(text, 1)

    x = int(32 / 2 - w / 2 + 1)
    y = 12

    graphics.set_pen(0)
    graphics.text(text, x - 1, y - 1, -1, 1)
    graphics.text(text, x, y - 1, -1, 1)
    graphics.text(text, x + 1, y - 1, -1, 1)
    graphics.text(text, x - 1, y, -1, 1)
    graphics.text(text, x + 1, y, -1, 1)
    graphics.text(text, x - 1, y + 1, -1, 1)
    graphics.text(text, x, y + 1, -1, 1)
    graphics.text(text, x + 1, y + 1, -1, 1)

    graphics.set_pen(graphics.create_pen(v, v, v))
    graphics.text(text, x, y, -1, 1)

def outline_text_lower(text):
    graphics.set_font("bitmap6")

    w = graphics.measure_text(text, 1)

    # x = int(32 / 2 - w / 2 + 1)
    x = 1
    y = 26

    graphics.set_pen(0)
    graphics.text(text, x - 1, y - 1, -1, 1)
    graphics.text(text, x, y - 1, -1, 1)
    graphics.text(text, x + 1, y - 1, -1, 1)
    graphics.text(text, x - 1, y, -1, 1)
    graphics.text(text, x + 1, y, -1, 1)
    graphics.text(text, x - 1, y + 1, -1, 1)
    graphics.text(text, x, y + 1, -1, 1)
    graphics.text(text, x + 1, y + 1, -1, 1)

    graphics.set_pen(graphics.create_pen(255, 255, 255))
    graphics.text(text, x, y, -1, 1)

cu.set_brightness(0.5)
start = time.ticks_ms()

while True:

#     elapsed = (time.clock() - start)

    # elapsed
    time_ms = time.ticks_ms() - start
    if seconds != -1:
        seconds = (time_ms // 1000) % 5

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_UP):
        cu.adjust_brightness(+0.01)

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_DOWN):
        cu.adjust_brightness(-0.01)

    graphics.set_pen(graphics.create_pen(0, 0, 0))
    graphics.clear()

    text = ""
    timer_text = str(time_ms)[3:]

    if seconds == 0:
        print("grid pattern")
        grid(255, 255, 255)
    elif seconds == 1:
        print("red gradient")
        text = "Ready"
        gradient(255, 0, 0)
    elif seconds == 2:
        print("red gradient")
        text = "Ready"
        gradient(255, 0, 0)
    elif seconds == 3:
        print("yellow gradient")
        text = "Set"
        gradient(255, 255, 0)
    elif seconds == 4:
        print("green gradient")
        text = "Go"
        gradient(0, 255, 0)
        boopety_beepety.frequency(523)

    elif seconds == 5:
        print("green gradient")
        text = "Go"
        gradient(0, 255, 0)
    elif seconds == 5:
        print("white gradient")
        gradient(255, 255, 255)
    elif seconds == -1:
        print("gray gradient")
        grid_gradient(100, 100, 100)
        boopety_beepety.frequency(131)

    if cu.is_pressed(CosmicUnicorn.SWITCH_A):
        text = "Start"
        seconds = 0

    if cu.is_pressed(CosmicUnicorn.SWITCH_B):
        text = "Stop"
        seconds = -1

    if cu.is_pressed(CosmicUnicorn.SWITCH_C):
        text = "C"

    if cu.is_pressed(CosmicUnicorn.SWITCH_D):
        text = "D"

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

    outline_text(text)
    outline_text_lower(timer_text)
    
    if debounce(1000):
        boopety_beepety.trigger_attack()
    cu.update(graphics)
    time.sleep(0.1)
