# Modul 5 Home work 1

def caching_fibonacci(): #Порожній словник.
    cache = {}

    def fibonacci(n): #Умови словника.
        if n <= 0: #Повернути 0.
            return 0
        elif n == 1: #Повернути 1.
            return 1
        if n in cache: #Повернути cache[n].
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) #Повернути cache[n].
        return cache[n]

    return fibonacci

#Перевірка.
fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(15))  # 610
print(fib(20))  # 6765
