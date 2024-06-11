def score(dice):
    result_points = 0
    count_dict = {}

    for elem in dice:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1

    for num, count in count_dict.items():
        if num == 1:
            result_points += (count // 3) * 1000 + (count % 3) * 100
        elif num == 5:
            result_points += (count // 3) * 500 + (count % 3) * 50
        else:
            result_points += (count // 3) * num * 100

        return result_points
