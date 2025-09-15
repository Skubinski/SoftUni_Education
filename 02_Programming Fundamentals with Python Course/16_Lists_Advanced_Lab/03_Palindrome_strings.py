def palindrome (text):
    if text == text[::-1]:
        return text




words = input().split()
palindrome_word = input()
palindrome_list = [word for word in words if palindrome(word)]
palindrome_counter = palindrome_list.count(palindrome_word)
print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")
