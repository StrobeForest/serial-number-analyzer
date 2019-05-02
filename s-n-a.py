name = input("What is your name? ")
proper_input = False
while proper_input == False:
    print("Hello " + name + "!")
    print("I will take in your bills serial number, and tell you all about it.")
    print("I am only able to analyze the serial numbers on $1 bills due to the higher denominations being of a different format.")
    print("The serial number can be found twice on the front of the dollar bill written in green.")
    print("It appears once on either side of Washington, and is 8 digits with a letter at the beginning and the end for 10 digits in all.")
    print("Some examples of $1 serial numbers are: B03542754F, L01986303*, F03779718I, and C81230251D")
    print("Please submit your bill's serial number below in the format found in the examples above.")
    serial = input("---> ")

# Redirecting errors in code to reset
    if len(serial) != 10:
        print("The Total Number of Characters Did Not Pass. Please Try Submitting Again.")
        continue
    if serial[0] not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]:
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
    if serial[9] not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "*"]:
        print("Tenth Character Did Not Pass. Please Try Submitting Again.")
    else:
        print("")
        proper_input = True


# Storing numbers as variables now that they have passed
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

# 1 Identifying which Federal Reserve Bank the bill is from using the first letter
print("The first letter of a serial number (A-L) signifies which of the 12 Federal Reserve Bank locations in the U.S. the bill was printed in.")
FirstLetterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
FRBNumList = ["Boston", "New York", "Philadelphia", "Cleveland", "Richmond", "Atlanta", "Chicago", "St. Louis", "Minneapolis", "Kansas City", "Dallas", "San Francisco"]
Location = (FirstLetterList.index(FirstLetter))
FRBNum = (FRBNumList[Location])
print("Your bill was printed in the " + FRBNum + " Federal Reserve Bank.")
print("")

# 2 Identifying which block the bill was printed on
print("The last letter of a serial number signifies which block the bill was printed on.")
print("The last letter is A-Y, without a O because it looks like 0 and without Z because it's reserved for test printings.")
print("Every time a run from 00000001 to 99999999 is completed, the block is changed, and the last letter goes up by one.")
print("When a bill is damaged during the printing process, a new set of bills is printed to make up for the lost ones.")
print("These new bills have a * (star) as the final letter in the Serial Number, rather than one of the letters defined above.")
if LastLetter == "*":
    print("Your bill is a star note. It's the rarest final character of the bill but doesn't necessarily make it valuable.")
    print("It was printed on it's own set due to a production error with the original run.")
    print("")
else:
    LastLetterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
    BlockNumList = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "twenty-first", "twenty-second", "twenty-third", "twenty-fourth"]
    Location = (LastLetterList.index(LastLetter))
    BlockNum = (BlockNumList[Location])
    print("Your bill was printed on the " + BlockNum + " block.")
    print("")

# Calculating how many of each number there is in the serial number
AllNumbers = [FirstNumber, SecondNumber, ThirdNumber, FourthNumber, FifthNumber, SixthNumber, SeventhNumber, EighthNumber]

# 3 Tell what percentage of the way through the run the bill was
print("Your bill was printed about " + str(AllNumbers[0]) + str(AllNumbers[1]) + "." + str(AllNumbers[2]) + str(AllNumbers[3]) + "% of the way through the run.")
print("")

# 4 Tell how many different numbers are present and list them
Zeros = 0
Ones = 0
Twos = 0
Threes = 0
Fours = 0
Fives = 0
Sixes = 0
Sevens = 0
Eights = 0
Nines = 0

for i in AllNumbers:
    if i == 0:
        Zeros = Zeros + 1
    if i == 1:
        Ones = Ones + 1
    if i == 2:
        Twos = Twos + 1
    if i == 3:
        Threes = Threes + 1
    if i == 4:
        Fours = Fours + 1
    if i == 5:
        Fives = Fives + 1
    if i == 6:
        Sixes = Sixes + 1
    if i == 7:
        Sevens = Sevens + 1
    if i == 8:
        Eights = Eights + 1
    if i == 9:
        Nines = Nines + 1

PresentNumbers = []
AppearNumbers = 0
CheckList = [Zeros, Ones, Twos, Threes, Fours, Fives, Sixes, Sevens, Eights, Nines]
if Zeros > 0:
    PresentNumbers.append("zero")
    AppearNumbers = AppearNumbers + 1
