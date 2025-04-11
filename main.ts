input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("" + targetID + ":FEED")
    basic.showString("F")
    basic.pause(500)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("" + targetID + ":LOVE")
    basic.showIcon(IconNames.Heart)
    basic.pause(500)
    basic.clearScreen()
})
let targetID = ""
targetID = "S1"
radio.setGroup(23)
