#!/usr/bin/env python3
"""
Module 'pyfuncs.py' contains functions testable using the 'pytest'
framework.

'python requests' MUST be installed.
"""
import datetime
import inspect
import logging
import requests
import sys
import time
from random import randint


# 'import sys' REQUIRED to force:
# logging StreamHandler to use 'stdout' instead of 'stderr'
# Name the logger '__name__'
logger = logging.getLogger(name=__name__)
# log via 'logger.info; instead of 'logging.info'.
# Establish which severity of messages to pass to the handler
logger.setLevel(logging.INFO)
# Create a console handler to OVERRIDE default '(sys.stderr)'
# Output will be redirected to '(sys.stdout)'.
stream_handler = logging.StreamHandler(stream=sys.stdout)
# Establish which severity of messages to respond to
stream_handler.setLevel(logging.INFO)
# Creat a message format
stream_format = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
# Add this format to the handler
stream_handler.setFormatter(stream_format)
# Add handler to the logger
logger.addHandler(stream_handler)
# Disable progation to root logger - eliminate duplicate messages.
logger.propagate = False


def add(x, y):
    # WARNING isinstance(Boolean) is considered an integer
    if type(x) not in [int, float]:
        addend_x = x
        err_msg = f"Invalid Addend X Value == '{addend_x}'"
        print()
        logger.error(f'\n{err_msg}')
        raise ValueError(err_msg)
    if type(y) not in [int, float]:
        addend_y = y
        err_msg = f"Invalid Addend Y Value == '{addend_y}'"
        print()
        logger.error(f'\n{err_msg}')
        raise ValueError(err_msg)
    sum = x + y
    return sum


def divide(x, y):
    if y == 0:
        divisor = y
        err_msg = f"Invalid Divisor Value == '{divisor}'"
        logger.error(f'\n{err_msg}')
        raise ZeroDivisionError(err_msg)
    # WARNING isinstance(Boolean) is considered an integer
    # Checking type is more reliable
    if type(x) not in [int, float]:
        dividend = x
        err_msg = f"Invalid Dividend Value == '{dividend}'"
        print()
        logger.error(f'\n{err_msg}')
        raise ValueError(err_msg)
    if type(y) not in [int, float]:
        divisor = y
        err_msg = f"Invalid Divisor Value == '{divisor}'"
        print()
        logger.error(f'\n{err_msg}')
        raise ValueError(err_msg)
    quotient = x / y
    return quotient


def multiply(x, y):
    # WARNING isinstance(Boolean) is considered an integer
    # Checking type is more reliable
    if type(x) not in [int, float]:
        multiplier_x = x
        err_msg = f"Invalid Multiplier X Value == '{multiplier_x}'"
        print()
        logger.error(f'\n{err_msg}')
        raise ValueError(err_msg)
    if type(y) not in [int, float]:
        multiplican_y = y
        err_msg = f"Invalid Multiplican Y Value == '{multiplican_y}'"
        print()
        logger.error(f'\n{err_msg}')
        raise ValueError(err_msg)
    product = x * y
    return product


def subtract(x, y):
    # WARNING isinstance(Boolean) is considered an integer
    # Checking type is more reliable
    if type(x) not in [int, float]:
        minuend_x = x
        err_msg = f"Invalid Minuend X Value == '{minuend_x}'"
        print()
        logger.error(f'\n{err_msg}')
        raise ValueError(err_msg)
    if type(y) not in [int, float]:
        subtrahend_y = y
        err_msg = f"Invalid Subtrahend Y Value == '{subtrahend_y}'"
        print()
        logger.error(f'\n{err_msg}')
        raise ValueError(err_msg)
    difference = x - y
    return difference


