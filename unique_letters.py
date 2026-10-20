s="abcdeabcde"

unique_letters=""

for char in s:
    if char not in unique_letters:
        unique_letters += char

print(f"number of unique letters in the string is {len(unique_letters)}")
