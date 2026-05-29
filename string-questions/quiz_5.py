def count_leap_years(year_range):
    # Split the range into start and end years
    start, end = map(int, year_range.split("-"))

    count = 0

    # Check each year in the range
    for year in range(start, end + 1):
        # Leap year condition
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            count += 1

    return count


# Examples
print(count_leap_years("1981-1991"))  
print(count_leap_years("2000-2020"))  