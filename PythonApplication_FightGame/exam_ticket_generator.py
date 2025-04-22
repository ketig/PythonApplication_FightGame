import random

with open("students.txt", "r", encoding="utf-8") as f:
    students = [line.strip() for line in f if line.strip()]

with open("exercises.txt", "r", encoding="utf-8") as f:
    exercises = [line.strip() for line in f if line.strip()]

for student in students:
    selected_exercises = random.sample(exercises, 4)
    filename = f"{student}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for idx, exercise in enumerate(selected_exercises, 1):
            file.write(f"{idx}. {exercise}\n")

print("Exam tickets have been successfully created!")
