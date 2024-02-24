from functions.level_1.four_bank_parser import parse_ineco_expense


def test_parse_ineco_expense(ineco_expense_fxt):
    assert parse_ineco_expense(**ineco_expense_fxt['param']) == ineco_expense_fxt['result']
