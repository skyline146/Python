# Описати рекурсивную функцію Fact (N) дійсного типу, яка обчислює значення факторіала N! = 1 • 2 • ... • N (N> 0 - параметр цілого типу).
# За допомогою цієї функції обчислити факторіали п'яти довільних натуральних чисел.
import random as r
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


Array = [r.randint(1,10) for i in range(0, 5)]
for i in Array:
    print(fact(i))