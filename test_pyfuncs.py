#!/usr/bin/env python3
"""
File 'test_pyfuncs.py' is used to test functions in module
'pyfuncs.py'. 'test_pyfuncs.py' and 'pyfuncs.py' SHOULD exist
in same directory.

If a SINGLE 'test_*.py' file exists:
    Invoke with verbosity via 'pytest -vrP'
    Invoke without verbosity via 'pytest'
Else:
    Invoke with verbosity via 'pytest ./pyfuncs.py -vrP'
    Invoke without verbosity via 'pytest ./pyfuncs.py'
"""
import datetime
import inspect
import logging
import sys
import time

from io import StringIO

import pytest
from unittest.mock import (
    MagicMock,
    Mock,
    patch,
)

from pyfuncs import (
    add,
    divide,
    eb_time_local,
    eb_time_utc,
    exercise_datetime,
    exercise_inspect,
    exercise_randint,
    exercise_time,
    feet_2_meters,
    get_joke_dict,
    get_joke_else,
    get_random_int,
    is_dt_today_a_weekday,
    kilograms_2_pounds,
    len_joke_dict,
    len_joke_else,
    meters_2_feet,
    multiply,
    pounds_2_kilograms,
    printing_the_name_of_this_function,
    request_input,
    return_args_and_kwargs,
    return_args_only,
    return_kwargs_only,
    subtract,
)


# 'import sys' REQUIRED to force:
# logging StreamHandler to use 'stdout" instead of 'stderr'

