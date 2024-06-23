from typing import List


def exercise6(data: List, max: float, min: float):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result

if __name__ == "__main__":
    my_list = [10, 2, 5, 0, 1]
    max = 2
    min = 1

    print(exercise6(max=max, min=min, data=my_list))
