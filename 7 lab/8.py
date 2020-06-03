# Написати програму, в якій зберігаються дані про товари, їх кількість і ціну. При запуску програми ця інформація виводиться на екран.
# Далі користувачеві має пропонуватися вводити номера товарів і їх нову кількість. Зміна даних має завершуватися,
# якщо користувач вводить спеціально обумовлений символ (наприклад, 0). Після цього всі дані про товари повинні знову виводитися на екран.

listProducts = ["Mivina", "Pineapple", "Banana", "Water", "Beer"]
listQuantity = ["23", "14", "35", "15", "19"]
listPrice = ["4", "50", "6", "7", "15"]
for i in range(0, len(listPrice)):
    print(str(i+1)+". "+listProducts[i]+" - "+listQuantity[i]+" - "+listPrice[i]+" hrn.")
while True:
    a = int(input("Enter 1 - to change quantity of products, 0 - to exit: "))
    if a == 1:
        index = int(input("Enter the number of product: "))
        print("Enter new quantity of "+listProducts[index-1]+": ")
        listQuantity[index-1] = input()
    elif a == 0:
        break
for i in range(0, len(listPrice)):
    print(str(i+1)+". "+listProducts[i]+" - "+listQuantity[i]+" - "+listPrice[i]+" hrn.")