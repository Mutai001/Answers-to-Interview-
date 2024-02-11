# Question 5: Reverse IntegerWrite a program that takes an integer as input and returns an integer with reversed digit
# ordering.
def reverse_integer(num):
    num_str = str(num)
    if num < 0:
        reversed_num = int("-" + num_str[:0:-1])
    else:
        reversed_num = int(num_str[::-1])
    return reversed_num
def main():
    try:
        num = int(input("Enter an integer: "))
        reversed_num = reverse_integer(num)
        print("Reversed integer:", reversed_num)
    except ValueError:
        print("Invalid input! Please enter an integer.")
if __name__ == "__main__":
    main()