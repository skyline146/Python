# Відомо, що X кг цукерок коштують A гривень. Визначити, скільки коштує 1 кг і Y кг цих же цукерок.
x = int(input("Введите кг цукерок: "))
a = int(input("Введите стоимость за х кг: "))
print("1 kg sweets = ", a/x)
y = int(input("Введите y кг конфет: "))
print("Y kg sweets = ", (a/x)*y)