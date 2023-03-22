def validate_period(list):
    for tupla in list:
        if type(tupla[0]) != int or type(tupla[1]) != int:
            return False

    return True


def study_schedule(permanence_period, target_time):
    if type(target_time) == int and validate_period(permanence_period):
        count = 0
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                count += 1

        return count

    return None
