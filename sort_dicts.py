def sort_dicts_by_key(dict_list, sort_key):
    """
    Sorts a list of dictionaries by the specified key.

    Args:
        dict_list (list): List of dictionaries to sort.
        sort_key (str): The key to sort the dictionaries by.

    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda d: d.get(sort_key))

data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

sorted_data = sort_dicts_by_key(data, 'age')
print(sorted_data)
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]