def base_analyze_text():
    words_count = 0
    line_count = 0
    longest_length = 0
    number_of_longest_line = 0
    longest_line = ""

    lines = [
        "Заходит однажды в бар улитка и говорит:",
        "- Можно виски с колой?",
        "- Простите, но мы не обслуживаем улиток.",
        "И бармен вышвырнул ее за дверь.",
        "Через неделю заходит опять эта улитка и спрашивает:"
    ]

    file = open("resource/text.txt", "w+", encoding="utf-8")
    for line in lines:
        file.write(f"{line}\n")

    with open("resource/text.txt", "r", encoding="utf-8") as file:
        content = file.readlines()

    for line in content:
        clear_line = line.strip()
        words_count += len(clear_line.split())
        line_count += 1
        if len(clear_line) > longest_length:
            longest_length = len(clear_line)
            longest_line = clear_line
            number_of_longest_line = line_count

    print(f"Колличество строк в файле: {line_count}.")
    print(f"Колличество слов в файле: {words_count}.")
    print(f"Самая длинная строка: {number_of_longest_line}) {longest_line}.")

if __name__ == "__main__":
    base_analyze_text()
