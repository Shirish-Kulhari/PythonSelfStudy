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
-------------
Programming exercises

1. Original dateconvert2:
def main():
  dateStr = input("Enter a date (mm/dd/yyyy): ")
  monthStr, dayStr, yearStr = dateStr.split("/")
  months = ["January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"]
  monthStr = months[int(monthStr)-1]
  print("The converted date is:", monthStr, dayStr + ",", yearStr)
main()
