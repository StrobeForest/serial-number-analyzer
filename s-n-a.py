name = input("What is your name? ")
proper_input = False
while proper_input == False:
    print("Hello " + name + "!")
    print("I will take in your bills serial number, and tell you all about it.")
    print("I am only able to analyze the serial numbers on $1 bills due to the higher denominations being of a different format.")
    print("The serial number can be found twice on the front of the dollar bill written in green.")
    print("It appears once on either side of Washington, and is 8 digits with a letter at the beginning and the end for 10 digits in all.")
    print("Some examples of $1 serial numbers are: B03542754F, L01986303*, F03779718I, and C81230251D")
    print("Please submit your bills serial number below in the format found in the examples above.")
    serial = input("---> ")

    if len(serial) != 10:
        print("The Total Number of Characters Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[0] not in ["A", "B", "C", "D", "E", "F"]:
        print("First Character Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Second Character Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[2] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Third Character Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[3] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Fourth Character Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[4] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Fifth Character Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[5] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Sixth Character Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[6] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Seventh Character Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[7] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Eighth Character Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[8] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Ninth Character Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[9] not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
        print("Tenth Character Did Not Pass. Please Try Submitting Again.")
    else:
        proper_input = True


FirstLetter = serial[0]
FirstNumber = int(serial[1])
SecondNumber = int(serial[2])
ThirdNumber = int(serial[3])
FourthNumber = int(serial[4])
FifthNumber = int(serial[5])
SixthNumber = int(serial[6])
SeventhNumber = int(serial[7])
EighthNumber = int(serial[8])
LastLetter = serial[9]

print(FirstLetter)
print(type(FirstLetter))
print(FirstNumber)
print(type(FirstNumber))
print(SecondNumber)
print(type(SecondNumber))
print(ThirdNumber)
print(type(ThirdNumber))
print(FourthNumber)
print(type(FourthNumber))
print(FifthNumber)
print(type(FifthNumber))
print(SixthNumber)
print(type(SixthNumber))
print(SeventhNumber)
print(type(SeventhNumber))
print(EighthNumber)
print(type(EighthNumber))
print(LastLetter)
print(type(LastLetter))
#hi



