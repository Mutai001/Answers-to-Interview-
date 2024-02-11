# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the
# string, and then returns the result string.
def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    result = " ".join(capitalized_words)
    return result
def main():
    sentence = input("Enter a sentence: ")
    result = capitalize_first_letter(sentence)
    print("Result:", result)
if __name__ == "__main__":
    main()