# Name the logger '__name__'
logger = logging.getLogger(name=__name__)
# log via 'logger.info; instead of 'logging.info'.
# Establish which severity of messages to pass to the handler
logger.setLevel(logging.INFO)
# Create a console handler OVERRIDE default '(sys.stderr)'
stream_handler = logging.StreamHandler(stream=sys.stdout)
# Establish which severity of messages to respond to
stream_handler.setLevel(logging.INFO)
# Creat a message format
stream_format = logging.Formatter(
    '%(asctime)s %(levelname)s:%(name)s'
    ':%(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
# Add this format to the handler
stream_handler.setFormatter(stream_format)
# Convert loggint time to UTC
logging.Formatter.converter = time.gmtime
# Add handler to the logger
logger.addHandler(stream_handler)
# Disable progation to root logger - eliminate duplicate messages.
logger.propagate = False


spaces6 = ' '*6
spaces9 = ' '*9
spaces14 = ' '*14


def test_inspect_not_imported():
    logger.info(
        "'\nTest for a POTENTIAL missing 'inspect' import."
    )
    try:
        exercise_inspect()
    except NameError as e:
        # If NOT False
        logger.error(e)
        assert False, f'{e}'


def test_datetime_not_imported():
    logger.info(
        "'\nTest for a POTENTIAL missing 'datetime' import."
    )
    try:
        exercise_datetime()
    except NameError as e:
        # If NOT False
        logger.error(e)
        assert False, f'{e}'


def test_time_not_imported():
    logger.info(
        "'\nTest for a POTENTIAL missing 'time' import."
    )
    try:
        exercise_time()
    except NameError as e:
        # If NOT False
        logger.error(e)
        assert False, f'{e}'


def test_randint_not_imported():
    logger.info(
        "'\nTest for a POTENTIAL missing 'randint' import."
    )
    try:
        exercise_randint()
    except NameError as e:
        # If NOT False
        logger.error(e)
        assert False, f'{e}'


def test_requests_not_imported_dict():
    logger.info(
        "'\nTest for a POTENTIAL missing 'requests' import."
    )
    try:
        get_joke_dict()
    except NameError as e:
        # If NOT False
        logger.error(e)
        assert False, f'{e}'


def test_requests_not_imported_else():
    logger.info(
        "'\nTest for a POTENTIAL missing 'requests' import."
    )
    try:
        get_joke_else()
    except NameError as e:
        # If NOT False
        logger.error(e)
        assert False, f'{e}'


def test_feet_2_meters_bad_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    feet = "Invalid value for feet"
    with pytest.raises(TypeError):
        feet_2_meters(feet)


def test_meters_2_feet_bad_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    feet = "Invalid value for meters"
    with pytest.raises(TypeError):
        meters_2_feet(feet)


def test_pounds_2_kilograms_bad_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    pounds = "Invalid value for pounds"
    with pytest.raises(TypeError):
        pounds_2_kilograms(pounds)


def test_kilograms_2_pounds_bad_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    kilograms = "Invalid value for kilograms"
    with pytest.raises(TypeError):
        kilograms_2_pounds(kilograms)


def test_feet_2_meters_zero_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    feet = 0
    test_feet = 0
    expected_result = feet
    result = feet_2_meters(test_feet)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_meters_2_feet_zero_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    meters = 0
    test_meters = 0
    expected_result = meters
    result = meters_2_feet(test_meters)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_pounds_2_kilograms_zero_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    pounds = 0
    test_pounds = 0
    expected_result = pounds
    result = pounds_2_kilograms(test_pounds)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_kilograms_2_pounds_zero_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    kilograms = 0
    test_kilograms = 0
    expected_result = kilograms
    result = kilograms_2_pounds(test_kilograms)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_feet_2_meters_large_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    feet_2_meters_mult = 0.30480
    feet = 10000
    test_feet = 10000
    expected_result = feet * feet_2_meters_mult
    result = feet_2_meters(test_feet)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_meters_2_feet_large_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    meters_2_feet_mult = 3.28084
    meters = 10000
    test_meters = 10000
    expected_result = meters * meters_2_feet_mult
    result = meters_2_feet(test_meters)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_pounds_2_kilograms_large_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    pounds_2_kilograms_mult = 0.453592
    pounds = 10000
    test_pounds = 10000
    expected_result = pounds * pounds_2_kilograms_mult
    result = pounds_2_kilograms(test_pounds)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_kilograms_2_pounds_large_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    kilograms_2_pounds_mult = 2.20462
    kilograms = 10000
    test_kilograms = 10000
    expected_result = kilograms * kilograms_2_pounds_mult
    result = kilograms_2_pounds(test_kilograms)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_feet_2_meters_small_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    feet_2_meters_mult = 0.30480
    feet = 1
    test_feet = 1
    expected_result = feet * feet_2_meters_mult
    result = feet_2_meters(test_feet)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_meters_2_feet_small_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    meters_2_feet_mult = 3.28084
    meters = 1
    test_meters = 1
    expected_result = meters * meters_2_feet_mult
    result = meters_2_feet(test_meters)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_pounds_2_kilograms_small_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    pounds_2_kilograms_mult = 0.453592
    pounds = 1
    test_pounds = 1
    expected_result = pounds * pounds_2_kilograms_mult
    result = pounds_2_kilograms(test_pounds)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_kilograms_2_pounds_small_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    kilograms_2_pounds_mult = 2.20462
    kilograms = 1
    test_kilograms = 1
    expected_result = kilograms * kilograms_2_pounds_mult
    result = kilograms_2_pounds(test_kilograms)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_bad_addend_x_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    addend_x = 'a'
    addend_y = 11
    with pytest.raises(ValueError):
        add(addend_x, addend_y)


def test_add_bad_addend_y_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    addend_x = 22
    addend_y = 'b'
    with pytest.raises(ValueError):
        add(addend_x, addend_y)


def test_add_mixed_float_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = -14.0
    addend_y = 5.0
    expected_result = float(-9.0)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_mixed_float_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = 14.0
    addend_y = -5.0
    expected_result = float(9.0)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_mixed_int_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = -14
    addend_y = 5
    expected_result = (-9)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_mixed_int_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = 14
    addend_y = -5
    expected_result = (9)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_negative_float_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = -14.0
    addend_y = -5.0
    expected_result = float(-19.0)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_negative_float_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = -5.0
    addend_y = -14.0
    expected_result = float(-19.0)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_negative_int_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = -14
    addend_y = -5
    expected_result = (-19)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_negative_int_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = -5
    addend_y = -14
    expected_result = (-19)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_positive_float_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = 14.0
    addend_y = 5.0
    expected_result = float(19.0)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_positive_float_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = 5.0
    addend_y = 14.0
    expected_result = float(19.0)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_positive_int_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = 14
    addend_y = 5
    expected_result = (19)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_add_positive_int_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    addend_x = 5
    addend_y = 14
    expected_result = (19)
    result = add(addend_x, addend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_divide_bad_dividend_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    dividend = 'a'
    divisor = 11
    with pytest.raises(ValueError):
        divide(dividend, divisor)


def test_divide_bad_divisor_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    dividend = 22
    divisor = 'b'
    with pytest.raises(ValueError):
        divide(dividend, divisor)


def test_divide_by_zero_float():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    dividend = 11
    divisor = float(0.0)
    with pytest.raises(ZeroDivisionError):
        divide(dividend, divisor)


def test_divide_by_zero_int():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    dividend = 22
    divisor = int(0)
    with pytest.raises(ZeroDivisionError):
        divide(dividend, divisor)


def test_divide_mixed_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    dividend = -14
    divisor = 5
    expected_result = -2.8
    floor_division_result = -3
    result = divide(dividend, divisor)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces14}'{expected_result}'\n"
            f"Actual Result:{spaces9}'{result}'\n"
            f"Floor Division Result: '{floor_division_result}'\n"
        )


