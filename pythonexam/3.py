def  isP(s):
   if   len (s)    <=  1:
      return True
   return  s[0] == s[len (s)  - 1] and isP(s[1 : len (s) - 1])

inp = input('Enter Input : ')
l = ""
for i in inp:
    if i.isalpha():
        l += i.lower()
a = "'" + inp + "'"
if   isP(l):
      print (a,"is palindrome")
else :
      print (a,"is not palindrome")