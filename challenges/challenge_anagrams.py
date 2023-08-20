def ana_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def is_anagram(first_string, second_string):
    first_string = first_string.replace(" ", "").lower()
    second_string = second_string.replace(" ", "").lower()

    if len(first_string) != len(second_string):
        return first_string, second_string, False

    first_list = list(first_string)
    second_list = list(second_string)

    ana_sort(first_list)
    ana_sort(second_list)

    return "".join(first_list), "".join(second_list), first_list == second_list
