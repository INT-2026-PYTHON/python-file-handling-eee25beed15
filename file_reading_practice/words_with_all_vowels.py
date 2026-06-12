"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""
# Function to check if a word contains all vowels
def has_all_vowels(word):
    vowels = "aeiou"
    word = word.lower()

    for vowel in vowels:
        if vowel not in word:
            return False
    return True

count = 0

# Open and read file
with open("sowpods.txt", "r") as file:
    for line in file:
        word = line.strip()

        # Check for all vowels
        if has_all_vowels(word):
            print(word)
            count += 1

# Print total count
print("Total words with all vowels:", count)
