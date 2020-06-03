# Дано список кортежів grades = [( "Алла 4), (" Борис 2), ( "Катерина 3), (" Денис 5)].
# Вивести на екран послідовність повідомлень виду "Вітаю, Алла! Ваша оцінка - 4".

grades = [("Алла 4"), ("Борис 2"), ("Катерина 3"), ("Денис 5")]
strExample = ""
str1 = ""
str2 = ""
for i in grades:
    strExample = i
    for j in range(0, len(strExample)):
        if strExample[j] == " ":
            str1 = strExample[:j]
            str2 = strExample[j+1:]
    print("Вітаю, "+str1+"! Ваша оцінка - "+str2)