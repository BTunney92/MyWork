#Program to divide a number by another
#Author: Brendan Tunney

x = int(input ("Enter First Number: "))
y = int(input ("Enter Second Number: "))

#To get integer division
answer = int(x/y) 
#To get division with remainder
remainder = x%y 

print ("{} divided by {} is {} with remainder {} ". format (x, y , answer, remainder))



print ()