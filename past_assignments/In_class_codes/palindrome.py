
def isPalindrome(word:str) -> bool:

    word = word.lower()

    for i in range(len(word)//2):

        if word[i] != word[len(word) - i - 1]:
            return False

    return True

print(isPalindrome("MADAM"))
print(isPalindrome("RACECAR"))
print(isPalindrome("DAVID"))
print(isPalindrome("Toot"))
