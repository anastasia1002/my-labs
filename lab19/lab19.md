## Task1
__Дано текстовий файл, який містить дійсні числа. Визначити найменший елемент серед додатніх.__
```py
with open("text.txt") as file:
    a=[]
    for el in file:
        a.append(float(el))
    res = []
    for i in a:
        if i > 0:
            res.append(i)
            m = min(res)

    print(m)
```

## Task2
__Дано типізований файл, який містить деякий текст (кожен елемент типу string[40]).Вивести рядки тексту, які містять символ «А» у порядку зворотному до порядку слідування їх у файлі.__
```py
with open("text1.txt") as file:
    a = []
    for line in file:
        if "A" in line:
            a.append(line)
    for index in range(-1, -len(a) - 1, -1):
        print(a[index])

    print(a)
```