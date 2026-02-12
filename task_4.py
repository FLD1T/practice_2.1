from datetime import datetime
FILENAME = "resource/calculator.log"

def write_log(filename, calculation):
    with open(filename, "a", newline='') as file:
        now = datetime.now()
        log = f"[{now.strftime("%Y-%m-%d %H:%M:%S")}] {calculation}\n"
        file.write(log)

def read_log(filename):
    with open(filename, "r", newline='') as file:
        lines = file.readlines()
        last_five_lines = lines[-5:]
    return last_five_lines

def clear_log(filename):
    with open(filename, "w", newline=''):
        pass
    print(f"Содержимое файла {filename} очищено!")

def calculate_with_log():
    try:
        try:
            first_num, second_num = input("Введите два числа через пробел.\n"
                                        "Ввод: ").split()
        except ValueError:
            quit("Вы не ввели два числа через пробел!")

        choice = input("Выберите операцию, которую хотите провести:\n"
                       "+ - * /\n"
                       "Ввод: ")
        first_num, second_num = int(first_num), int(second_num)

        match choice:
            case "+":
                result = f"{first_num} + {second_num} = {first_num + second_num}"
            case "-":
                result = f"{first_num} - {second_num} = {first_num - second_num}"
            case "*":
                result = f"{first_num} * {second_num} = {first_num * second_num}"
            case "/":
                result = f"{first_num} / {second_num} = {first_num / second_num}"
            case _:
                quit("Вы ввели не тот символ!")
    except ValueError:
        quit("Нужно вводить два числа через пробел и выбирать нужную операцию!")
    return result

def main(filename):
    i = True
    last_logs = read_log(filename)
    print("-" * 20, "\nКалькулятор с логированием\n", "-" * 20)
    print(f"Последние 5 операций в {filename}\n")
    if last_logs:
        for log in last_logs:
            print(log.strip())

    while i:
        choice = input("\nВозможности программы:\n"
                       "1 - Выполнить вычисление.\n"
                       "2 - Очистка лог-файла.\n"
                       "0 - Выход.\n"
                       "Выбор: ")
        match choice:
            case "1":
                write_log(filename, calculate_with_log())
            case "2":
                clear_log(filename)
            case "0":
                i = False
            case _:
                quit("Для выбора нужно вписывать число из списка!")

if __name__ == "__main__":
    main(FILENAME)