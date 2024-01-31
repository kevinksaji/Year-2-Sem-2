def isPalindrome(s):
    n = len(s)
    if n <= 1: # base case
        return True
    return s[0] == s[n-1] and isPalindrome(s[1:n-1])

for s in ['geeksforgeeks', 'malayalam']:
    print(s, 'is', 'a' if isPalindrome(s) else 'not a', 'palindrome')