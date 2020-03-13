name = input("firstname")
surname = input ("surname")
exam_mark =float( input("exam_mark"))

if (exam_mark >= 80) and (exam_mark<=100):
    print(name, surname, "grade A- Outstanding")
elif (exam_mark >= 60) and (exam_mark<=79):
    print(name, surname, "grade B-Satisfactory")
elif (exam_mark >= 50) and (exam_mark <=59):
    print( name, surname,"grade C-Pass")
elif (exam_mark >= 0) and (exam_mark <= 49):
    print(name, surname,"grade D-Fail")

