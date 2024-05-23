from function import load_operations, filter_executed_operations, sort_operations_by_date, format_operation


def print_last_5_operations(file_path):
    """
    Вывести на экран последние 5 выполненных операций из указанного JSON файла.

    :param file_path: Путь к файлу JSON с операциями
    """
    operations = load_operations(file_path)
    executed_operations = filter_executed_operations(operations)
    sorted_operations = sort_operations_by_date(executed_operations)[:5]

    for operation in sorted_operations:
        print(format_operation(operation))
        print()


if __name__ == '__main__':
    print_last_5_operations('operations.json')