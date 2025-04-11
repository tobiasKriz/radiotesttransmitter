def on_button_pressed_a():
    radio.send_string("" + targetID + ":FEED")
    basic.show_string("F")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("" + targetID + ":LOVE")
    basic.show_icon(IconNames.HEART)
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

targetID = ""
targetID = "S1"
radio.set_group(23)