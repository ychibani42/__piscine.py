import time


def getSecondsSinceEpoch():
    return time.time()


current_time = time.time()
time_tuple = time.localtime(current_time)


print("Seconds since January 1, 1970: " + f'{getSecondsSinceEpoch():,.4f}'
      + " or " + f'{getSecondsSinceEpoch():.2e}'
      + " in scientific notation\n" + time.strftime('%b', time_tuple) + " "
      + time.strftime('%d', time_tuple) + " "
      + time.strftime('%Y', time_tuple))
