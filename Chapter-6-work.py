def is_leap(year):
    # your code here
    leap = False
    # Write your logic here

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap
def main():
    year = int(input("enter year"))
    print (is_leap(year))

if __name__ == "__main__":
    main()


# Below is a set of tests so you can check if your code is correct.
# Do not copy this part into Vocareum.
from test import testEqual

#testEqual(is_leap(1944), True)
#testEqual(is_leap(2011), False)
#testEqual(is_leap(1986), False)
#testEqual(is_leap(1956), True)
#testEqual(is_leap(1957), False)
#testEqual(is_leap(1800), False)
#testEqual(is_leap(1900), False)
#testEqual(is_leap(1600), True)
#testEqual(is_leap(2056), True)
