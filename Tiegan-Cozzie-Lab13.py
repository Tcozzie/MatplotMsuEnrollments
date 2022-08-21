import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# November 30, 2021                                 |
# Tiegan Cozzie                                       |
# -------------------------------------------------
file=open("fall-2020.csv","r",encoding="ISO-8859-1")
def read_file(file_name):
    nameList=[]
    enrollmentList=[]
    useful=file.readlines()
    for i in useful[1:]:
        line=i.strip().split(',')
        nameList.append(line[1])
        enrollmentList.append(int(line[0]))
    names=np.array(nameList)
    enrollments=np.array(enrollmentList)
    return ([names,enrollments])
        

    
        
        

# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)
    colors=["gold","blue","gold","blue","gold","blue","gold"]
    plt.figure("MSU Enrollments")
    plt.title("Fall 2020")
    plt.xlabel("College")
    plt.ylabel("Enrollment")
    plt.ylim(0,5000)
    plt.bar(college_names,college_enrollments, color=colors)
    

    plt.show()
    

# -------------------------------------------------

main(file)
