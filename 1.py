def check_height(students, height):
    return height in students

# Пример
students_heights = [150, 155, 160, 165, 170, 175, 180]
height_to_check = 170
print(check_height(students_heights, height_to_check))