def eb_time_local(zone_offset=True):
    """Print local time"""
    # Create a time object, extract appropriate time and UTC offset
    local_time = time.localtime()
    local_time_all_names = time.tzname
    local_time_zone_active = time.strftime("%Z", local_time)
    utc_offset = time.strftime("%z", local_time)
    if __name__ == '__main__':
        # get the frame object of the function
        frame = inspect.currentframe()
        logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    if zone_offset:
        if __name__ == '__main__':
            logger.info(
                f'\nLocal Time Zone(s): {local_time_all_names}'
                f'\nLocal Time Zone_Active: {local_time_zone_active}'
                f'\nUTC Offset: {utc_offset}\n')
        date_time_zone_offset_str = (
              f'{time.strftime("%Y-%m-%d %H:%M:%S %Z %z", local_time)}')
        logger.info(
            f'\nDate, Time, Zone and Offset:'
            f'\n{date_time_zone_offset_str}')
        return list(date_time_zone_offset_str.split(" "))
    else:
        date_time_zone_str = (
              f'{time.strftime("%Y-%m-%d %H:%M:%S %Z", local_time)}')
        logger.info(f'\nDate, Time and Zone:\n{date_time_zone_str}')
        return list(date_time_zone_str.split(" "))


def eb_time_utc(zone_offset=True):
    """Print UTC time"""
    # Create a time object, extract appropriate time and UTC offset
    utc_time = time.gmtime()
    if __name__ == '__main__':
        # get the frame object of the function
        frame = inspect.currentframe()
        logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    if zone_offset:
        date_time_zone_offset_str = (
              f'{time.strftime("%Y-%m-%d %H:%M:%S %Z %z", utc_time)}')
        logger.info(
            f'\nDate, Time, Zone and Offset:'
            f'\n{date_time_zone_offset_str}')
        return list(date_time_zone_offset_str.split(" "))
    else:
        date_time_zone_str = (
              f'{time.strftime("%Y-%m-%d %H:%M:%S %Z", utc_time)}')
        logger.info(f'\nDate, Time and Zone:\n{date_time_zone_str}')
        return list(date_time_zone_str.split(" "))


def display_name_weekday(weekday_num, weekday_name):
    """Display day name - during the week"""
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(
        f"'{frame_detail}' {weekday_num},"
        f" Day of the week == {weekday_name}"
    )
    return


def display_name_weekend(weekday_num, weekday_name):
    """Display day name - during a weekend"""
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(
        f"'{frame_detail}' {weekday_num},"
        f" Day of the weekend == {weekday_name}"
    )
    return


def is_dt_today_a_weekday():
    """Determine if today is a weekday using 'import datetime'"""
    # 'datetime' is pytestable. 'time' ???
    flag_using_datetime = True
    if __name__ == '__main__':
        # get the frame object of the function
        frame = inspect.currentframe()
        print()
        logger.info(f"\nExecuting: '{frame.f_code.co_name}")
    weekday_first_mon_1 = 1
    weekday_last_fri_5 = 5
    weekday_first = weekday_first_mon_1
    weekday_last = weekday_last_fri_5
    print()
    if flag_using_datetime:
        logger.info("\n'datetime' days (Sun == Zero) - (Sat == Six)")
        # Create time object
        local_time_datetime = datetime.datetime.now()
        local_time = local_time_datetime
        # Extract time and if possible, the UTC offset
        weekday_name = local_time.strftime('%A')
        weekday_num = int(local_time.strftime('%w'))
        date_time_zone_str = (
            f'{local_time.strftime("%Y-%m-%d %H:%M:%S %Z")}'
        )
    else:
        logger.info("\n'time' days (Sun == Zero) - (Sat == Six)")
        # Create time object
        local_time_time = time.localtime()
        local_time = local_time_time
        # Extract time and if possible, the UTC offset
        weekday_name = time.strftime('%A', local_time)
        weekday_num = int(time.strftime('%w', local_time))
        date_time_zone_str = (
            f'{time.strftime("%Y-%m-%d %H:%M:%S %Z", local_time)}'
        )
    logger.info(f'Date and Time:\n{date_time_zone_str}')
    flag_weekday = False
    if (
        weekday_num >= weekday_first
        and weekday_num <= weekday_last
    ):
        flag_weekday = True
        display_name_weekday(weekday_num, weekday_name)
    else:
        display_name_weekend(weekday_num, weekday_name)
    logger.info(f"flag_weekday == {flag_weekday}")
    return (flag_weekday)


