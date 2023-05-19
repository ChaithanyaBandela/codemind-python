def longest_vowel_substring(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_length = 0
    current_length = 0
    for char in s:
        if char in vowels:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length

# Example usage
string =input()
result = longest_vowel_substring(string)
print(result)
