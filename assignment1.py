#create a mapping of two items and their values
name_and_reason ={
        "FullName":"John Akpa Ujah",
        "reasonForAttendingAISaturday":
        "have grown my knowledge in python especially in the aspect of Machine learning and also associated fully with my fellow Pythonistas"
         }

#Print the values in the dictionary above
print("My name is ", name_and_reason["FullName"],  "and at the end of this cohort i want to ", name_and_reason["reasonForAttendingAISaturday"] )

#list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10,11,75,55,33,55,24,14,12,29]
#An empty list to store even numbers
even= []
#An empty list to store odd numbers
odd = []
#iterate through the numbers
for number in numbers:
    #check for even numbers and append to even list
    if number % 2 == 0:
        even.append(number)
    #if not even,append to odd list
    else:
        odd.append(number)
#print the number total number in even list
print("Number of even numbers: ",len(even))
#print the number total number in odd list
print("Number of odd numbers: ",len(odd))