def is_tm_today_a_weekday():
    """Determine if today is a weekday using 'import time'"""
    # 'datetime' is pytestable. 'time' ???
    flag_using_datetime = False
    if __name__ == '__main__':
        # get the frame object of the function
        frame = inspect.currentframe()
        print()
        logger.info(f"\nExecuting: '{frame.f_code.co_name}")
    weekday_first_mon_0 = 0
    weekday_last_fri_4 = 4
    weekday_first = weekday_first_mon_0
    weekday_last = weekday_last_fri_4
    print()
    if flag_using_datetime:
        logger.info("\n'datetime' days (Sun == Zero) - (Sat == Six)")
        # Create time object
        local_time_datetime = datetime.datetime.now()
        local_time = local_time_datetime
        # Extract time and if possible, the UTC offset
        weekday_name = local_time.strftime('%A')
        weekday_num = int(local_time.strftime('%w'))
        date_time_zone_str = (
            f'{local_time.strftime("%Y-%m-%d %H:%M:%S %Z")}'
        )
    else:
        logger.info("\n'time' days (Sun == Zero) - (Sat == Six)")
        # Create time object
        local_time_time = time.localtime()
        local_time = local_time_time
        # Extract time and if possible, the UTC offset
        weekday_name = time.strftime('%A', local_time)
        weekday_num = int(time.strftime('%w', local_time))
        date_time_zone_str = (
            f'{time.strftime("%Y-%m-%d %H:%M:%S %Z", local_time)}'
        )
    logger.info(f'\nDate, Time and Zone:\n{date_time_zone_str}')
    flag_weekday = False
    if (
        weekday_num >= weekday_first
        and weekday_num <= weekday_last
    ):
        flag_weekday = True
        display_name_weekday(weekday_num, weekday_name)
    else:
        display_name_weekend(weekday_num, weekday_name)
    logger.info(f"flag_weekday == {flag_weekday}")
    return (flag_weekday)


def exercise_inspect():
    """
    Cause 'Pytest' to throw a LESS verbose error
    if 'inspect' was not imported
    """
    try:
        # Check to see if ( inspect ) has been imported
        # get the frame object of the function
        frame = inspect.currentframe()
        frame_detail = frame.f_code.co_name
        print()
        logger.info(f"Executing: '{frame_detail}'\n")
    except NameError as e:
        logger.error(f"\n'exercise_inspect'\nImport Error: {e}")
        raise
        return


def exercise_datetime():
    """
    Cause 'Pytest' to throw a LESS verbose error
    if 'datetime' was not imported
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    print()
    logger.info(f"Executing: '{frame_detail}'\n")
    try:
        # Check to see if ( datetime ) has been imported
        local_time = datetime.datetime.now()
        weekday_name = local_time.strftime('%A')
        weekday_num = int(local_time.strftime('%w'))
        logger.info(f"\nday_name:{weekday_name} day_num:{weekday_num}")
    except NameError as e:
        logger.error(f"\n'{frame_detail}'\nImport Error: {e}")
        raise
        return


def exercise_time():
    """
    Cause 'Pytest' to throw a LESS verbose error
    if 'time' was not imported
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    print()
    logger.info(f"Executing: '{frame_detail}'\n")
    try:
        # Check to see if ( time ) has been imported
        local_time = time.localtime()
    except NameError as e:
        logger.error(f"\n'{frame_detail}'\nImport Error: {e}")
        raise
        return
    # Extract time and if possible, the UTC offset
    weekday_name = time.strftime('%A', local_time)
    weekday_num = int(time.strftime('%w', local_time))
    logger.info(f"\nday_name:{weekday_name} day_num:{weekday_num}")


