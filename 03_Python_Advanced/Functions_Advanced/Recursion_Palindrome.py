def palindrome(word, idx):

    if idx == len(word) // 2:
        return f'{word} is palindrome'

    left = word[idx]
    right = word[-idx - 1]

    if left != right:
        return f'{word} is not palindrome'

    return palindrome(word, idx+1)

print(palindrome("abcssssba", 0))