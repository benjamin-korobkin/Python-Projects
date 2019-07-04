# Check the list to find numbers whose sum is 0

def find0(listA):
    if 0 in listA:
        return("We have a sum! It's just 0!")
         

    for num in listA:
        if (num * -1) in listA:
            return("We have a sum! " + str(num) + " + " + str((num * -1)) + " = 0") 
             
    listB = []
    for num in listA:
        listB.append(listA[0])
        listA = listA[1:] ## listA loses its first element.
        if sum(listB) == 0 or -(sum(listB)) in listA:
            print("Sum found!", end = ' ')
            for num in listB:
                print(str(num) + " +", end=' ')
            return ("" + str(-sum(listB)) + " = 0")

    return ("No sum found :(")        

## Omg, find sum? NP!
nums = int(input("How many ints? "))
myList = []
while nums > 0:
    userInt = int(input("Int? "))
    myList.append(userInt)
    nums -= 1
## We now have all the user's input in myList
print (find0(myList))


'''
  Place all the user's input into a list called listA.
  Strategy: First check if the list contains a 0. If so, just return the zero
  and we're done.
  Then, check if the list contains two oppostie values.
  For example, 1 and -1, 2 and -2, 30 and -30. These are pairs of opposite
  numbers which, when added together, sum up to 0.
  If neither of these conditions are met, create a new empty list, called listB.
  Start by adding the first element from listA to listB. (Be sure to remove
  that element from listA.) Then, create a loop to check if listA contains the
  opposite value of the sum of what's in listB. At the end of each loop
  iteration, take out the first number from listA and append it to listB.
  Keep going, all the while checking if listA contains a value which is the
  opposite of the sum of what's inside listB. The loop will end when:
  1) the sum of listB adds up to 0
  2) listA contains an opposite value of the sum of listB
  3) We've exhausted the contents of listA
  If one of the first two conditions are met, we have successfully found a sum
  in listA that adds up to 0. Otherwise, condition 3) tells us that there is no
  sum that adds up to 0.
'''
