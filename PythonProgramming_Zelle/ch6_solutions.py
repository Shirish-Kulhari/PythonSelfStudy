"""
TRUE/FALSE:
1.  F
2.  F
3.  T
4.  T
5.  F
6.  F
7.  F   ["In some cases, functions can also communicate back to the 
          calling program by making changes to the function parameters.
8.  T
9.  T
10. F

MCQ:
1.  b
2.  a
3.  a
4.  b
5.  d
6.  a
7.  d
8.  a
9.  d
10. a
-------------
Discussion:
4. (c) Because answer defined in the cube function and answer declared in
       program body are two different variables. Let's call the former
       answer1 and the latter answer2 for convenience. The value 3 gets
       passed to cube, 27 is assigned to answer1 and the value 27 is
       returned back to the result variable. As soon as the cube function
       ends, answer1 variable is out of the picture. answer2 has been
       independent the entire time and will retain its value.
"""
# Programming exercises

# 1. Write a program to print the lyrics of the song "Old MacDonald." Your
#    program should print the lyrics for five different animals, similar to
#    the example verse below.
#    Old MacDonald had a farm, Ee-igh, Ei-igh, Oh!
#    And on that farm he had a cow, Ee-igh, Ee-igh, Oh!
#    With a moo, moo here and a moo, moo there.
#    Here a moo, there a moo, everywhere a moo, moo.
#    Old MacDonald had a farm, Ee-igh, Ei-igh, Oh!

exclamation = ", Ee-igh, Ee-igh, Oh!"
punchLine = "Old MacDonald had a farm" + exclamation
def verse(animal, sound):
  doubles = sound + ", " + sound
  print(punchLine)
  print("And on that farm he had a(n)", animal + exclamation)
  print("With a " + doubles + " here and a " + doubles + " there.")
  print("Here a " + sound + ", there a " + sound + ", everywhere a " + doubles + ".")
  print(punchLine + "\n\n")
  
verse("cow", "moo")
verse("owl", "hoot")
verse("Peek", "yee")
verse("cat", "meow")
verse("car", "vroom")

# ~~~~~~~~~~~~~~~~~~~~~~~~

# 2. Too tedious
# 3. Write definitions for sphereArea(radius) and sphereVolume(radius), and
#    use your functions to solve Programming Exercise 1 from Chapter 3.

import math

def sphereArea(radius):
  return 4*math.pi*(radius**2)
def sphereVolume(radius):
  return 4*math.pi*(radius**3)/3

def main(r):
  print("Area: ", sphereArea(r), "\nVolume: ", sphereVolume(r), sep = "")
  
main(float(input("Radius: ")))

# ~~~~~~~~~~~~~~~~~~~~~~~~~

# 4. Write definitions for the following two functions:
#    sumN(n) returns the sum of the first n natural numbers
#    sumNCubes(n) returns the sum of the cubes of the first n natural numbers
#    Then use these functions in a program that prompts a user for an n and
#    prints out the sum of the first n natural numbers and the sum of the
#    cubes of the first n natural numbers.

def sumN(n):
  sum = 0
  for i in range(n):
    sum += i + 1
  return sum

def sumNCubes(n):
  sum = 0
  for i in range(n):
    sum += (i + 1)**3
  return sum

def main(n):
  print("Sum of first n numbers: ", sumN(n),
        "\nSum of first n cubes: ", sumNCubes(n), sep = "")
  
main(int(input("Enter a natural number: ")))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# 5 and 6. Boring
# 7. Write a function to compute the nth Fibonacci number.

def fib(n):
  seq = [1, 1]
  for i in range(2, n):
    seq.append(seq[i-2] + seq[i-1])
  return seq[-1]
  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# 8. Solve Programming Exercise 17 from Chapter 3 using a function
#    nextGuess(guess, x) that returns the next guess

def nextGuess(guess, x):
  return (guess + (x/guess))/2

iterations = int(input("No. of iterations: "))
x = float(input("Number input: "))
latestGuess = x/2
for i in range(iterations):
  latestGuess = nextGuess(latestGuess, x)
  
print("Square root:", latestGuess)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~

# 9 and 10. Simple enough to implement as a function. Ref. relevant
#    answers from ch5_solutions.py

# 11. Write and test a function to meet this specification.
#     squareEach(nums)  nums is a list of numbers. Modifies the list
#     by squaring each entry.

numList = [1, 2, 3, 4]

def squareEach(nums):
  i = 0
  for num in nums:
    nums[i] = num**2
    i += 1
    
squareEach(numList)
print(numList)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 12. Write and test a function to meet this specification.
#     sumList(nums)  nums is a list of numbers. Returns the sum of
#     the numbers in the list.

numList = [1, 2, 13, 24, 71]

def sumList(nums):
  sum = 0
  for num in nums:
    sum += num
  return sum
    
print(sumList(numList))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 13. 