def exercise_randint():
    """
    Cause 'Pytest' to throw a LESS verbose error
    if 'datetime' was not imported
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    print()
    logger.info(f"Executing: '{frame_detail}'\n")
    begin = 1
    bookend = 22
    try:
        # Check to see if ( randint ) has been imported
        randint(begin, bookend)
    except NameError as e:
        logger.error(f"\n'{frame_detail}'\nImport Error: {e}")
        raise
        return


def get_joke_dict():
    """
    Attempt to get a joke from the web.
    Throw an error upon failure using dictionary logic
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    joke = 'No jokes'
    err_switch = {
        '301': '301 - Permanent Redirect',
        '302': '302 - Temporary Redirect',
        '401': '401 - Unauthorized',
        '403': '403 - Forbidden',
        '404': '404 - Not Found',
        '410': '410 - Gone',
        '500': '500 - Internal Server Error',
        '502': '502 - Bad Gateway',
        '503': '503 - Service Unavailable',
        '504': '504 - Gateway Timeout',
    }
    try:
        # Check to see if ( inspect ) has been imported
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
    except NameError as e:
        logger.error(f"\n'{frame_detail}' - Import Error: {e}")
        raise
        return
    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = err_switch.get(str(response.status_code), 'Unexpected ERROR!!')
    return joke


def get_joke_else():
    """
    Attempt to get a joke from the web.
    Throw an error upon failure using else if logic
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    joke = 'No jokes'
    try:
        # Check to see if ( requests ) has been imported
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
    except NameError as e:
        logger.error(f"\n'{frame_detail}' - Import Error: {e}")
        raise
        return

    if response.status_code == 200:
        joke = response.json()['value']
    elif response.status_code == 301:
        joke = '301 - Permanent Redirect'
    elif response.status_code == 302:
        joke = '302 - Temporary Redirect'
    elif response.status_code == 401:
        joke = '401 - Unauthorized'
    elif response.status_code == 403:
        joke = '403 - Forbidden'
    elif response.status_code == 404:
        joke = '404 - Not Found'
    elif response.status_code == 410:
        joke = '410 - Gone'
    elif response.status_code == 500:
        joke = '500 - Internal Server Error'
    elif response.status_code == 502:
        joke = '502 - Bad Gateway'
    elif response.status_code == 503:
        joke = '503 - Service Unavailable'
    elif response.status_code == 504:
        joke = '504 - Gateway Timeout'
    else:
        joke = 'Unexpected ERROR!!'
    return joke


def len_joke_dict():
    """
    Attempt to get a joke from the web.
    Throw an error upon failure using dictionary logic or
    return the joke's length
    """
    if __name__ == '__main__':
        # get the frame object of the function
        frame = inspect.currentframe()
        logger.info(f"\nExecuting: '{frame.f_code.co_name}'")
    joke = get_joke_dict()
    logger.info(f"\nMocked Joke string:\n'{joke}'")
    return len(joke)


def len_joke_else():
    """
    Attempt to get a joke from the web.
    Throw an error upon failure using else if logic or
    return the joke's length
    """
    if __name__ == '__main__':
        # get the frame object of the function
        frame = inspect.currentframe()
        logger.info(f"\nExecuting: '{frame.f_code.co_name}'")
    joke = get_joke_else()
    logger.info(f"\nMocked Joke string:\n'{joke}'")
    return len(joke)


def request_input():
    """
    Request then display user input.
    if first entry ==  'q':
        return 'q'
    else:
        return prior entry
    """

    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'")
    out_str = 'q'
    while True:
        err_num = input("\nEnter an error code or 'q' to quit: ")
        if err_num == 'q':
            logger.info(f'\nReturning Input String:\n{out_str}')
            return out_str
        else:
            print(f"You entered '{err_num}'")
            out_str = err_num


def access_dict():
    """Demo accessing a dictionary"""
    if __name__ == '__main__':
        # get the frame object of the function
        frame = inspect.currentframe()
        logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    err_switch = {
        '301': '301 - Permanent Redirect',
        '302': '302 - Temporary Redirect',
        '401': '401 - Unauthorized',
        '403': '403 - Forbidden',
        '404': '404 - Not Found',
        '410': '410 - Gone',
        '500': '500 - Internal Server Error',
        '502': '502 - Bad Gateway',
        '503': '503 - Service Unavailable',
        '504': '504 - Gateway Timeout',
    }
    while True:
        err_num = input("\nEnter an error code or 'q' to quit: ")
        print(f"You entered '{err_num}'")
        if err_num == 'q':
            return
        print(err_switch.get(str(err_num), 'Unexpected ERROR!!'))


def get_random_int(begin=1, bookend=11, modifier=2):
    """Get a random integer. Add modifier and return the result"""
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    try:
        # Check to see if ( randint ) has been imported
        roll = randint(begin, bookend)
    except NameError as e:
        logger.error(f"'{frame_detail}' - Import Error: {e}")
        return
    result = modifier + roll
    logger.info(
        f"\nbegin: '{begin}' bookend: '{bookend}'"
        f" modifier: '{modifier}' roll: '{roll}'"
        '\n return value  == roll + modifier'
        f"\n'{frame_detail}' returning'{result}'"
    )
    return result


def printing_the_name_of_this_function():
    """Used by 'Pytest' to validate stdout stream capture"""
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    print(f"Executing Function: '{frame_detail}'")


def return_args_only(
    # *args receives arguments as a tuple
    # **kwargs receives arguments as a dictionary
        arg1, arg2, arg3,
        # named1='n_one', named2='n_two', named3='n_three'
):
    """
    Used by 'Pytest' to validate capture of positional args
    Return a list containing args
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    print(f"Executing Function: '{frame_detail}'")
    print()
    args_list = [arg1, arg2, arg3,]
    logger.info(f'\nReturning args:\n"{args_list}"')
    return args_list


