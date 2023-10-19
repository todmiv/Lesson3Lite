def input_numbers():
    numbers_input = input("Введите элементы списка с разделителем: ")
    delimiters = [",", ";", "/"]
    used_delimiters = [delimiter for delimiter in delimiters if delimiter in numbers_input]
    return numbers_input, used_delimiters

numbers_input, used_delimiters = input_numbers()

# Проверяем, если использовано более одного разделителя
if len(used_delimiters) > 1:
    print("Ошибка ввода. Пожалуйста, используйте только один разделитель: ',', ';', '/'")
    numbers_input, used_delimiters = input_numbers()

delimiter = used_delimiters[0]

# Разделяем введенные числа по разделителю и сохраняем их в список
numbers = numbers_input.split(delimiter)

# Создаем новый список, содержащий только уникальные элементы, которые встречаются только один раз в исходном списке
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

# Выводим новый список на экран
print("Результат:", ", ".join(unique_numbers))
