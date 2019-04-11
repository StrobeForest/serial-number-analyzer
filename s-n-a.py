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

#Redirecting errors in code to reset
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
        proper_input = True

#Storing numbers as variables now that they have passed
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
if FirstLetter == "A":
    print("Your bill was printed in the Boston Federal Reserve Bank.")
elif FirstLetter == "B":
    print("Your bill was printed in the New York Federal Reserve Bank.")
elif FirstLetter == "C":
    print("Your bill was printed in the Philadelphia Federal Reserve Bank.")
elif FirstLetter == "D":
    print("Your bill was printed in the Cleveland Federal Reserve Bank.")
elif FirstLetter == "E":
    print("Your bill was printed in the Richmond Federal Reserve Bank.")
elif FirstLetter == "F":
    print("Your bill was printed in the Atlanta Federal Reserve Bank.")
elif FirstLetter == "G":
    print("Your bill was printed in the Chicago Federal Reserve Bank.")
elif FirstLetter == "H":
    print("Your bill was printed in the St. Louis Federal Reserve Bank.")
elif FirstLetter == "I":
    print("Your bill was printed in the Minneapolis Federal Reserve Bank.")
elif FirstLetter == "J":
    print("Your bill was printed in the Kansas City Federal Reserve Bank.")
elif FirstLetter == "K":
    print("Your bill was printed in the Dallas Federal Reserve Bank.")
elif FirstLetter == "L":
    print("Your bill was printed in the San Francisco Federal Reserve Bank.")
print("")

# 2 Identifying which block the bill was printed on
print("The last letter of a serial number signifies which block the bill was printed on.")
print("The last letter is A-Y, without a O because it looks like 0 and without Z because it's reserved for test printings.")
print("Every time a run from 00000001 to 99999999 is completed, the block is changed, and the last letter goes up by one.")
if LastLetter == "A":
    print("Your bill was printed on the first block.")
if LastLetter == "B":
    print("Your bill was printed on the second block.")
if LastLetter == "C":
    print("Your bill was printed on the third block.")
if LastLetter == "D":
    print("Your bill was printed on the fourth block.")
if LastLetter == "E":
    print("Your bill was printed on the fifth block.")
if LastLetter == "F":
    print("Your bill was printed on the sixth block.")
if LastLetter == "G":
    print("Your bill was printed on the seventh block.")
if LastLetter == "H":
    print("Your bill was printed on the eighth block.")
if LastLetter == "I":
    print("Your bill was printed on the ninth block.")
if LastLetter == "J":
    print("Your bill was printed on the tenth block.")
if LastLetter == "K":
    print("Your bill was printed on the eleventh block.")
if LastLetter == "L":
    print("Your bill was printed on the twelfth block.")
if LastLetter == "M":
    print("Your bill was printed on the thirteenth block.")
if LastLetter == "N":
    print("Your bill was printed on the fourteenth block.")
if LastLetter == "P":
    print("Your bill was printed on the fifteenth block.")
if LastLetter == "Q":
    print("Your bill was printed on the sixteenth block.")
if LastLetter == "R":
    print("Your bill was printed on the seventeenth block.")
if LastLetter == "S":
    print("Your bill was printed on the eighteenth block.")
if LastLetter == "T":
    print("Your bill was printed on the nineteenth block.")
if LastLetter == "U":
    print("Your bill was printed on the twentieth block.")
if LastLetter == "V":
    print("Your bill was printed on the twenty-first block.")
if LastLetter == "W":
    print("Your bill was printed on the twenty-second block.")
if LastLetter == "X":
    print("Your bill was printed on the twenty-third block.")
if LastLetter == "Y":
    print("Your bill was printed on the twenty-fourth block.")
print("")

# Calculating how many of each number there is in the serial number
AllNumbers = [FirstNumber, SecondNumber, ThirdNumber, FourthNumber, FifthNumber, SixthNumber, SeventhNumber, EighthNumber]

# 3 Tell what percentage of the way through the run the bill was
print("There are 99,999,999 bills printed in a run.")
print("Your bill was printed about " + str(AllNumbers[0]) + str(AllNumbers[1]) + "." + str(AllNumbers[2]) + str(AllNumbers[3]) + "% of the way through the run.")
print("")

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

print(Zeros)
print(Ones)
print(Twos)
print(Threes)
print(Fours)
print(Fives)
print(Sixes)
print(Sevens)
print(Eights)
print(Nines)

# 6 Finding out the maximum number(s) in the serial number
NumberAppearances = [Zeros, Ones, Twos, Threes, Fours, Fives, Sixes, Sevens, Eights, Nines]

Maximums = []

MaxNums = 0

Max = max(NumberAppearances)

print(Max)

if Zeros == Max:
    print("Zeros")
    Maximums.append("Zero")
    MaxNums = MaxNums + 1
if Ones == Max:
    print("Ones")
    Maximums.append("One")
    MaxNums = MaxNums + 1
if Twos == Max:
    print("Twos")
    Maximums.append("Two")
    MaxNums = MaxNums + 1
if Threes == Max:
    print("Threes")
    Maximums.append("Three")
    MaxNums = MaxNums + 1
if Fours == Max:
    print("Fours")
    Maximums.append("Four")
    MaxNums = MaxNums + 1
if Fives == Max:
    print("Fives")
    Maximums.append("Five")
    MaxNums = MaxNums + 1
if Sixes == Max:
    print("Sixes")
    Maximums.append("Six")
    MaxNums = MaxNums + 1
if Sevens == Max:
    print("Sevens")
    Maximums.append("Seven")
    MaxNums = MaxNums + 1
if Eights == Max:
    print("Eights")
    Maximums.append("Eight")
    MaxNums = MaxNums + 1
if Nines == Max:
    print("Nines")
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

