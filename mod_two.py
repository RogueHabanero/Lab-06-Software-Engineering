#Name: Ryan Dominguez
#Date 10/22/2022
#Assignment: Lab 06

def modify_two(a, b):
    return a + b

def main():
    a = int(input())
    b = int(input())

    summation = modify_two(a, b)

    print(f"The sum of {a} and {b} is: {summation}")

if __name__ == "__main__":
    main()
