

def palindrome():
    original_word = input("Enter a word: ")

    palindrome_word = ""
    for index in range(0, len(original_word)):
        print(original_word[index])

    for index in range(len(original_word)-1, -1, -1):
        palindrome_word = palindrome_word + original_word[index]
        print(palindrome_word)

    if palindrome_word == original_word:
        print("palindrome")
    else:
        print("Not a palindrome.")


palindrome()
