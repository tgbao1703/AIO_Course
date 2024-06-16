from typing import List


def exercise8(n: List[int]):
    min_value = n[0]

    for i in range(1, len(n)):
        if n[i] < min_value:
            min_value = n[i]

    return min_value


if __name__ == "__main__":
    my_list=[1, 2, 3, -1]
    print(exercise8(my_list))
