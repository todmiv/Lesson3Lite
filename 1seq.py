n = int(input("Введите количество элементов: "))
lst = []
for i in range(n):
    lst.append(int(input(f"Введите {i+1} элемент: ")))
lst.sort()
print(f"Вывод: {lst}")
