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


# Check whether the RTC time has changed and if so redraw the display
def redraw_display_if_reqd():
    global year, month, day, wd, hour, minute, second, last_second

    year, month, day, wd, hour, minute, second, _ = rtc.datetime()
    if second != last_second:
        hour = (hour + utc_offset) % 24

        if hour == WAKEUP_HOUR:
            gradient(0,255,0)
        elif hour > WAKEUP_HOUR and hour < WAKEUP_HOUR + 10:
            gradient(255,255,0)
        else:
            gradient(255,0,0)


        clock = "{:02}:{:02}".format(hour, minute)

    
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
