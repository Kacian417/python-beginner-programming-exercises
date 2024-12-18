import random

def get_color(color_number=4):
    # Making sure is a number and not a string
    color_number = int(color_number)

    switcher = {
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    
    return switcher.get(color_number,"Invalid Color Number")

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌

def get_allStudentColors():
    example_color = get_color(1)
    students_array = []
    # ✅ ↓ your loop here ↓ ✅ 1.loop 10 times, 2. generate a random number within the loop, 3. call get_color(random_number), 4. push the return random coloe to the student_array
    for i in range(0, 10):
        random_number = random.randint(0,3)
        random_color = get_color(random_number)
        students_array.append(random_color)
    
    return students_array

        
    

print(get_allStudentColors())
