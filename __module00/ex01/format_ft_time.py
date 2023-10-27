import time


def getSecondsSinceEpoch():
    return time.time()


current_time = time.time()
time_tuple = time.localtime(current_time)


month = time.strftime('%b', time_tuple)
day = time.strftime('%d', time_tuple)
year = time.strftime('%Y', time_tuple)


formated_time = f"{month} {day} {year}"

print("Seconds since January 1, 1970: " + f'{getSecondsSinceEpoch():,.4f}'
      + " or " + f'{getSecondsSinceEpoch():.2e}'
      + " in scientific notation\n" + formated_time)
