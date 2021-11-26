#x-denotes a new score this
# + denotes the sum of previous 2 score
# D denotes records a new new score that is double the previous score
# c Invalidates the previos score
# question return all the previous scores in the record

#ops=[5,2,"C","D","+"]
#ops=[5,-2,4,"C","D",9,"+","+"]
#ops=[1]
line=input()
list1=[]
list1[:0]=line
ops=list1
opss=[]
for item in ops:
    if item.isnumeric():
        item=int(item)
        opss.append(item)
    else:
        opss.append(item)
print(opss)
ops=opss
newops=[]

for idx, val in enumerate(ops):
    if len(ops)<=0:
       sum =0
    elif len(ops)==1:
        sum=ops[0]
    else:
        if type(val) == int:
            newops.append(val)
        if val == "C":
            newops.pop()
        if val == "D":
            if len(newops)==0:
                pass
            else:
                score = (newops[-1])*2
                newops.append(score)
        if val == "+":
            if len(newops)<2:
                pass
            else:
                score = newops[-1]+newops[-2]
                newops.append(score)
        sum = 0
        for ele in range(0, len(newops)):
            sum = sum + newops[ele]

print(sum)
