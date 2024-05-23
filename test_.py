import pytest
import json
from function import load_operations, filter_executed_operations, parse_date, sort_operations_by_date, mask_account_number, format_operation
from datetime import datetime


def test_parse_date():
    operation = {"date": "2022-01-01T10:00:00.000000"}
    parsed_date = parse_date(operation)
    assert isinstance(parsed_date, datetime)
    assert parsed_date.year == 2022
    assert parsed_date.month == 1
    assert parsed_date.day == 1


def test_mask_account_number():
    assert mask_account_number("Счет 1234567890") == "Счет **7890"
    assert mask_account_number("Maestro 1234567890123456") == "Maestro 1234 56** ****3456"
    assert mask_account_number("Visa Platinum 9876543210987654") == "Visa Platinum 9876 54** ****7654"

def test_format_operation():
    operation = {
        "date": "2022-01-01T10:00:00.000000",
        "description": "Sample operation 1",
        "from": "Maestro 1234567890123456",
        "to": "Счет 1234567890",
        "operationAmount": {"amount": "100.00", "currency": {"name": "USD"}}
    }
    formatted_operation = format_operation(operation)
    assert formatted_operation.startswith("01.01.2022 Sample operation 1")
    assert formatted_operation.endswith("100.00 USD")