from bigbrain.hands.motor import Motor

motor = Motor()

motor.nameHand(0, 'beuford')
while True:
    motor.findHands()
