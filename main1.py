# Modul 5 Home work 2

import re #Видалення не потрібних символів.
from typing import Callable, Generator #Зміна функціі, Позначення генераторів.

def generator_numbers(text: str) -> Generator[float, None, None]: #Генератор який знаходить дійсні числа у тексті.
    pattern = r"\d+\.\d+|\d+"
    for match in re.findall(pattern, text): #Пошук чисел з крапкою.
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float: #Обчислення сумми чисел з тексту.
    return sum(func(text))

#Перевірка.
if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        " 1000.01 як основний дохід, доповнений додатковими надходженнями "
        " 27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")



