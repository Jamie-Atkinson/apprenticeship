"""
data = []
n = input("How many elements do you have?")
print n
for i in range(int(n)):
    data.append(int(input("please input element " + str(i+1) + ": ")))
    print(data)
"""

data=[90,30,13,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83]
#data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

checker = True
for i in range(int(len(data))):
    if data[i] == int(data[i]):
        x=1
    else: 
        checker = False

if checker == False:
    print("better luck next time")
    exit()


#part1
number_of_students = len(data)
max_student_score = max(data)
min_student_score = min(data)
average_student_score = "{0:.2f}".format(sum(data)/len(data),)
print("\nThe number of students is: " + str(number_of_students) +"\n\nThe maximum score achived is: " + str(max_student_score)+ "\n\nThe minimum score acchived is: " + str(min_student_score) + "\n\nThe average student score is: " + str(average_student_score))
"""

#this is an old version of part 2, newer more efficient version (that actually works) can be found bellow


#part2
n10 = ""
n1020 = ""
n2030 = ""
n3040 = ""
n4050 = ""
n5060 = ""
n6070 = ""
n7080 = ""
n8090 = ""
n90100 = ""
n100 = ""
for i in range(int(len(data))):
    
    if data[i] <=10:
        n10 += "*"
    elif data[i] <=20:
        n1020 += "*"
    elif data[i] <=30:
        n2030 += "*"
    elif data[i] <= 40:
        n3040 += "*"
    elif data[i] <=50:
        n4050 += "*"
    elif data[i] <=60:
        n5060 += "*"
    elif data[i] <=70:
        n6070 += "*"
    elif data[i] <=80:
        n7080 += "*"
    elif data[i] <=90:
        n8090 += "*"
    elif data[i] <=100:
        n90100 += "*"
    else:
        n100 += "*"
     
print("\nScores between 0 and 10: " + (n10) + "\n\nScores between 10 and 20: " + n1020 + "\n\nScores between 20 and 30: " + n2030 + "\n\nScores between 30 and 40: " + n3040 + "\n\nScores between 40 and 50: " + n4050 + "\n\nScores between 50 and 60: " + n5060 + "\n\nScores between 60 and 70: " + n6070 + "\n\nScores between 70 and 80: " + n7080 + "\n\nScores between 80 and 90: " + n8090 + "\n\nScores between 90 and 100: " + n90100)

sets =[n10,n1020,n2030,n3040,n4050,n5060,n6070,n7080,n8090,n90100]

nn10=0
nn1020=0
nn2030=0
nn3040=0
nn4050=0
nn5060=0
nn6070=0
nn7080=0
nn8090=0
nn90100=0


print (nn10)

"""





band = [0,0,0,0,0,0,0,0,0,0]
sand = ['','','','','','','','','','']

for i in range (len(data)):
    band[data[i] //10] += 1
    sand[data[i] //10] += "*"

for i in range (len(band)):
    print("\nTotal number of scores between "+ str((i)*10) + " and " + str((i+1)*10) + ":" + sand[i])
"""
#part 3 alternative method i was considering
averagecount = 0
percentage_of_students_to_pass = 60
total_students_to_pass = (percentage_of_students_to_pass*len(data)/100)
sorteddata = sorted(data)
threshold_mark=(sorteddata[(len(data)-total_students_to_pass)-1])
print(threshold_mark)
print(round_down(threshold_mark,-1))

"""

#part 3
averagecount = 0
oneprintcheck = 0
for i in range (len(band)):
    if ((((len(data)-averagecount)*100)/len(data)) >=60):
        averagecount += band[i]
    elif (oneprintcheck == 0):
        print("\nThe pass mark to ensure 60% of students will pass the exam is: " + str(i-1) + "0")
        oneprintcheck +=1
