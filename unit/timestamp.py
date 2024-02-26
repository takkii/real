import datetime
import gc
import re
import threading


def main():
    try:
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        day = int(datetime.datetime.now().day)

        st_year = str(datetime.datetime.now().year)
        st_month = str(datetime.datetime.now().month)
        st_day = str(datetime.datetime.now().day)

        two_month = bool(re.fullmatch("^[2]$", str(month)))
        eleven_month = bool(re.fullmatch("^[11]$", str(month)))

        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if two_month:
                calc = ((365 * year + year / 4 - year / 100 + year / 400 +
                         (306 * (month + 1)) / 10 + day) - 426) % 7
            elif eleven_month:
                calc = ((365 * year + year / 4 - year / 100 + year / 400 +
                         (306 * (month + 1)) / 10 + day) - 427) % 7
            else:
                calc = ((365 * year + year / 4 - year / 100 + year / 400 +
                         (306 * (month + 1)) / 10 + day) - 428) % 7
        else:
            calc = (year + year / 4 - year / 100 + year / 400 +
                    (13 * month + 8) / 5 + day) % 7

        week = ["Sun", "Mon", "Tues", "Wedness", "Thurs", "Fri", "Satur"]
        cl_wk = week[int(calc)]

        print(st_year + "/" + st_month + "/" + st_day + " : " + cl_wk + "day")

    # Custom Exception.
    except ValueError as ext:
        print(ext)
        raise RuntimeError from None

    # Once Exec.
    finally:
        # GC collection.
        gc.collect()


# Thread call, list.
class time_stamp(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def start(self):
        main()


Thread = time_stamp()
start = Thread.start()