def return_kwargs_only(
    # *args receives arguments as a tuple
    # **kwargs receives arguments as a dictionary
        # arg1, arg2, arg3,
        named1='n_one', named2='n_two', named3='n_three'
):
    """
    Used by 'Pytest' to validate capture of keyword args
    Return a dictionary containin kwargs
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    print(f"Executing Function: '{frame_detail}'")
    print()
    kwargs_dict = {
        'named1': named1,
        'named2': named2,
        'named3': named3,
    }
    logger.info(
        f'\nReturning kwargs:\n"{kwargs_dict}"'
    )
    return kwargs_dict


def return_args_and_kwargs(
    # *args receives arguments as a tuple
    # **kwargs receives arguments as a dictionary
        arg1, arg2, arg3,
        named1='n_one', named2='n_two', named3='n_three'
):
    """
    Used by 'Pytest' to validate capture of positional and keyword args
    Return a dictionary containin kwargs
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    print(f"Executing Function: '{frame_detail}'")
    print()
    args_list = [arg1, arg2, arg3,]
    kwargs_dict = {
        'named1': named1,
        'named2': named2,
        'named3': named3,
    }
    logger.info(
        f'\nReturning args:\n"{args_list}"\n'
        f'\nReturning kwargs:\n"{kwargs_dict}"'
    )
    return args_list, kwargs_dict


def test_loop():
    """
    Request then display user input.
    if first entry ==  'q':
        return 'q'
    else:
        return prior entry
    """

    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    print()
    logger.info(f"Executing: '{frame_detail}'")
    out_str = 'q'
    while True:
        err_num = input("\nEnter an error code or 'q' to quit: ")
        print(f"Entered Value: '{err_num}'")
        if err_num == 'q':
            print()
            if err_num == out_str:
                logger.info(f'\nReturning Quit Value:\n{out_str}')
            else:
                logger.info(f'\nReturning Nummeric Value:\n{out_str}')
            return out_str
        try:
            # Check for numeric input
            err_num = float(err_num)
            calc_kilograms = pounds_2_kilograms(err_num)
            print()
            kilograms_2_pounds(calc_kilograms)
        except ValueError as e:
            print()
            logger.error(
                f"\n'{frame_detail}'\nNon-Numeric Value Error: {e}"
            )
            return
        out_str = err_num


