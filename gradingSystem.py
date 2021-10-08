Marks=int(input("Give your mark: "))

if Marks>=80 and Marks<=100:
    print("Your Grade is A+")
elif Marks>=70 and Marks<80:
    print("Your Grade is A")
elif Marks>=60 and Marks<70:
    print("Your Grade is A-")
elif Marks>=50 and Marks<60:
    print("Your Grade is B")
elif Marks>=40 and Marks<50:
    print("Your Grade is B-")
elif Marks>=0 and Marks<40:
    print("Your Grade is F")
else:
    print("Your Number is Not valid")