if Ones > 0:
    PresentNumbers.append("one")
    AppearNumbers = AppearNumbers + 1
if Twos > 0:
    PresentNumbers.append("two")
    AppearNumbers = AppearNumbers + 1
if Threes > 0:
    PresentNumbers.append("three")
    AppearNumbers = AppearNumbers + 1
if Fours > 0:
    PresentNumbers.append("four")
    AppearNumbers = AppearNumbers + 1
if Fives > 0:
    PresentNumbers.append("five")
    AppearNumbers = AppearNumbers + 1
if Sixes > 0:
    PresentNumbers.append("six")
    AppearNumbers = AppearNumbers + 1
if Sevens > 0:
    PresentNumbers.append("seven")
    AppearNumbers = AppearNumbers + 1
if Eights > 0:
    PresentNumbers.append("eight")
    AppearNumbers = AppearNumbers + 1
if Nines > 0:
    PresentNumbers.append("nine")
    AppearNumbers = AppearNumbers + 1

if AppearNumbers == 1:
    print("One digit appears in your serial number. That digit is " + PresentNumbers[0] + ".")
elif AppearNumbers == 2:
    print("Two digits appears in your serial number. Those digits are " + PresentNumbers[0] + " and " + PresentNumbers[1] + ".")
elif AppearNumbers == 3:
    print("Three digits appears in your serial number. Those digits are " + PresentNumbers[0] + ", " + PresentNumbers[1] + " and " + PresentNumbers[2] + ".")
elif AppearNumbers == 4:
    print("Four digits appears in your serial number. Those digits are " + PresentNumbers[0] + ", " + PresentNumbers[1] + ", " + PresentNumbers[2] + " and " + PresentNumbers[3] + ".")
elif AppearNumbers == 5:
    print("Five digits appears in your serial number. Those digits are " + PresentNumbers[0] + ", " + PresentNumbers[1] + ", " + PresentNumbers[2] + ", " + PresentNumbers[3] + " and " + PresentNumbers[4] + ".")
elif AppearNumbers == 6:
    print("Six digits appears in your serial number. Those digits are " + PresentNumbers[0] + ", " + PresentNumbers[1] + ", " + PresentNumbers[2] + ", " + PresentNumbers[3] + ", " + PresentNumbers[4] + " and " + PresentNumbers[5] + ".")
elif AppearNumbers == 7:
    print("Seven digits appears in your serial number. Those digits are " + PresentNumbers[0] + ", " + PresentNumbers[1] + ", " + PresentNumbers[2] + ", " + PresentNumbers[3] + ", " + PresentNumbers[4] + ", " + PresentNumbers[5] + " and " + PresentNumbers[6] + ".")
elif AppearNumbers == 8:
    print("Eight digits appears in your serial number. Those digits are " + PresentNumbers[0] + ", " + PresentNumbers[1] + ", " + PresentNumbers[2] + ", " + PresentNumbers[3] + ", " + PresentNumbers[4] + ", " + PresentNumbers[5] + ", " + PresentNumbers[6] + " and " + PresentNumbers[7] + ".")
print("")

# 5 Adding up the total of all the digits in the serial number
Total = 0
for i in AllNumbers:
    Total = Total + i

print("The total sum of the eight digits in the serial number is " + str(Total) + ".")
print("")

# 6 Finding out the maximum number(s) in the serial number
NumberAppearances = [Zeros, Ones, Twos, Threes, Fours, Fives, Sixes, Sevens, Eights, Nines]

Maximums = []

MaxNums = 0

Max = max(NumberAppearances)

if Zeros == Max:
    Maximums.append("Zero")
    MaxNums = MaxNums + 1
if Ones == Max:
    Maximums.append("One")
    MaxNums = MaxNums + 1
if Twos == Max:
    Maximums.append("Two")
    MaxNums = MaxNums + 1
if Threes == Max:
    Maximums.append("Three")
    MaxNums = MaxNums + 1
if Fours == Max:
    Maximums.append("Four")
    MaxNums = MaxNums + 1
if Fives == Max:
    Maximums.append("Five")
    MaxNums = MaxNums + 1
