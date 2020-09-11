def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
    music.play_melody("C5 B A B C5 B A B ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
    music.play_melody("C D C D E D C D ", 80)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
