#Name: Ryan Dominguez
#Date 10/22/2022
#Assignment: Lab 06

def add_two(a, b):
    return a + b

def sub_two(a, b):
    return a - b

def main():
    a = int(input())
    b = int(input())

    summation = add_two(a, b)
    print(f"The sum of {a} and {b} is: {summation}")

    subtraction = sub_two(a, b)
    print(f"The sum of {a} and {b} is: {subtraction}")

if __name__ == "__main__":
    main()
