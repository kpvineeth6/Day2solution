def findSum(str1):

    temp = "0"

    Sum = 0

    for ch in str1:

        if (ch.isdigit()):

            temp += ch

        else:

            Sum += int(temp)

            temp = "0"

    return Sum + int(temp)

str1 = "abc45def5ghi32"

print("sum of all numbers in a string=",findSum(str1))