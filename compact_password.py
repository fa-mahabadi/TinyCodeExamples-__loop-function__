from collections import Counter


def compact_password(str_prev):
    while True:
        str_current = []
        count = Counter(str_prev)
        for k, v in count.items():
            if int(v) > 1:
                str_current.append(str(v))
            str_current.append(k)
        str_current.sort()
        if str_current == str_prev:
            print(f'Compact password: {"".join(str_current)}')
            break
        str_prev = str_current


str_prev = input("enter number: ")
compact_password(str_prev)
