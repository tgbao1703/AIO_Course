from typing import List


def exercise9(n: List[int]):
    max_value = n[0]

    for i in range(1, len(n)):
        if n[i] > max_value:
            max_value = n[i]

    return max_value


if __name__ == "__main__":
    my_list=[1 , 9 , 9 , 0]
    print(exercise9(my_list))
