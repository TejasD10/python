"""
The method takes in the name and age and prints
the years left for the person to reach the age of 100
"""
import datetime


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(name)
    print(age)
    print("You will be hundred years old in " + str(datetime.datetime.now().year + (100 - age)))


# Execute the main method
if __name__ == '__main__':
    main()
