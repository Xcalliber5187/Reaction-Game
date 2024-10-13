def on_pin_pressed_p0():
    global running, False_start, start
    serial.write_number(1)
    basic.show_number(3)
    basic.show_number(2)
    basic.show_number(1)
    basic.clear_screen()
    running = False
    False_start = False
    basic.pause(1000 + randint(0, 4000))
    if not (False_start):
        start = input.running_time()
        running = True
        led.stop_animation()
        basic.clear_screen()
        led.plot(randint(0, 4), randint(0, 4))
        serial.write_number(2)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p2():
    global Pin2, running, end
    if running:
        Pin2 = True
        running = False
        end = input.running_time()
        basic.show_leds("""
            . . . # #
            . . . # #
            . . . # #
            . . . # #
            . . . # #
            """)
        serial.write_number(3)
        basic.pause(100)
        serial.write_number(end - start)
        basic.show_number(end - start)
    else:
        if Pin2 == False:
            Pin2 = True
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    global Pin1, running, end, Pin2
    if running:
        Pin1 = True
        running = False
        end = input.running_time()
        basic.show_leds("""
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            # # . . .
            """)
        serial.write_number(4)
        basic.pause(1000)
        basic.show_number(end - start)
        serial.write_number(end - start)
    else:
        if Pin1 == False:
            Pin2 = True
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

start = 0
end = 0
False_start = False
running = False
Pin2 = False
Pin1 = False
Pin1 = False
Pin2 = False
running = False
False_start = False
end = 0

def on_forever():
    if False_start == True:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        serial.write_number(0)
basic.forever(on_forever)
