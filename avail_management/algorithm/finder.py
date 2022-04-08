from polls.models import Order
from datetime import date
from datetime import datetime

# This file contains a list of functions for order management.


class KeyDate:
    day_of_year = 0
    is_start = True
    actual_date = datetime.now();

    def __init__(self, day_of_year, is_start, actual_date):
        self.day_of_year = day_of_year
        self.is_start = is_start
        self.actual_date = actual_date;


# This function load all the existing orders and returns the currently active ones.
def load_active_orders():
    return Order.objects.filter(end_date__gte=date.today()).order_by('-start_date')


def find_next_available(max_capacity, orders):
    key_dates = []
    for o in orders:
        key_dates.append(KeyDate(o.start_date.timetuple().tm_yday, True, o.start_date))
        key_dates.append(KeyDate(o.end_date.timetuple().tm_yday, False, o.end_date))
    return find(max_capacity, datetime.today(), key_dates)


# This function is the implementation of the sweeping-line algorithm.
def find(max_capacity, today, key_dates):
    if len(key_dates) < 2 * max_capacity:
        return today

    # Need to sort the key dates by the day_of_year.
    sorted_key_dates = sorted(key_dates, key=lambda KeyDate: KeyDate.day_of_year, reverse=False)

    num_occupied = 0
    for i in range(len(sorted_key_dates)):
        current_date = sorted_key_dates[i]
        if current_date.is_start:
            num_occupied += 1
        else:
            num_occupied -= 1

        # There might be multiple orders start or end on the same day
        if i + 1 < len(sorted_key_dates) and sorted_key_dates[i + 1].day_of_year == current_date.day_of_year:
            continue

        if current_date.day_of_year >= today.timetuple().tm_yday and num_occupied < max_capacity:
            return current_date.actual_date
    return 0
