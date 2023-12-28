import sys


def probability_of_attendance(
        prev_attendance, curr_attendance,
        missing_attendance, number_of_days, attendance, miss_flag):
    """"
    This function is updating the  number_of_ways_to_attend_classes and probability_to_miss_gradution_ceremony
        on the basis of inputs.
        Parameters:
            prev_attendance: str
            curr_attendance : str
            missing_attendance: int
            number_of_days: int
            attendance : int
            miss_flag : Boolean
        Return: None
    """
    global number_of_ways_to_attend_classes
    global probability_to_miss_gradution_ceremony

    if missing_attendance >= 4:
        miss_flag = True
        return

    if number_of_days == attendance:
        attendance_str = prev_attendance + curr_attendance
        if miss_flag:
            return
        if curr_attendance == 'A':
            probability_to_miss_gradution_ceremony += 1
        number_of_ways_to_attend_classes += 1
        return

    probability_of_attendance(prev_attendance=prev_attendance+curr_attendance, curr_attendance="P",
                              missing_attendance=0, number_of_days=number_of_days+1,
                              attendance=attendance, miss_flag=miss_flag)
    probability_of_attendance(prev_attendance=prev_attendance+curr_attendance, curr_attendance="A",
                              missing_attendance=missing_attendance+1, number_of_days=number_of_days+1,
                              attendance=attendance, miss_flag=miss_flag)
    return

if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
        print("Number of days is {}".format(days))
        prev_attendance = ''
        curr_attendance = ''
        missing_attendance = 0
        number_of_days = 0
        number_of_ways_to_attend_classes = 0
        probability_to_miss_gradution_ceremony = 0

    except IndexError:
        print("Please pass 'days' argument in command line")
    except ValueError:
        print("'Days' argument must be of integer type")
    except Exception as e:
        print(e)
    else:
        probability_of_attendance(prev_attendance, curr_attendance,
                                  missing_attendance, number_of_days, days, False)
        print("Number of ways to attend classes over {} days is {}".format(days, number_of_ways_to_attend_classes))
        print("probability to miss graduation ceremony is {}".format(probability_to_miss_gradution_ceremony))
        print("output", str(probability_to_miss_gradution_ceremony) + '/' + str(number_of_ways_to_attend_classes))

