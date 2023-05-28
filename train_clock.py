# Clock example with NTP synchronization
#
# Create a secrets.py with your Wifi details to be able to get the time
# when the Cosmic Unicorn isn't connected to Thonny.
#
# secrets.py should contain:
# WIFI_SSID = "Your WiFi SSID"
# WIFI_PASSWORD = "Your WiFi password"
#
# Clock synchronizes time on start, and resynchronizes if you press the A button

import time
import math
import machine
import network
import ntptime
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY
from bitfonts import BitFont, font5x9
try:
    from secrets import WIFI_SSID, WIFI_PASSWORD
    wifi_available = True
except ImportError:
    print("Create secrets.py with your WiFi credentials to get time from NTP")
    wifi_available = False


# constant for wakeup hour of green color
WAKEUP_HOUR = 6
UTC_OFFSET_HOUR = -7


# create cosmic object and graphics surface for drawing
cu = CosmicUnicorn()
graphics = PicoGraphics(DISPLAY)
bitfont = BitFont(graphics)

# create the rtc object
rtc = machine.RTC()

width = CosmicUnicorn.WIDTH
height = CosmicUnicorn.HEIGHT

# set up some pens to use later
WHITE = graphics.create_pen(255, 255, 255)
BLACK = graphics.create_pen(0, 0, 0)
DARK_YELLOW = graphics.create_pen(50, 50, 0)
DARK_RED = graphics.create_pen(30, 0, 0)
DARK_GRAY = graphics.create_pen(20, 20, 20)
LIGHT_GRAY = graphics.create_pen(120, 120, 120)
DARK_CYAN = graphics.create_pen(0, 120, 120)
YELLOW = graphics.create_pen(255, 255, 0)

def gradient(r, g, b):
    for y in range(0, height):
        for x in range(0, width):
            graphics.set_pen(graphics.create_pen(int((r * (height - y)) / 32), int((g * (height - y)) / 32), int((b * (height - y)) / 32)))
            graphics.pixel(x, y)

# function for drawing outlined text
def outline_text_custom_font(text, x, y, font):
    graphics.set_pen(BLACK)
    bitfont.draw_text(text, x - 1, y - 1, font)
    bitfont.draw_text(text, x, y - 1, font)
    bitfont.draw_text(text, x + 1, y - 1, font)
    bitfont.draw_text(text, x - 1, y, font)
    bitfont.draw_text(text, x + 1, y, font)
    bitfont.draw_text(text, x - 1, y + 1, font)
    bitfont.draw_text(text, x, y + 1, font)
    bitfont.draw_text(text, x + 1, y + 1, font)

    graphics.set_pen(WHITE)
    bitfont.draw_text(text, x, y, font)

# Connect to wifi and synchronize the RTC time from NTP
def sync_time():
    if not wifi_available:
        return

    # Start connection
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    # Wait for connect success or failure
    max_wait = 100
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(0.2)

        redraw_display_if_reqd()
        cu.update(graphics)

    if max_wait > 0:
        print("Connected")

        try:
            ntptime.settime()
            print("Time set")
        except OSError:
            pass

    wlan.disconnect()
    wlan.active(False)


# NTP synchronizes the time to UTC, this allows you to adjust the displayed time
# by one hour increments from UTC by pressing the volume up/down buttons
#
# We use the IRQ method to detect the button presses to avoid incrementing/decrementing
# multiple times when the button is held.
utc_offset = UTC_OFFSET_HOUR

up_button = machine.Pin(CosmicUnicorn.SWITCH_VOLUME_UP, machine.Pin.IN, machine.Pin.PULL_UP)
down_button = machine.Pin(CosmicUnicorn.SWITCH_VOLUME_DOWN, machine.Pin.IN, machine.Pin.PULL_UP)


def adjust_utc_offset(pin):
    global utc_offset
    if pin == up_button:
        utc_offset += 1
    if pin == down_button:
        utc_offset -= 1


up_button.irq(trigger=machine.Pin.IRQ_FALLING, handler=adjust_utc_offset)
down_button.irq(trigger=machine.Pin.IRQ_FALLING, handler=adjust_utc_offset)


year, month, day, wd, hour, minute, second, _ = rtc.datetime()

last_second = second

def tracks(y=30):
    graphics.set_pen(LIGHT_GRAY)
    graphics.line(0, y, 32, y)
    for tie in range(11):
        graphics.set_pen(DARK_YELLOW)
        graphics.line(4*tie, y+1, 4*tie+2, y+1)
    
