import datetime
import decimal
import re

from pytest import fixture

from functions.level_1.four_bank_parser import BankCard, Expense, SmsMessage


@fixture(params=[
    {'param': {
        'verb_male': 'сделала',
        'verb_female': 'сделал',
        'gender': 'male'
    },
        'result': 'сделала'
    },
    {'param': {
        'verb_male': 'сделала',
        'verb_female': 'сделал',
        'gender': ''
    },
        'result': 'сделал'
    },
])
def gender(request):
    return request.param


@fixture(params=[
    {
        'date_str': 'tomorrow',
        'time': 11
    },
    {
        'date_str': '',
        'time': 22
    },
])
def compose_dt_from(request):
    today = datetime.date.today()
    dt = datetime.datetime(
        today.year,
        today.month,
        today.day,
        int(request.param['time']),
        int(request.param['time']),
    )
    if request.param['date_str'] == 'tomorrow':
        dt += datetime.timedelta(days=1)
    data = {
        'param': {
            'date_str': request.param['date_str'],
            'time_str': f'{request.param['time']}:{request.param['time']}'
        },
        'result': dt
    }
    return data


@fixture(params=[
    {'host_name': 'https://learn.python.ru', 'relative_url': 'advanced', 'get_params': {}},
    {'host_name': 'https://www.youtube.com', 'relative_url': 'watch', 'get_params': {'v': 'oi-E29ozktQ'}},
])
def build_url_fxt(request):
    get_params = request.param['get_params'] or {}
    querypart = ''
    if get_params:
        querypart = '?' + '&'.join([f'{k}={v}' for (k, v) in get_params.items()])
    url = f'{request.param['host_name']}/{request.param['relative_url']}{querypart}'
    print(url)
    return {
        'param': request.param,
        'result': url
    }


@fixture(params=[
    {'raw_details': '4090.00 RUB, 4785 23.02.24 11:11 Ashan authcode 76584',
     'cards': [{'last_digits': '4785', 'owner': 'John Doe'}, {'last_digits': '0948', 'owner': 'John Doe'}]},
    {'raw_details': '32500.00 RUB, 7659 17.02.24 10:01 Курс по программированию LPA authcode 98754',
     'cards': [{'last_digits': '9088', 'owner': 'John Doe'}, {'last_digits': '7659', 'owner': 'John Doe'}]},
])
def ineco_expense_fxt(request):
    sms = SmsMessage(
        text=request.param['raw_details'],
        author='test author',
        sent_at=datetime.datetime.now()
    )
    cards = [BankCard(**card) for card in request.param['cards']]
    raw_sum, raw_details = sms.text.split(', ')
    raw_details = raw_details.split(' authcode ')[0]
    raw_card, raw_date, raw_time, spend_in = raw_details.split(' ', maxsplit=3)
    expense = Expense(
        amount=decimal.Decimal(raw_sum.split(' ')[-2]),
        card=[c for c in cards if c.last_digits == raw_card[-4:]][0],
        spent_in=spend_in,
        spent_at=datetime.datetime.strptime(f'{raw_date} {raw_time}', '%d.%m.%y %H:%M'),
    )
    return {
        'param': {'sms': sms, 'cards': cards},
        'result': expense
    }


@fixture(params=[
    {'title': 'test', 'max_main_item_title_length': 100},
    {'title': 'test', 'max_main_item_title_length': 2},
    {'title': 'test', 'max_main_item_title_length': 3},
    {'title': 'Copy of test', 'max_main_item_title_length': 5},
    {'title': 'Copy of test', 'max_main_item_title_length': 12},
    {'title': 'Copy of test', 'max_main_item_title_length': 15},
    {'title': 'test (1)', 'max_main_item_title_length': 5},
    {'title': 'test (1)', 'max_main_item_title_length': 8},
    {'title': 'test (1)', 'max_main_item_title_length': 10},
    {'title': 'Copy of test (1)', 'max_main_item_title_length': 15},
    {'title': 'Copy of test (1)', 'max_main_item_title_length': 27},  # на этом кейсе ошибка то ли в функции толи у меня
    {'title': 'Copy of test (2)', 'max_main_item_title_length': 30},  # на этом кейсе ошибка то ли в функции толи у меня
])
def ch_cp_item_fxt(request):
    title = request.param['title']
    max_main_item_title_length = request.param['max_main_item_title_length']
    additional_copy_text: str = 'Copy of'
    title_with_additional_copy_text: str = f'{additional_copy_text} {title}'

    if len(title_with_additional_copy_text) >= max_main_item_title_length:
        return {
        'param': request.param,
        'result': title
    }
    if not title.startswith(additional_copy_text):
        return {
        'param': request.param,
        'result': title_with_additional_copy_text
    }

    last_element = title.split()[-1]
    element_in_brackets = last_element.split('(')[-1].split(')')[0]
    has_copy_number = all([re.search(r'\(\d+\)', last_element), element_in_brackets.isdigit()])
    title.replace(title.split()[-1], f'({int(element_in_brackets) + 1})') if has_copy_number else f'{title} (2)'
    return {
        'param': request.param,
        'result': title
    }