name = input("What is your name? ")
maths_mark = int(input("What was your Maths mark? "))
chem_mark = int(input("What was your Chemistry mark? "))
phy_mark = int(input("What was your Physics mark? "))

overall = maths_mark + chem_mark + phy_mark

if overall >= 70:
    print("Your grade is, A")

elif overall >= 60:
    print("Your grade is, B")

elif overall >= 50:
    print("Your grade is, C")

elif overall >=40:
    print("Your grade is, D")

else:
    print("You failed")
    