def test_divide_mixed_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    dividend = 14
    divisor = -5
    expected_result = -2.8
    floor_division_result = -3
    result = divide(dividend, divisor)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces14}'{expected_result}'\n"
            f"Actual Result:{spaces9}'{result}'\n"
            f"Floor Division Result: '{floor_division_result}'\n"
        )


def test_divide_negatives():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    dividend = -14
    divisor = -5
    expected_result = 2.8
    floor_division_result = 2
    result = divide(dividend, divisor)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces14}'{expected_result}'\n"
            f"Actual Result:{spaces9}'{result}'\n"
            f"Floor Division Result: '{floor_division_result}'\n"
        )


def test_divide_positives():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    dividend = 14
    divisor = 5
    expected_result = 2.8
    floor_division_result = 2
    result = divide(dividend, divisor)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces14}'{expected_result}'\n"
            f"Actual Result:{spaces9}'{result}'\n"
            f"Floor Division Result: '{floor_division_result}'\n"
        )


def test_multiply_bad_multiplier_x_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    multiplier_x = 'a'
    multiplican_y = 11
    with pytest.raises(ValueError):
        multiply(multiplier_x, multiplican_y)


def test_multiply_bad_multiplican_y_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    multiplier_x = 22
    multiplican_y = 'b'
    with pytest.raises(ValueError):
        multiply(multiplier_x, multiplican_y)


def test_multiply_mixed_float_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = -14.0
    multiplican_y = 5.0
    expected_result = (-70.0)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_mixed_float_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = 14.0
    multiplican_y = -5.0
    expected_result = (-70.0)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_mixed_int_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = -14
    multiplican_y = 5
    expected_result = (-70)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_mixed_int_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = 14
    multiplican_y = -5
    expected_result = (-70)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_negative_float_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = -14.0
    multiplican_y = -5.0
    expected_result = (70.0)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_negative_float_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = -5.0
    multiplican_y = -14.0
    expected_result = (70.0)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_negative_int_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = -14
    multiplican_y = -5
    expected_result = (70)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_negative_int_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = -5
    multiplican_y = -14
    expected_result = (70)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_positive_float_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = 14.0
    multiplican_y = 5.0
    expected_result = (70.0)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_positive_float_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = 5.0
    multiplican_y = 14.0
    expected_result = (70.0)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_positive_int_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = 14
    multiplican_y = 5
    expected_result = (70)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_multiply_positive_int_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    multiplier_x = 5
    multiplican_y = 14
    expected_result = (70)
    result = multiply(multiplier_x, multiplican_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_bad_minuend_x_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    minuend_x = 'a'
    subtrahend_y = 11
    with pytest.raises(ValueError):
        subtract(minuend_x, subtrahend_y)


def test_subtract_bad_subtrahend_y_value():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'")
    minuend_x = 22
    subtrahend_y = 'b'
    with pytest.raises(ValueError):
        subtract(minuend_x, subtrahend_y)


def test_subtract_mixed_float_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = -14.0
    subtrahend_y = 5.0
    expected_result = float(-19.0)
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_mixed_float_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = 14.0
    subtrahend_y = -5.0
    expected_result = float(19.0)
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_mixed_int_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = -14.0
    subtrahend_y = 5.0
    expected_result = -19.0
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_mixed_int_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = 14.0
    subtrahend_y = -5.0
    expected_result = 19.0
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_negative_float_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = -14.0
    subtrahend_y = -5.0
    expected_result = float(-9.0)
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
            )


