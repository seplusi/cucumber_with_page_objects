import time
from steps.browser import close_web_driver


def before_scenario(context, scenario):
    context.storage = {'initial_ts': int(time.time())}
    print('Before scenario\n')


def after_scenario(context, scenario):
    print(f"Executing teardown for scenario: {scenario.name}")
    close_web_driver(context)

