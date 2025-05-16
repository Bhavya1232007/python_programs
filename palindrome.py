def isPalindrome(s):
    return s==s[::-1]
s=input("enter a string: ")
if(len(s)>1):
    ans=isPalindrome(s)
    if(ans):
        print("yes")
    else:
        print("no")
else:
    print("Please enter a string")