def test_subtract_negative_float_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = -5.0
    subtrahend_y = -14.0
    expected_result = float(9.0)
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_negative_int_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = -14
    subtrahend_y = -5
    expected_result = -9
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_negative_int_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = -14
    subtrahend_y = -5
    expected_result = -9
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_positive_float_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = 14.0
    subtrahend_y = 5.0
    expected_result = float(9.0)
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_positive_float_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = 5.0
    subtrahend_y = 14.0
    expected_result = float(-9.0)
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_positive_int_01():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = 14
    subtrahend_y = 5
    expected_result = 9
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_subtract_positive_int_02():
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    minuend_x = 14
    subtrahend_y = 5
    expected_result = 9
    result = subtract(minuend_x, subtrahend_y)
    if not result == expected_result:
        assert logger.info(
            f"\nExpected:{spaces6}'{expected_result}'\n"
            f"Actual Result: '{result}'\n"
        )


def test_request_1_input(monkeypatch):
    """
    Mock user input request(s) via 'side_effects' list
    if first entry ==  'q':
        return 'q'
    else:
        return prior entry
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    expected_result = 'q'
    # Specify SINGLE monkeypatched user_input_string
    monkeypatch.setattr('builtins.input', lambda _: 'q')
    result = request_input()
    assert result == expected_result


def test_request_2_inputs(monkeypatch):
    """
    Mock user input request(s) via 'side_effects' list
    if first entry ==  'q':
        return 'q'
    else:
        return prior entry
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    expected_result = '222'
    inputs = iter(['222', 'q'])
    # Iterate through MULTIPLE monkeypatched user_input_strings
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = request_input()
    assert result == expected_result


