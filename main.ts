input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
    music.playMelody("C5 B A B C5 B A B ", 120)
})
input.onButtonPressed(Button.AB, function () {
	
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Sad)
    music.playMelody("C D C D E D C D ", 80)
})
input.onGesture(Gesture.Shake, function () {
	
})
