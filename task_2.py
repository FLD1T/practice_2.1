def filter_data():
    students_dict = {}

    with open("resource/students.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    result_file = open("result.txt", "w", encoding="utf-8")

    for line in lines:
        line = line.strip()
        try:
            name, rates = line.split(":")

        except ValueError:
            continue

        grades_list = rates.split(",")

        value = 0

        for rate in grades_list:
            value += int(rate)

        average_value = value / len(grades_list)

        students_dict[name] = round(average_value, 2)

        if average_value > 4.0:
            result_file.write(f"{name}: {average_value}\n")

    best_student = max(students_dict,key=students_dict.get)
    best_score = students_dict[best_student]
    print(f"Лучший студент: {best_student}: {best_score}")

if __name__ == "__main__":
    filter_data()
