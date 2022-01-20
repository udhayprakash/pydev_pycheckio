#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/sun-angle/solve/
"""


def sun_angle(time):
    degrees_per_hour = 180 / 12  # 15.0
    degrees_per_minute = degrees_per_hour / 60  # 0.25

    hours, minutes = map(int, time.split(':'))
    if 6 <= hours <= 18:
        if hours == 18 and minutes > 0:
            return "I don't see the sun!"
        hours -= 6
        return hours * degrees_per_hour + minutes * degrees_per_minute
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("12:15"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("06:00") == 0
    assert sun_angle("07:00") == 15
    assert sun_angle("12:00") == 90
    assert sun_angle("12:15") == 93.75
    assert sun_angle("18:00") == 180
    assert sun_angle("18:01") == "I don't see the sun!"
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
