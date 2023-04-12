# Ask the user for a string and print out whether this string is a palindrome or not.

word = input("Enter a word: ")

half_mark = len(word)//2
end_mark = len(word)
first_half = word[0:half_mark]
last_half = word[end_mark:half_mark-1:-1]

if first_half == last_half:
    print(f"{word} is a palindrome.")
elif first_half != last_half:
    print(f"Sorry, {word} is not a palindrome.")
