def isPalindrome(s) :
    return s==s[::-1]
s="malayalam"
ans=isPalindrome(s)
if ans:
  print("palindrome no.")
else:
  print("not a palindrome no.")