def feet_2_meters(feet=1):
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'")
    feet_2_meters_mult = 0.30480
    if type(feet) not in [int, float]:
        err_msg = f"Invalid Foot Value == '{feet}'"
        print()
        logger.error(f'\n{err_msg}')
        raise TypeError(err_msg)
        return
    if feet == 0:
        meters = 0
    else:
        meters = feet * feet_2_meters_mult
    if feet == 1:
        msg_feet = 'foot'
    else:
        msg_feet = 'feet'
    print()
    logger.info(
        f"\n{feet:.5f}' {msg_feet} == '{meters:.5f}' meters\n"
        f"Returning: '{meters:.5f}' meters"
    )
    return meters


def meters_2_feet(meters=1):
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'")
    meters_2_feet_mult = 3.28084
    if type(meters) not in [int, float]:
        err_msg = f"Invalid Meter Value == '{meters}'"
        print()
        logger.error(f'\n{err_msg}')
        raise TypeError(err_msg)
        return
    if meters == 0:
        feet = 0
    else:
        feet = meters * meters_2_feet_mult
    if meters == 1:
        msg_meters = 'meters'
    else:
        msg_meters = 'meters'
    print()
    logger.info(
        f"\n{meters:.5f}' {msg_meters} == '{feet:.5f}, feet\n"
        f"Returning: '{feet:.5f}' feet\n"
    )
    return feet


def pounds_2_kilograms(pounds=1):
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'")
    pounds_2_kilograms_mult = 0.453592
    if type(pounds) not in [int, float]:
        err_msg = f"Invalid Pound Value == '{pounds}'"
        print()
        logger.error(f'\n{err_msg}')
        raise TypeError(err_msg)
        return
    if pounds == 0:
        kilograms = 0
    else:
        kilograms = pounds * pounds_2_kilograms_mult
    if pounds == 1:
        msg_pounds = 'pound'
    else:
        msg_pounds = 'pounds'
    print()
    logger.info(
        f"\n{pounds:.5f}' {msg_pounds} == '{kilograms:.5f}' kilograms\n"
        f"Returning: '{kilograms:.5f}' kilograms"
    )
    return kilograms


def kilograms_2_pounds(kilograms=1):
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'")
    kilograms_2_pounds_mult = 2.20462
    if type(kilograms) not in [int, float]:
        err_msg = f"Invalid Kilogram Value == '{kilograms}'"
        print()
        logger.error(f'\n{err_msg}')
        raise TypeError(err_msg)
        return
    if kilograms == 0:
        pounds = 0
    else:
        pounds = kilograms * kilograms_2_pounds_mult
    if kilograms == 1:
        msg_kilograms = 'kilogram'
    else:
        msg_kilograms = 'kilograms'
    print()
    logger.info(
        f"\n{kilograms:.5f}' {msg_kilograms} == '{pounds:.5f}, pounds\n"
        f"Returning: '{pounds:.5f}' pounds\n"
    )
    return pounds


def main():
    # eb_time_local(False)
    # eb_time_utc(False)
    # eb_time_local()
    # eb_time_utc()
    # is_tm_today_a_weekday()
    is_dt_today_a_weekday()
    # exercise_inspect()
    # exercise_datetime()
    # exercise_time()
    # print(get_joke_dict())
    # print(get_joke_else())
    # print(request_input())
    # access_dict()
    # len_joke_dict()
    # len_joke_else()
    # get_random_int(begin=1, bookend=11, modifier=1)
    # get_random_int()
    return


if __name__ == '__main__':
    main()
    # EOF
