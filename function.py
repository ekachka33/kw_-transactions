import json
from datetime import datetime


def load_operations(file_path):
    """
    Загрузить операции из указанного JSON файла.

    :param file_path: Путь к файлу JSON с операциями
    :return: Список операций
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)



def filter_executed_operations(operations):
    """
    Отфильтровать операции, оставив только выполненные (EXECUTED).

    :param operations: Список всех операций
    :return: Список выполненных операций
    """
    executed_operations = []
    for operation in operations:
        if operation.get('state') == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations


def parse_date(operation):
    """
    Преобразовать строку с датой в объект datetime.

    :param operation: Операция
    :return: Объект datetime
    """
    return datetime.fromisoformat(operation['date'])

def sort_operations_by_date(operations):
    """
    Отсортировать операции по дате в порядке убывания.

    :param operations: Список операций
    :return: Список отсортированных операций
    """
    return sorted(operations, key=parse_date, reverse=True)


def mask_account_number(account):
    """
    Замаскировать номера счетов и карт.

    :param account: Номер счета или карты
    :return: Замаскированный номер
    """
    if 'Счет' in account:
        return f'Счет **{account[-4:]}'
    else:
        parts = account.split(' ')
        if len(parts) == 2 and len(parts[1]) >= 4:
            return f'{parts[0]} {parts[1][:4]} {parts[1][4:6]}** ****{parts[1][-4:]}'
        elif len(parts) > 2:
            return f'{parts[0]} {parts[1]} {parts[-1][:4]} {parts[-1][4:6]}** ****{parts[-1][-4:]}'
        else:
            return ''


def format_operation(operation):
    """
    Отформатировать одну операцию для вывода.

    :param operation: Операция
    :return: Строка, отформатированная для вывода
    """
    date = datetime.fromisoformat(operation['date']).strftime('%d.%m.%Y')
    description = operation['description']
    from_account = mask_account_number(operation.get('from', ''))
    to_account = mask_account_number(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    from_to = f'{from_account} -> {to_account}' if from_account else to_account

    return f"{date} {description}\n{from_to}\n{amount} {currency}"