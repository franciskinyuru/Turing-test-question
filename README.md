# Turing-test-question
Turing test question 
# Hi there i thought good to try share my way for the turing practise test.
#I implemented it on my own view but i welcome more easier ways of impementing it 

Here is the question
![image](https://user-images.githubusercontent.com/49100234/143646346-28d89326-a900-4002-a9ed-12e1b604a080.png)

Though my implementation is not the best

I thought of how first i can change the string "52DC+" to a list

i used the below method to do that
ops=[]          # Initialize the empty list for assignment later
line=input()    # get the input from user
list1=[]        # initialize an empty list
list1[:0]=line  # convert the line input to a list.
ops=list1       #Assign list1 to Our list ops
# The next step is to convert the Integers which are in string form in the list
opss=[]         # create a temporaly List
for item in ops:#loop through the list
    if item.isnumeric(): # check if a value of the list is a numeral 
        item=int(item)   # if true convert to int and append to our temporal list
        opss.append(item)
    else:               # Else append to the Temporal list
        opss.append(item)
        
# reassign the list to ##ops list as below:
ops=opss

# create a new temporal list 
newops=[]

# next step loop through our list and get both the indexs and values of the list
for idx, val in enumerate(ops):

# Check if the length of our list is 0 or 1 as below and return the sum 
     if len(ops)<=0:
       sum =0
    elif len(ops)==1:
        sum=ops[0]
  # if length is greater than one then you can carry on the other part.
  
  #  step 1. check if value is int if true append to our newops list.
     else:
        if type(val) == int:
            newops.append(val)
   # step 2 . check if value is C if so remove the last value in our newops list.
        if val == "C":
            newops.pop()
   # step 3 . check if value is D if so take the last value in our newops list ans double it and append it in the newops list but you have also to check if length of our newops             list is zero
        if val == "D":
            if len(newops)==0:
                pass
            else:
                score = (newops[-1])*2
                newops.append(score)
 #  Step 4 . check if our value is + if so check first id the length of our newops list is less than 2. then take the last two values in the newops list and sum then and the               outcome append it to the newops list
        if val == "+":
            if len(newops)<2:
                pass
            else:
                score = newops[-1]+newops[-2]
                newops.append(score)
 #  step 5 . add the values of our list to the the total value.
        sum = 0
        for ele in range(0, len(newops)):
            sum = sum + newops[ele]

         print(sum)


## This is my only view of this problem ## I welcome ideas kindly raise any issues i am available to harder

