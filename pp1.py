

year_age = int(input("Enter your age or  year of Birth : "))
isage = False
isyear = False

if len(str(year_age))==4:
    isyear = True

else:
    
    isage = True



if (year_age<1900 & isyear):
    print("You seem to be oldest person alive")
    exit()

if (year_age>2019):
    print("You are not yet born")
    exit()



if isage:
    year_age = 2020 - year_age

print(f"You will be 100 year old in {year_age + 100}")

interestedyear = int(input("Enter the year you want  to know your age in \n"))

print(f"You will be {interestedyear - year_age} year old in {interestedyear}")