def test_request_3_inputs(monkeypatch):
    """
    Mock user input request(s) via 'side_effects' list
    if first entry ==  'q':
        return 'q'
    else:
        return prior entry
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    expected_result = '333'
    # Iterate through MULTIPLE monkeypatched user_input_strings
    inputs = iter(['222', '333', 'q'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = request_input()
    assert result == expected_result


def test_request_4_inputs(monkeypatch):
    """
    Mock user input request(s) via 'side_effects' list
    if first entry ==  'q':
        return 'q'
    else:
        return prior entry
    """
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    expected_result = '444'
    # Iterate through MULTIPLE monkeypatched user_input_strings
    inputs = iter(['222', '333', '444', 'q'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = request_input()
    assert result == expected_result


def test_args_only():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    arg1 = 'parg_one'
    arg2 = 'parg_two'
    arg3 = 'parg_three'
    expected_result = ['parg_one', 'parg_two', 'parg_three']
    assert (
        return_args_only(arg1, arg2, arg3,) ==
        expected_result
    )


def test_args_and_default_kwargs():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    arg1 = 'parg_one'
    arg2 = 'parg_two'
    arg3 = 'parg_three'
    expected_result = (
        ['parg_one', 'parg_two', 'parg_three'],
        {
            'named1': 'n_one',
            'named2': 'n_two',
            'named3': 'n_three'
        }
    )
    assert (
        return_args_and_kwargs(
            arg1, arg2, arg3,
        ) == expected_result
    )


def test_args_and_unique_kwargs():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    arg1 = 'parg_one'
    arg2 = 'parg_two'
    arg3 = 'parg_three'
    named1 = 'n_one_unique'
    named2 = 'n_two_unique'
    named3 = 'n_three_unique'
    expected_result = (
        ['parg_one', 'parg_two', 'parg_three'],
        {
            'named1': 'n_one_unique',
            'named2': 'n_two_unique',
            'named3': 'n_three_unique',
        }
    )
    assert (
        return_args_and_kwargs(
            arg1, arg2, arg3,
            named1, named2, named3,
        ) == expected_result
    )


def test_default_kwargs():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    expected_result = {
        'named1': 'n_one',
        'named2': 'n_two',
        'named3': 'n_three',
    }
    assert (
        return_kwargs_only() ==
        expected_result
    )


def test_unique_kwargs():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    named1 = 'n_one_unique'
    named2 = 'n_two_unique'
    named3 = 'n_three_unique'
    expected_result = {
        'named1': 'n_one_unique',
        'named2': 'n_two_unique',
        'named3': 'n_three_unique',
    }
    assert (
        return_kwargs_only(named1, named2, named3) ==
        expected_result
    )


def test_printing_called_function_name_with_capsys(capsys):
    """Capture ( 'stdout' ) from logger() used in tested function"""
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    printing_the_name_of_this_function()
    stdout, stderr = capsys.readouterr()
    # Test will execute an UGLY failure WITHOUT the trailing '\n'.
    expected_result = (
        "Executing Function: 'printing_the_name_of_this_function'\n"
    )
    assert stdout == expected_result


@patch('sys.stdout', new_callable=StringIO)
# Cannot use 'autospec' and 'new_callable' together
# @patch('sys.stdout', new_callable=StringIO, autospec=True)
def test_printing_called_function_name_with_mocked_stdout(mock_stdout):
    """Mimic ( 'stdout' ) from logger() used in tested function"""
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    # Test will execute an UGLY failure WITHOUT the trailing '\n'.
    expected_result = (
        "Executing Function: 'printing_the_name_of_this_function'\n"
    )
    printing_the_name_of_this_function()
    assert mock_stdout.getvalue() == expected_result


def test_printing_called_function_name_with_normal_stdout():
    """Capture ( 'stdout' ) from logger() used in tested function"""
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    printing_the_name_of_this_function()


@patch('pyfuncs.randint', return_value=7, autospec=True)
def test_get_random_int(mock_randint):
    """Mimic ( 'randint' ) used in tested function"""
    # Code in tested function ( returned_value = modifier + roll )
    # Adjust mocked randint return value and modifier parameter to suit
    begin = 2
    bookend = 22
    modifier = 5
    expected_result = 12
    assert get_random_int(begin, bookend, modifier) == expected_result
    # Verify that randint was called with (begin, bookend)
    mock_randint.assert_called_once_with(begin, bookend)


@patch('pyfuncs.requests', autospec=True)
def test_200_OK_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 200 - OK
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=200)
    test_string = 'Mocked ( OK ) URL response_string'
    mock_response.json.return_value = {'value': test_string}
    mock_requests.get.return_value = mock_response
    expected_response = test_string
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_200_OK_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 200 - OK
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=200)
    test_string = 'Mocked ( OK ) URL response_string'
    mock_response.json.return_value = {'value': test_string}
    mock_requests.get.return_value = mock_response
    expected_response = test_string
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_301_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 301 - Permanent Redirect
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=301)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '301 - Permanent Redirect'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_301_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 301 - Permanent Redirect
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=301)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '301 - Permanent Redirect'
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_302_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 302 - Temporary Redirect
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=302)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '302 - Temporary Redirect'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_302_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 302 - Temporary Redirect
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=302)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '302 - Temporary Redirect'
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_401_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 401 - Unauthorized
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=401)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '401 - Unauthorized'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_401_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 401 - Unauthorized
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=401)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '401 - Unauthorized'
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_403_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 403 - Forbidden
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=403)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '403 - Forbidden'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_403_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 403 - Forbidden
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=403)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '403 - Forbidden'
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_404_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 404 - Not Found
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=404)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '404 - Not Found'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_404_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 404 - Not Found
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=404)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '404 - Not Found'
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_410_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 410 - Gone
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=410)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '410 - Gone'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_410_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 410 - Gone
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=410)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '410 - Gone'
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_500_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 500 - Internal Server Error
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=500)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '500 - Internal Server Error'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_500_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 500 - Internal Server Error
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=500)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '500 - Internal Server Error'
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_502_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 502 - Bad Gateway
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=502)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '502 - Bad Gateway'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_502_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 502 - Bad Gateway
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=502)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '502 - Bad Gateway'
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_503_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 503 - Service Unavailable
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=503)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '503 - Service Unavailable'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_503_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 503 - Service Unavailable
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=503)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '503 - Service Unavailable'
    assert get_joke_else() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_504_get_joke_dict(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 504 - Gateway Timeout
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=504)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '504 - Gateway Timeout'
    assert get_joke_dict() == expected_response


@patch('pyfuncs.requests', autospec=True)
def test_504_get_joke_else(mock_requests):
    """Mock URL response"""
    # If a module referenced by 'patch()' is unavailable,
    # UGLY errors will occur.
    # HTTP Status Code 504 - Gateway Timeout
    # The expected_response should == the mocked URL response
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    mock_response = MagicMock(status_code=504)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '504 - Gateway Timeout'
    assert get_joke_else() == expected_response


@patch('pyfuncs.get_joke_dict', autospec=True)
def test_len_joke_dict(mock_get_joke_dict):
    """Mock function response"""
    # Test a function that calls another function
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    test_string = (
        'Substitute this return string for the URL return when'
        "'get_joke_disc()' is called"
    )
    mock_get_joke_dict.return_value = test_string
    assert len_joke_dict() == len(test_string)


@patch('pyfuncs.get_joke_else', autospec=True)
def test_len_joke_else(mock_get_joke_else):
    """Mock function response"""
    # Test a function that calls another function
    # get the frame object of the function
    frame = inspect.currentframe()
    logger.info(f"Executing: '{frame.f_code.co_name}'\n")
    test_string = (
        'Substitute this return string for the URL return when'
        "'get_joke_else()' is called"
    )
    mock_get_joke_else.return_value = test_string
    assert len_joke_else() == len(test_string)


def test_eb_time_local_zone_false():
    eb_time_local(False)


def test_eb_time_utc_zone_false():
    eb_time_utc(False)


def test_eb_time_local_zone_true():
    eb_time_local(True)


def test_eb_time_utc_zone_true():
    eb_time_utc(True)


def test_dt_weekend():
    """Mimic ( 'datetime' ) used in tested function"""
    logger.info("\n'datetime' days (Sun == Zero) - (Sat == Six)")
    # Weekend test dates
    # Day 06 Saturday == 2018_1006
    # Day 07 Sunday == 2018_1007

    mock_date = Mock(wraps=datetime.datetime, autospec=True)
    saturday = datetime.datetime(year=2018, month=10, day=6)
    sunday = datetime.datetime(year=2018, month=10, day=7)

    mock_date.now.return_value = saturday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_dt_today_a_weekday()
        assert not flag_weekday
    mock_date.now.return_value = sunday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_dt_today_a_weekday()
        assert not flag_weekday


def test_dt_weekday():
    """Mimic ( 'datetime' ) used in tested function"""
    logger.info("\n'datetime' days (Sun == Zero) - (Sat == Six)")
    # Weekday test dates
    # Day 01 Monday == 2018_1001
    # Day 02 Tuesday == 2018_1002
    # Day 03 Wednesday == 2018_1003
    # Day 04 Thursday == 2018_1004
    # Day 05 Friday == 2018_1005

    mock_date = Mock(wraps=datetime.datetime, autospec=True)
    monday = datetime.datetime(year=2018, month=10, day=1)
    tuesday = datetime.datetime(year=2018, month=10, day=2)
    wednesday = datetime.datetime(year=2018, month=10, day=3)
    thursday = datetime.datetime(year=2018, month=10, day=4)
    friday = datetime.datetime(year=2018, month=10, day=5)

    mock_date.now.return_value = monday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_dt_today_a_weekday()
        assert flag_weekday
    mock_date.now.return_value = tuesday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_dt_today_a_weekday()
        assert flag_weekday
    mock_date.now.return_value = wednesday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_dt_today_a_weekday()
        assert flag_weekday
    mock_date.now.return_value = thursday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_dt_today_a_weekday()
        assert flag_weekday
    mock_date.now.return_value = friday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_dt_today_a_weekday()
        assert flag_weekday


# EOF
