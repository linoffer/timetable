# Python program to create a table

from tkinter import *
import json
OPENHOUR = 'free'
BUSYHOUR = 'busy'
class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

num_of_hours = 6
num_of_days = 6
# take the data
for i in range(3):
    S = [["free" for x in range(num_of_days)] for i in range(num_of_hours)]
    file = open("sch.txt"+str(i), 'w')
    json.dump(S,file)






milon = {'pysics': 2, 'math': 3,"loop":5}

for i in milon:
    print(i)
    num_of_teachers = int(input("how many teacher for this subject?"))
    for j in range(num_of_teachers):
        S = [["free" for x in range(num_of_days)] for i in range(num_of_hours)]
        file = open("teacher.txt" + str(j), 'w')
        json.dump(S, file)




x = 0
for k in range(3):
    file = open("sch.txt"+str(k), 'r')
    S = json.load(file)
    for i in milon:
        for j in range(milon[i]):
            for d in range(len(S)):
                for h in range(len(S[d])):
                    if S[d][h] == "free" and x < milon[i]:
                        S[d][h] = i
                        x += 1

        x = 0
    file = open("sch.txt" + str(k), 'w')
    json.dump(S, file)

for i in S:
    print(i)
lst = S

    # find total number of rows and
    # columns in list
for i in range (3):
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    root = Tk()
    t = Table(root)
root.mainloop()

