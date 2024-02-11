# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
def is_power_of_two(num):
    if num <= 0:
        return False
    return (num & (num - 1)) == 0
def main():
    try:
        num = int(input("Enter an integer: "))
        if is_power_of_two(num):
            print("True")
        else:
            print("False")
    except ValueError:
        print("Invalid input! Please enter an integer.")
if __name__ == "__main__":
    main()