# num = "5.6777"
# print("Before conversion:", type(num))
# print("After conversion:", type(float(num)))

grade = float(input("Enter your grade: "))

"""
grade >= 70 === A
grade >= 60 === B
grade >= 50 === C
grade >= 40 === D
grade >= 30 === E
grade < 30 === F
"""
if grade >= 70:
    print("Grade A")
elif grade >= 60:
    print("Grade B")
elif grade >= 50:
    print("Grade C")
elif grade >= 40:
    print("Grade D")
elif grade >= 30:
    print("Grade E")
else:
    print("Grade F")



