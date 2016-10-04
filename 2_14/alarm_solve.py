#!/usr/bin/env python3
time = int(input("What time is it? "))
alarm = int(input("When do you want your alarm to go of?"))

while alarm >= 24:
	alarm = alarm - 24

a = time + alarm
if a >= 24:
	a = a - 12
print(a)