if Sixes == Max:
    Maximums.append("Six")
    MaxNums = MaxNums + 1
if Sevens == Max:
    Maximums.append("Seven")
    MaxNums = MaxNums + 1
if Eights == Max:
    Maximums.append("Eight")
    MaxNums = MaxNums + 1
if Nines == Max:
    Maximums.append("Nine")
    MaxNums = MaxNums + 1

if MaxNums == 1:
    print(Maximums[0] + " is the maximum in the serial number. It appears", Max, "times.")
elif MaxNums == 2:
    print(Maximums[0] + " and " + Maximums[1] + " are the maximums in the serial number. They both appear", Max, "times.")
elif MaxNums == 3:
    print(Maximums[0] + ", " + Maximums[1] + " and " + Maximums[2] + " are the maximums in the serial number. Each of them appears", Max, "times.")
elif MaxNums == 4:
    print(Maximums[0] + ", " + Maximums[1] + ", " + Maximums[2] + " and " + Maximums[3] + " are the maximums in the serial number. Each of them appears", Max, "times.")
else:
    print("No number appears more than once in your serial number.")
print("")

# Tests to see if a bill is solid
if AppearNumbers == 1:
    print("Your bill's serial number is a solid. These only appear once every 11 million bills. It is very rare.")
    print("")
else:

    # Tests to see if the serial number is a radar
    if FirstNumber == EighthNumber and SecondNumber == SeventhNumber and ThirdNumber == SixthNumber and FourthNumber == FifthNumber:
        print("Your bill's serial number is a radar. That is a rare form of bill.")
        print("")

    # Tests to see if the bill is very close to the beginning or the end of the run
    if FirstNumber == 0 and SecondNumber == 0 and ThirdNumber == 0 and FourthNumber == 0 and FifthNumber == 0:
        print("Your bill is very close to the beginning of the run. The lower the number, the higher it's value.")
        print("")

    if FirstNumber == 9 and SecondNumber == 9 and ThirdNumber == 9 and FourthNumber == 9 and FifthNumber == 9:
        print("Your bill is very close to the end of the run. The higher the number, the higher it's value.")
        print("")

    # Tests if a bill is a bookend or not
    if FirstNumber == SixthNumber and SecondNumber == SeventhNumber and ThirdNumber == EighthNumber:
        print("Your bill's serial number is a bookend. That is a rare form of bill.")
        print("")

    # Tests to see if the bill is a repeater
    if FirstNumber == FifthNumber and SecondNumber == SixthNumber and ThirdNumber == SeventhNumber and FourthNumber == EighthNumber:
        print("Your bill's serial number is a repeater. This is a rare form of bill.")

    # Tests to see if the bill is a ladder
    if SecondNumber == FirstNumber + 1 and ThirdNumber == SecondNumber + 1 and FourthNumber == ThirdNumber + 1 and FifthNumber == FourthNumber + 1 and SixthNumber == FifthNumber + 1 and SeventhNumber == SixthNumber + 1 and EighthNumber == SeventhNumber + 1:
        print("Your bill's serial number is a ladder. Ladder serial numbers only appear 3 times in an entire run. So they go for a lot of money. It is the rarest sought after serial number (aside from very specific numbers).")

    if SecondNumber == FirstNumber - 1 and ThirdNumber == SecondNumber - 1 and FourthNumber == ThirdNumber - 1 and FifthNumber == FourthNumber - 1 and SixthNumber == FifthNumber - 1 and SeventhNumber == SixthNumber - 1 and EighthNumber == SeventhNumber - 1:
        print("Your bill's serial number is a reverse ladder. Reverse ladder serial numbers only appear 3 times in an entire run. So they go for a lot of money.")


    # Tests to see if the bill is a binary or trinary bill
    if AppearNumbers == 2:
        print("Your bill's serial number is a binary. The numbers " + PresentNumbers[0] + " and " + PresentNumbers[1] + " are the only numbers that appear in it.")

    if AppearNumbers == 3:
        print("Your bill's serial number is a trinary. The numbers " + PresentNumbers[0] + ", " + PresentNumbers[1] + " and " + PresentNumbers[2] + " are the only numbers that appear in it.")

print("")
print("Thanks for using my bill serial number analyzer!")

