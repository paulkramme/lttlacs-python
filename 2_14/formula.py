#!/usr/bin/env python3

P = 10000 #Dollars
n = 12
r = 8
t = int(input("Input the number of years you which to calculate: "))

a = P * ((1 + (r/n))**(n*t))

print(a)
