def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if any(
        not isinstance(start, int) or not isinstance(end, int) or start > end
        for start, end in permanence_period
    ):
        return None

    return sum(
        1 for start, end in permanence_period if start <= target_time <= end
    )
