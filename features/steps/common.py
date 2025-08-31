
import time
from behave import step


@step('I store current timestamp in storage key "{key}"')
def store_current_ts_in_key(context, key):
    context.storage[key] = int(time.time())

@step('the value in storage with key "{key1}" is higher then valule in storage with key "{key2}"')
def compare_2_keys(context, key1, key2):
    assert context.storage[key1] > context.storage[key2], f'{context.storage[key1]} is not higher than {context.storage[key2]}'

@step('I sleep "{seconds:d}" seconds')
def sleep(context, seconds):
    time.sleep(seconds)

@step('debug')
def pause_func(context):
    print("Debug")