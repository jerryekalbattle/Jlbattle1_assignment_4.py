# Step 1: Foundation Setup
student_name = "Jerryeka Battle"
current_gpa = 3.9
study_hours = 25
social_points = 50
stress_level = 80
print(f"Welcome to College Life Adventure Game\n\nYour Stats\n\tName: {student_name}\n\tGPA: {current_gpa}\n\tStudy Hours: {study_hours}\n\tSocial Points {social_points}\n\tStress Level {stress_level}")

# Step 2: Course Planning Decision

print("Choose your Entertainment Time:")
print("A) 1 Hours per day")  
print("B) 4 Hours per day")
print("C) 7 Hours per day")

choice = input("Your Choice: ")
if choice == "A":
    if current_gpa <= 2.8:
        print("You Failed")
    else:
        study_hours = study_hours + 5
        stress_level = stress_level - 10
        if stress_level >= 100:
            print("You've Died This Level Proceed to next one")
        else:
            if study_hours <= 0:
                print("You've Died This Level Proceed to next one")
                if stress_level >= 100:
                    print("You've Died This Level Proceed to next one")
elif choice == "B":
    if current_gpa <= 3.0:
        print("You Failed")
    else:
        study_hours = study_hours - 5
        stress_level = stress_level + 10
        if stress_level >= 100:
            print("You've Died This Level Proceed to next one")
            if study_hours <= 0:
                print("You've Died This Level Proceed to next one")
elif choice == "C":
    if current_gpa <= 3.5:
        print("You Failed")
    else:
        study_hours = study_hours - 10
        stress_level = stress_level + 20
        if stress_level >= 100:
            print("You've Died This Level Proceed to next one")
            if study_hours <= 0:
                print("You've Died This Level Proceed to next one")
else:
    print("Not Valid Try Again")

print(f"GPA: {current_gpa}\nStudy Hours: {study_hours}\nStress Level: {stress_level}\nSocial Points:{social_points}")

# Step 3: Study Strategy Decision

study_list = ["Python", "Math", "English", "History"]

choice = input("Your Class to study: ")

if choice in study_list:
    current_gpa = current_gpa + 0.2
    social_points -= 20
    if social_points <= 0:
        print("You've Died This Level Proceed to next one")
    else:
        print("Go to Next Level")
elif choice in study_list:
    if current_gpa <= 3.0:
        print("You Failed")
    else:
        social_points -= 10
        if social_points <= 0:
            print("You've Died This Level Proceed to next one")
        else:
            print("Go to Next Level")
elif choice in study_list:
    if current_gpa <= 3.5:
        print("You Failed")
    else:
        social_points += 10
        if social_points <= 0:
            print("You've Died This Level Proceed to next one")
        else:
            print("Go to Next Level")
elif choice not in study_list:
    if current_gpa <= 3.2 and current_gpa != 0:
        print("You Failed")
    else:  
        social_points -= 20
        if social_points < 0 or social_points == 0:
            print("You've Died This Level Proceed to next one")
        else:
            print("Go to Next Level")
else:
    print("Not Valid Run Again")

print(f"GPA: {current_gpa}\nStudy Hours: {study_hours}\nStress Level: {stress_level}\nSocial Points:{social_points}")

# Step 4: Final Semester Assessment

print("Choose how you commuting:")
print("A) Walking")  
print("B) Car")
print("C) Shuttle")

valid = False

choice = input("Your Choice: ")
if choice == "A":
    stress_level is stress_level - 30
    if current_gpa == 3.0 and stress_level <= 73:
        print("You've Died on the last Level")
    else:
        print("congrats")
if choice == "B":
    stress_level is stress_level - 10
    if current_gpa == 3.0:
        print("You've Died on the last Level")
    else:
        print("congrats")
if choice == "C":
    stress_level is stress_level - 20
    if current_gpa == 3.0 or current_gpa > 3.0:
        print("You've Died on the last Level")
    else:
        print("congrats")
else:
    choice is not valid
    print("Not Valid Try Again")

print(f"GPA: {current_gpa}\nStudy Hours: {study_hours}\nStress Level: {stress_level}\nSocial Points:{social_points}")