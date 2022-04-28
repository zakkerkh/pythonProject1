#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#28/04/2022
#Hello, how are you doing

num1 = input("Enter string 1: ") #takes user input for the strings
num2 = input("Enter string 2: ")
while len(num1) != len(num2): #If the strings aren't the same in length it informs them and makes them reenter
    print("Not the same length. Try again.")
    num1 = input("Enter string 1: ")
    num2 = input("Enter string 2: ")

var1 = len(num1) #stores the length of the entry as a variable in order to know how many letters to add to the final answer
count = 0 #this will keep track of how many times the while loop will run
answer = "" #the variable for the final answer

while count != var1: #this will run the while loop as many times till the letter amount is reached)
    answer += num1[count] + num2[count] #add the letters to the string for each loop run
    count += 1 #add to the while loop counter to make sure it doesn't run past the letter amount

print(answer) #prints the final answer