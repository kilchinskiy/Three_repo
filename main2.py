# Modul 5 Home work 3

import sys #Отримуємо аргумент командного рядка.
import os #Іинструменти для роботи з операційною системою.
from typing import List, Dict #Повертає слвоник, Є словником.

def parse_log_line(line: str) -> dict: #Перетворює лог в словник.
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

def load_logs(file_path: str) -> List[dict]: #Завантажуеємо лог і повертаємо словник.
    logs = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            log = parse_log_line(line)
            if log:
                logs.append(log)
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]: #Фільтруємо логи.
    return [log for log in logs if log["level"].lower() == level.lower()]

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]: #Рахуємо кількість логів.
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]) -> None: #Виводимо логи у вігляді таблиці.
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main(): #Перевіряємо шлях до лого.
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_логфайлу> [рівень]")
        return

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None
    if not os.path.exists(file_path): #Автоматично створюємо файл логів.
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("""2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
""")
        print(f"Файл {file_path} був створений автоматично.")
    try:
        logs = load_logs(file_path) # Завантажуємо логи.
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return

    counts = count_logs_by_level(logs) # Рахуємо статистику
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)  #Всі записи цього рівня. Якщо він є.
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()

#Перевірка у терміналі.
#python main.py logfile.log
#python main.py logfile.log error