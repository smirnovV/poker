def get_result(cards):
    values = [card[0: -1] for card in cards]
    s = len(set([card[-1] for card in cards])) == 1

    val = list(set(values))

    if len(set(cards)) != 5:
        raise Exception('Одинаковые карты')

    if s and (set([int(card) - int(min(values)) for card in values]) == {0, 1, 2, 3, 4}):
        return 8
    elif len(val) == 2 and (values.count(val[0]) == 4 or values.count(val[1]) == 4):
        return 7
    elif len(val) == 2 and (values.count(val[0]) == 3 or values.count(val[1]) == 3):
        return 6
    if s:
        return 5
    if set([int(card) - int(min(values)) for card in values]) == {0, 1, 2, 3, 4}:
        return 4
    elif len(val) == 3 and (values.count(val[0]) == 2 or values.count(val[1]) == 2 or values.count(val[2]) == 2):
        return 2
    elif len(val) == 2 or len(val) == 3:
        return 3
    elif len(val) == 4:
        return 1
    return 0


if __name__ == '__main__':

    print(get_result(["07s", "09s", "08s", "10s", "11s"]))  # 8
    print(get_result(["07h", "07d", "07c", "07s", "11s"]))  # 7
    print(get_result(["07h", "11d", "07c", "07s", "11s"]))  # 6
    print(get_result(["07s", "09s", "08s", "02s", "11s"]))  # 5
    print(get_result(["07h", "08d", "09c", "06s", "10s"]))  # 4
    print(get_result(["07h", "09d", "09c", "09s", "11s"]))  # 3
    print(get_result(["07h", "09d", "09c", "07s", "11s"]))  # 2
    print(get_result(["07h", "09d", "05c", "07s", "11s"]))  # 1
    print(get_result(["07h", "09d", "05c", "03s", "11s"]))  # 0
    try:
        print(get_result(["09d", "09d", "05c", "03s", "11s"]))  # except
    except Exception:
        print("success")
