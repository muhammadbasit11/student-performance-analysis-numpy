import numpy as np
# producing 200 students data with 5 subjects
np.random.seed(12)
data=np.random.randint(0,101,size=(200,5))
# print(data)   #let data[0]=physics,data[1]=biology,data[2]=english,data[3]=stat,data[4]=maths


# step-1                  average_marks
average_marks=np.mean(data,axis=1)
print(f"the average marks of the students per subjects are: {average_marks} ")
# step-2 Count how many students scored > 85 in Math

students_math_marks=data[:,4]
marks_greater_85_maths=students_math_marks[students_math_marks>85]
no_of_students_with_85_greater_marks=marks_greater_85_maths.size
print(no_of_students_with_85_greater_marks)

# step-3 top 10 students average wise

# highest_average=np.sort(average_marks)       #arg gives us the indices
# highest_average_marks=highest_average[::-1]
# print(f"the highest averages marks are {highest_average_marks[0:10]}")

# to get the indexes of top 10 students
highest_average=np.argsort(average_marks)
highest_average_marks=highest_average[::-1]
print(f"the top students marks by indices are: {highest_average_marks[0:10]}")

#  STEP-4       Find subject with highest average
each_sub_average=np.average(data,axis=0)
highest_average_subject=np.argmax(each_sub_average) #argmax will give you the index of highest average
the_subject_with_highest_average=each_sub_average[highest_average_subject]
print(f"the highest average of the subject is {the_subject_with_highest_average} at {highest_average_subject} index")



