"""
TRUE/FALSE:
1.  F      [double OR single quotes]
2.  T
3.  F      [can contain newline characters (multi-line)]
4.  T
5.  T
6.  T
7.  T      [<string>.split(<sep>) breaks <string> into a <list> of substrings separated by <sep>.
           <sep>.join(<list>) combines all substrings in <list> into a single string separated by
           <sep>. Overall, <sep>.join(<string>.split(<sep>)) gives us back <string>.
8.  F      [Substitution ciphers aren't difficult to decode]
9.  F      [append method]
10. F      ["opening" the file]

MCQ:
1.  d
2.  c
3.  a
4.  c
5.  c
6.  d
7.  d
8.  c
9.  c
10. a
-------------
Discussion:
2.  
a)  s2[:2].upper()
b)  s2+s1+s2
c)  (((s1+' '+s2).ljust(10))*3).rstrip().title()  [probably more elegant ways to get the same output]
d)  s1
e)  s1.split('a')
f)  s1[:2]+s1[3]
"""
# Programming exercises

# 1. Original dateconvert2:
def main():
  dateStr = input("Enter a date (mm/dd/yyyy): ")
  monthStr, dayStr, yearStr = dateStr.split("/")
  months = ["January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"]
  monthStr = months[int(monthStr)-1]
  print("The converted date is:", monthStr, dayStr + ",", yearStr)
main()

# Modified program:
def main():
  dateStr = input("Enter a date (mm/dd/yyyy): ")
  monthStr, dayStr, yearStr = dateStr.split("/")
  months = ["January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"]
  monthStr = months[int(monthStr)-1]
  print("The converted date is: {:} {:}, {:}".format(monthStr, dayStr, yearStr))
main()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 2. A certain CS professor gives 5-point quizzes that are graded on the scale
#    5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as
#    an input and prints out the corresponding grade

grades = ['A', 'B', 'C', 'D', 'F', 'F']
print("Grade: ", grades[5 - max(0, min(5, int(input("Quiz score: "))))])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3. A certain CS professor gives 100-point exams that are graded on the scale
#    90-100:A, 80-89:B, 70-79:C, 60:69:D, <60:F. Write a program that accepts an
#    exam score as input and prints out the corresponding grade.

grades = ['A', 'B', 'C', 'D', 'F']
score = float(input("Exam score: "))
idx = min(4, max(0, int((99 - score)/10)))
print("Grade:", grades[idx])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 4. Write a program that allows the user to type in a phrase and then outputs
#    the acronum for that phrase. Note: The acronym should be all uppercase

phrase = input("Enter a phrase: ")
initials = []
for word in phrase.split():
  initials.append(word[0])
print("Acronym:", ("".join(initials)).upper())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 5. The value of a name is determined by summing up the values of the letters of
#    "a" is 1, "b" is 2, "c" is 3, up to "z" being 26. Write a program that
#    calculates the numeric value of a single name provided as input.

name = (input("Enter a name: ").replace(" ", "")).upper()
numval = 0
for ch in name:
  numval += ord(ch) - 64
print("Numeric value:", numval)

# 6. (Same solution as above)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 7 and 8. A Caesar cipher is a simple substitution cipher based on the idea of shifting
#    each letter of the plaintext message a fixed number (called the key) of positions
#    in the alphabet. Write a program that can encode and decode Caesar ciphers.

def main(string, key):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
  alphabetEnc = []
  for letter in alphabet:
    alphabetEnc.append(letter)
    
  for letter in alphabet:
    alphabetEnc[(alphabet.find(letter) - key)%len(alphabet)] = letter
  
  listEnc = []
  for ch in string:
    listEnc.append(alphabetEnc[alphabet.find(ch)])
    
  return("".join(listEnc))
  
print(main(input("String to encode: "), int(input("Key: "))))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 9. Write a program that counts the number of words in a sentence entered by
#    the user.

print("No. of words in sentence: ", len(input("Enter a sentence: ").split()))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 10. Write a program that calculates the avg. word length in a sentence
#     entered by the user.

sentence = input("Enter a sentence: ")
totalLetters = 0
for word in sentence.split():
  totalLetters += len(word)
print("Avg. word length:", totalLetters/len(sentence.split()))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 11. Write an improved version of the chaos.py program from Chapter 1 that allows
#     a user to input two initial values and the number of iterations, and then
#     prints a nicely formatted table showing how the values change over time.

x1 = float(input("Enter the first initial value: "))
x2 = float(input("Enter the second initial value: "))

print("{:5}{:^12.2f}{:" ">9.2f}".format("index", x1, x2))
print("-"*28)

for i in range(10):
  x1 = 3.9*x1*(1-x1)
  x2 = 3.9*x2*(1-x2)
  print("{:^5}{:^12.6f}{:" ">11.6f}".format(i+1, x1, x2))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 12. Write an improved version of the fulval.py program from Chapter 2. Your
#     program will prompt the user for the amount of the investment, the
#     annualized interest rate, and the numbers of years of the investment.
#     The program will then output a nicely formatted table that tracks the
#     value of the investment year by year.

principal = float(input("Invested amount: "))
rate = float(input("Rate of interest: "))
n = int(input("Time horizon: "))

print("\n{:^6}{:^9}".format("Year", "Value"))
print("-"*15)

for i in range(n+1):
  print("{:^6}${:>8.2f}".format(i, principal*(1+rate)**i))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 13. Redo any of the previous programming problems to make them batch-oriented.

infile = open(input("Input file: "), "r")
outfile = open(input("Output file: "), "w")
key = int(input("Key: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
alphabetEnc = []
for letter in alphabet:
  alphabetEnc.append(letter)
    
for letter in alphabet:
  alphabetEnc[(alphabet.find(letter) - key)%len(alphabet)] = letter
              
"""
This section is only to differentiate the last line from the rest
All lines except the last one have a '\n' character at the end,
which must be ignored.
"""          
# Begin Section    
listTemp = []
for line in infile:
  listTemp.append(line)
  print(line)
i = 0
for item in listTemp[:-1]:
  listTemp[i] = item[:-1]
  i += 1
print(listTemp)
# End Section

for line in listTemp[:-1]:
  listEnc = []
  for ch in line:
    listEnc.append(alphabetEnc[alphabet.find(ch)])
  print("".join(listEnc), file = outfile)

# This section has to be included separately since
# the last line needs to be printed without '\n' at
# its end.
listEnc = []
for ch in listTemp[-1]:
  listEnc.append(alphabetEnc[alphabet.find(ch)])
print("".join(listEnc), file = outfile, end="")

infile.close()
outfile.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 14. Write a program that accepts a file name as input and then
#     prints three numbers showing the count of lines, words and
#     characters in the file.

infile = open(input("Input file: "), "r")
lines = infile.readlines()
print("No. of lines =", len(lines))
words = chars = 0
for line in lines:
  for word in line.split():
    words += 1
    for char in word:
      chars += 1

print("No. of words = {:}\nNo. of chars = {:}".format(words, chars))
infile.close()
