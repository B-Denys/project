Main_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
def remove_duplicates(input_list):
    return list(set(input_list))
def sort_list(input_list):
    numbers = sorted([x for x in input_list if isinstance(x, (int, float))])
    strings = sorted([x for x in input_list if isinstance(x, str)])
    return numbers + strings
Unique_list = remove_duplicates(Main_list)
Sorted_list = sort_list(Unique_list)
print("Список без повторень:", Unique_list)
print("Відсортований список:", Sorted_list)