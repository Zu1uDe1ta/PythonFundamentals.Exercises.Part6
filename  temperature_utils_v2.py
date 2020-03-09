from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    fahrenheit = float(convert_to_celsius())
    celsius = (fahrenheit - 32) * 5 / 9
    celsius_to_kelvin = (celsius + 273.15)
    return(celsius 'celsius', celsius_to_kelvin 'kelvin')# remove pass statement and implement me


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    celsius = float(convert_to_fahrenheit())
    fahrenheit = (9 * celsius) / 5 + 32
    fahrenheit_to_kelvin = 273.5 + ((fahrenheit - 32.0) * (5.0/9.0))
    return(fahrenheit 'fahrenheit', fahrenheit_to_kelvin 'kelvin')# remove pass statement and implement me


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    for x in temperature_tuple:
        if input_unit_of_measurement = 'f':
            return((x), ((x - 32) * 5 / 9)))
        if input_unit_of_measurement = 'c':
            return((x), ((9 * x) / 5 + 32)))# remove pass statement and implement me
