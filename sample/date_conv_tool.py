import datetime


def get_timestamp():
    datetime_object = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return datetime_object


def get_readable(precision="minute"):
    now = datetime.datetime.now()
    if precision == "year":
        string_data = "%Y"
    elif precision == "month":
        string_data = "%b, %Y"
    elif precision == "day":
        string_data = "%b %d, %Y"
    elif precision == "minute":
        string_data = "%b %d, %Y %I:%M %p"
    elif precision == "second":
        string_data = "%b %d, %Y %I:%M:%S %p"

    readable = now.strftime(string_data)
    return readable


def get_readable_full_month(precision="minute"):
    now = datetime.datetime.now()
    if precision == "year":
        string_data = "%Y"
    elif precision == "month":
        string_data = "%B, %Y"
    elif precision == "day":
        string_data = "%B %d, %Y"
    elif precision == "minute":
        string_data = "%B %d, %Y %I:%M %p"
    elif precision == "second":
        string_data = "%B %d, %Y %I:%M:%S %p"

    readable = now.strftime(string_data)
    return readable


def get_readable_time(precision="minute"):
    now = datetime.datetime.now()
    if precision == "minute":
        string_data = "%I:%M %p"
    elif precision == "second":
        string_data = "%I:%M:%S %p"

    readable = now.strftime(string_data)
    return readable


def main():
    print(get_readable("year"))
    print(get_readable("month"))
    print(get_readable("day"))
    print(get_readable())
    print(get_readable("second"))

    print(get_readable_full_month("second"))

    print(get_readable_time())
    print(get_readable_time("second"))


# runs main (sample) if called directly
if __name__ == '__main__':
    main()
