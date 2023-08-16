# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Months = ["Jan", "Feb"]
print (Months[-1])


for m in Months:
    print (m.upper())

print ("=" * 15)

index = 0
while index < len(Months):
    print ('Month: {}'.format(Months[index]))
    index += 1
    
