def study_schedule(permanence_period, target_time):
    if target_time is None or any(
        start > end for start, end in permanence_period
    ):
        return None

    return sum(
        1 for start, end in permanence_period if start <= target_time <= end)