def train(x,y):
    # LEFT FACING
    # NOSE AND WINDOW FRAME
    graphics.set_pen(DARK_CYAN)
    graphics.polygon([
      (x, y),
      (x+26, y),
      (x+26, y-5),
      (x+5, y-5),
      (x, y),
    ])
    # ROOF
    graphics.set_pen(LIGHT_GRAY)
    graphics.line(x+6, y-6, x+27, y-6)
    graphics.line(x+5, y-5, x+27, y-5)
    # BOTTOM FRAME
    graphics.polygon([
      (x, y),
      (x+26, y),
      (x+26, y+4),
      (x+2, y+4),
      (x, y),
    ])
    # WHEEL WELLS
    graphics.set_pen(BLACK)
    graphics.polygon([
      (x+4, y+4),
      (x+4, y+5),
      (x+11, y+5),
      (x+11, y+4),
      (x+10, y+2),
      (x+6, y+2),
      (x+4, y+4),
    ])
    # WHEELS
    graphics.set_pen(LIGHT_GRAY)
    graphics.line(x+5, y+4, x+7, y+4)
    graphics.line(x+5, y+5, x+7, y+5)   
    graphics.line(x+9, y+4, x+11, y+4)
    graphics.line(x+9, y+5, x+11, y+5)

def littlez(x,y):
    graphics.set_pen(LIGHT_GRAY)
    graphics.line(x, y, x+3, y)
    graphics.line(x, y+2, x+3, y+2)
    graphics.set_pen(WHITE)
    graphics.line(x+2, y, x, y+3)
    
def bigz(x,y):
    graphics.set_pen(WHITE)
    graphics.line(x, y, x+4, y)
    graphics.line(x+3, y, x, y+3)
    graphics.line(x, y+3, x+4, y+3)
    
def sleepface(x,y):
    # ADDS A SLEEP FACE TO LEFT FACING TRAIN AT SAME X Y
    graphics.set_pen(BLACK)
    # EYE
    graphics.polygon([
      (x+3, y-1),
      (x+6, y-4),
      (x+13, y-4),
      (x+4, y-1),
    ])
    # MOUTH
    graphics.polygon([
      (x, y),
      (x+3, y),
      (x+1, y+2),
      (x, y+1),
    ])

def wakeface(x,y):
    # ADDS A WAKING FACE TO LEFT FACING TRAIN AT SAME X Y
    # EYE
    graphics.set_pen(WHITE)
    graphics.polygon([
      (x + 5, y - 2),
      (x + 7, y - 4),
      (x + 7, y - 4),
      (x + 8, y - 2),
      (x + 7, y - 1),
      (x + 6, y - 1),
    ])
    # PUPIL
    graphics.set_pen(BLACK)
    graphics.line(x + 6, y - 2, x + 8, y - 2)

    # MOUTH OPEN SMILE
    graphics.set_pen(BLACK)
    graphics.polygon([
      (x, y),
      (x+3, y),
      (x+1, y+2),
      (x, y+1),
    ])
    graphics.line(x + 2, y, x + 4, y)

# Check whether the RTC time has changed and if so redraw the display
def redraw_display_if_reqd():
    global year, month, day, wd, hour, minute, second, last_second

    year, month, day, wd, hour, minute, second, _ = rtc.datetime()
    if second != last_second:
        hour = (hour + utc_offset) % 24

        if hour == WAKEUP_HOUR:
            gradient(0,255,0)
        elif hour > WAKEUP_HOUR and hour < WAKEUP_HOUR + 10:
            gradient(40,40,255)
            graphics.set_pen(YELLOW)
            graphics.circle(32, 0, 9)
        else:
            gradient(255,0,0)


        clock = "{:02}:{:02}".format(hour, minute)
        
        tracks()
        train(7, 24)
        if hour < WAKEUP_HOUR or hour >= WAKEUP_HOUR + 10:
            littlez(5, 18)
            bigz(0, 13)
            sleepface(7,24)
        else:
            wakeface(7,24)
        outline_text_custom_font(clock, 3, 2, font5x9)

        last_second = second


# set the font
graphics.set_font("bitmap8")
cu.set_brightness(0.5)

sync_time()

while True:
    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_UP):
        cu.adjust_brightness(+0.01)

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_DOWN):
        cu.adjust_brightness(-0.01)

    if cu.is_pressed(CosmicUnicorn.SWITCH_A):
        sync_time()

    redraw_display_if_reqd()

    # update the display
    cu.update(graphics)

    time.sleep(0.01)
