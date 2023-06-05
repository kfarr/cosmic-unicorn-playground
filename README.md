# Cosmic Unicorn Projects

MicroPython demos of custom bitmap fonts, a train-themed "Ok to Wake" clock, and more for the [Pimoroni Cosmic Unicorn LED Matrix with built-in Raspberry Pi Pico W 2040](https://shop.pimoroni.com/products/cosmic-unicorn).

Table of Contents:
* [Custom Tiny Bitmap Fonts](#custom-tiny-bitmap-fonts-for-cosmic-unicorn)
* [Ok to Wake Train Clock](#ok-to-wake-train-clock)
* Traffic Signals

## Custom (Tiny) Bitmap Fonts for Cosmic Unicorn

### Why?

The default bitmap fonts that come PicoGraphics library are awesome, but sometimes you need a smaller font to display lots of numbers and text on LED matrices such as the Cosmic Unicorn.

### What does it look like?
On the LEFT: default Cosmic Unicorn "picofonts" bitmap fonts, and on the RIGHT: new fonts available via this bitfonts library
![bitfonts-vs-default](https://github.com/kfarr/cosmic-unicorn-playground/assets/470477/a26af2e1-f391-4e9a-975b-d894382b81e0)

### Usage Example
1. Upload `bitfonts.py` file to the Pico W
2. Import in your MicroPython .py project as follows (only import fonts you need for your project)
```
from bitfonts import BitFont, font2x5, font3x5, font4x5, font5x9
```

3. Then, initialise the `bitfont` Class immediately after you initialize `PicoGraphics`:
```
# INITIALISE GALACTIC UNICORN
cu = CosmicUnicorn()
graphics = PicoGraphics(DISPLAY)
bitfont = BitFont(graphics)
```

4. Finally, use the draw_text method to draw the font
```
bitfont.draw_text("my text string",0,16,font3x5)
```

See [this demo project custom_font.py](https://github.com/kfarr/cosmic-unicorn-playground/blob/main/custom_font.py) for an example of a working demo of the custom fonts used on the Cosmic Unicorn.

### Method variables

Function `draw_text` accepts a `str` of the text to be displayed, an `int` of the `x` position (where 0 = leftmost), an `int` of the `y` position (where 0 = topmost), and a `dict` font array as defined in `bitfonts.py` file [such as this 2x5 font](https://github.com/kfarr/cosmic-unicorn-playground/blob/main/bitfonts.py#L37). 

### ⚠️ WARNING - only numbers 0-9 are supported across all fonts

ONLY `0 1 2 3 4 5 6 7 8 9` characters are supported across all fonts. Some fonts include all alphanumeric characters. Some fonts include delimiters and limited emojis.

When using in your project, first refer to [the source code to see which characaters are supported](https://github.com/kfarr/cosmic-unicorn-playground/blob/main/bitfonts.py#L31). It is very easy to add your own characters. Then, please contribute them back to this repo! :)

### Credits
* Thanks to https://github.com/NiVZ78/galactic_unicorn_custom_font for improved bitmap font parser and definition format
* Thanks to https://github.com/leswright1977/picofont for 5x9 custom bitmap font example
* This repo is originally forked from Pimoroni's [Cosmic Unicorn MicroPython Examples](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/cosmic_unicorn)

## Ok to Wake Train Clock

To be written. See twitter for now: https://twitter.com/kfarr/status/1663203677828694022 and this file: https://github.com/kfarr/cosmic-unicorn-playground/blob/main/train_clock.py

===
Original readme:

- [About Cosmic Unicorn](#about-cosmic-unicorn)
- [Cosmic Unicorn and PicoGraphics](#cosmic-unicorn-and-picographics)
- [Examples](#examples)
  - [Clock](#clock)
  - [Eighties Super Computer](#eighties-super-computer)
  - [Feature Test](#feature-test)
  - [Feature Test With Audio](#feature-test-with-audio)
  - [Fire Effect](#fire-effect)
  - [Lava Lamp](#lava-lamp)
  - [Nostalgia Prompt](#nostalgia-prompt)
  - [Rainbow](#rainbow)
  - [Scrolling Text](#scrolling-text)
  - [Today](#today)
- [Wireless Examples](#wireless-examples)
  - [Cheerlights History](#cheerlights-history)
  - [Cosmic Paint](#cosmic-paint)
  - [Exchange Ticker](#exchange-ticker)
  - [HTTP Text](#http-text)
  - [Weather](#weather)
- [NumPy examples](#numpy-examples)
- [Other Examples](#other-examples)
  - [Launch (Demo Reel)](#launch-demo-reel)
- [Other Resources](#other-resources)

## About Cosmic Unicorn

Cosmic Unicorn offers 32x32 bright RGB LEDs driven by Pico W's PIO in addition to a 1W amplifier + speaker, a collection of system and user buttons, and two Qw/ST connectors for adding external sensors and devices. Woha!

- :link: [Cosmic Unicorn store page](https://shop.pimoroni.com/products/cosmic-unicorn)

Cosmic Unicorn ships with MicroPython firmware pre-loaded, but you can download the most recent version at the link below (you'll want the  `cosmic-unicorn` image).

- [MicroPython releases](https://github.com/pimoroni/pimoroni-pico/releases)
- [Installing MicroPython](../../../setting-up-micropython.md)

## Cosmic Unicorn and PicoGraphics

The easiest way to start displaying cool stuff on Cosmic Unicorn is using our Cosmic Unicorn module (which contains a bunch of helpful functions for interacting with the buttons, adjusting brightness and suchlike) and our PicoGraphics library, which is chock full of useful functions for drawing on the LED matrix.

- [Cosmic Unicorn function reference](../../modules/cosmic_unicorn/README.md)
- [PicoGraphics function reference](../../modules/picographics/README.md)

## Examples

### Clock

[clock.py](clock.py)

Clock example with (optional) NTP synchronization. You can adjust the brightness with LUX + and -, and resync the time by pressing A.

### Eighties Super Computer

[eighties_super_computer.py](eighties_super_computer.py)

Random LEDs blink on and off mimicing the look of a movie super computer doing its work in the eighties. You can adjust the brightness with LUX + and -.

### Feature Test

[feature_test.py](feature_test.py)

Displays some text, gradients and colours and demonstrates button use. You can adjust the brightness with LUX + and -.

### Feature Test With Audio

[feature_test_with_audio.py](feature_test_with_audio.py)

Displays some text, gradients and colours and demonstrates button use. Also demonstrates some of the audio / synth features.
- Button A plays a synth tune
- Button B plays a solo channel of the synth tune
- Button C plays a sinewave (it's frequency can be adjusted with VOL + and -)
- Button D plays a second sinewave (it's frequency can be adjusted with LUX + and -)
- Sleep button stops the sounds

### Fire Effect

[fire_effect.py](fire_effect.py)

A pretty, procedural fire effect. Switch between landscape fire and vertical fire using the A and B buttons! You can adjust the brightness with LUX + and -.

### Lava Lamp

[lava_lamp.py](lava_lamp.py)

A 70s-tastic, procedural rainbow lava lamp. You can adjust the brightness with LUX + and -.

### Nostalgia Prompt

[nostalgia_prompt.py](nostalgia_prompt.py)

A collection of copies of classic terminal styles including C64, MS-DOS, Spectrum, and more. Images and text are drawn pixel by pixel from a pattern of Os and Xs. You can adjust the brightness with LUX + and -.

### Rainbow

[rainbow.py](rainbow.py)

Some good old fashioned rainbows! You can adjust the cycling speed with A and B, stripe width with C and D, hue with VOL + and -, and the brightness with LUX + and -. The sleep button stops the animation (can be started again with A or B).

### Scrolling Text

[scrolling_text.py](scrolling_text.py)

Display scrolling wisdom, quotes or greetz. You can adjust the brightness with LUX + and -.

### Today

[today.py](today.py)

Calendar example with (optional) NTP synchronization. You can adjust the brightness with LUX + and -, and resync the date by pressing C.

## Wireless Examples

These examples need `WIFI_CONFIG.py` and `network_manager.py` (from the `common` directory) to be saved to your Pico W. Open up `WIFI_CONFIG.py` in Thonny to add your wifi details (and save it when you're done).

- [micropython/examples/common](../../examples/common)

### Cheerlights History

[cheerlights_history.py](cheerlights_history.py)

Updates one pixel every two minutes to display the most recent #Cheerlights colour. Discover the most popular colours over time, or use it as an avant garde (but colourful) 32 hour clock! Find out more about the Cheerlights API at https://cheerlights.com/

You can adjust the brightness with LUX + and -.

### Cosmic Paint

[cosmic_paint](cosmic_paint)

Draw on your Cosmic Unicorn from another device in real time, over wifi!

This example needs the `micropython-phew` and `microdot` libraries (you can install these using Thonny's 'Tools > Manage Packages').

### Exchange Ticker

[exchange_ticker.py](exchange_ticker.py)

This example uses the Coinbase open API to collect the current exchange rates of various cryptocurrencies.

Press A to change to a different base exchange currency.

### HTTP Text

[http_text](http_text)

Display scrolling wisdom, quotes or greetz... from another computer or device!

You can adjust the brightness with LUX + and -.

Requires `logging.mpy` and `tinyweb` from [micropython/examples/common](../../examples/common) - copy these into the `lib` folder on your Pico W. You'll also need `index.html` to be saved alongside `html_text.py`.

### Weather

[weather](weather)

Display current weather data from the [Open-Meteo](https://open-meteo.com/) weather API.

## NumPy examples

[numpy](numpy)

The examples in the folder use `numpy`-like array functions contained in the `ulab` library for super fast graphical effects.

## Other Examples

### Launch (Demo Reel)

[launch](launch)

If you want to get the demo reel that Cosmic Unicorn ships with back, copy the contents of this `launch` folder to your Pico W.

## Other Resources

Here are some cool Cosmic Unicorn community projects and resources that you might find useful / inspirational! Note that code at the links below has not been tested by us and we're not able to offer support with it.

- :link: [Green Energy Display with Cosmic Unicorn](https://www.hackster.io/andreas-motzek/clock-and-green-energy-display-with-cosmic-unicorn-641dcb)
