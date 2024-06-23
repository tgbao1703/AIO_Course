from typing import List

def exercise_12(n: List):
    return [element % 3 == 0 for element in n]


if __name__ == "__main__":
    print(exercise_12([1 , 2 , 3 , 5 , 6]))