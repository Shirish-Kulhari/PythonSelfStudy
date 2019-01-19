"""
TRUE/FALSE:
1.  T
2.  F
3.  T
4.  F
5.  T
6.  T
7.  F
8.  F
9.  T
10. F  [I'm assuming it means checking whether the user input
        is correct via a decision structure.]
        
MCQ:
1.  c
2.  c
3.  b
4.  c
5.  b
6.  c
7.  a
8.  c
9.  a
10. c
"""
# Programming Exercises

# 6. The speeding ticket fine in Podunksville is $50 plus $5 for
#    each mph over the limit plus a penalty of $200 for any speed
#    above 90 mph. Write a program that accepts a speed limit and
#    a clocked speed and either prints out a message indicating the
#    speed was legal or prints the amount of fine, if the speed is
#    legal.

limit = int(input("Speed limit (in mph, can't be more than 90): "))
clocked = int(input("Clocked speed (in mph): "))

try:
  if(limit > 90):
    print("Speed limit can't be greater than 90 mph.")
  elif(limit < 0 or clocked < 0):
    print("Speeds can't be negative.")
  elif(clocked <= limit):
    print("Clocked speed legal.")
  else:
    print("Clocked speed illegal. Your fine is: $",
          50 + 5*(clocked-limit) + 200*int(clocked > 90),
          sep = "")
except:
  print("Something went wrong.")
  
# 7. A babysitter charges $2.50 an hour until 9:00 pm when the rate
#    drops to $1.75 an hour. Write a program that accepts a starting
#    time and ending time in hours and minutes and calculates the
#    total babysitting bill. You may assume that the starting and
#    ending times are in a single 24-hour period. Partial hours should
#    be appropriately prorated.

