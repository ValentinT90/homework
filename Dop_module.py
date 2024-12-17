grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(sorted(students))
assessments_1=sum(grades[0])/ len(grades[0])
print(assessments_1)
assessments_2=sum(grades[1])/ len(grades[1])
print(assessments_2)
assessments_3=sum(grades[2])/ len(grades[2])
print(assessments_3)
assessments_4=sum(grades[3])/ len(grades[3])
print(assessments_4)
assessments_5=sum(grades[4])/ len(grades[4])
print(assessments_5)
average_scores={sorted(students)[0]:assessments_1,sorted(students)[1]:assessments_2,
sorted(students)[2]:assessments_3,sorted(students)[3]:assessments_4,sorted(students)[4]:assessments_5}
print(average_scores)