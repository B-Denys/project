original_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Hello World', 'Денис']
def remove_duplicates(input_list):
    return list(set(input_list))
def sort_list(input_list):
    numbers = sorted([x for x in input_list if isinstance(x, (int, float))])
    strings = sorted([x for x in input_list if isinstance(x, str)])
    return numbers + strings
unique_list = remove_duplicates(original_list)
sorted_list = sort_list(unique_list)
print("Список без повторень:", unique_list)
print("Відсортований список:", sorted_list)