# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
def count_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    sentence_lower = sentence.lower()
    vowel_count = 0
    for char in sentence_lower:
        if char in vowels:
            vowel_count += 1
    return vowel_count
def main():
    sentence = input("Enter a sentence: ")
    num_vowels = count_vowels(sentence)
    print("Number of vowels in the sentence:", num_vowels)
if __name__ == "__main__":
    main()