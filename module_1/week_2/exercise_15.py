from typing import List

def function_helper(x: int):
    return 'T' if x > 0 else 'N'

def exercise_15(data: List[int]):
    res = [function_helper(x) for x in data]
    return res

if __name__ == "__main__":

    data = [2, 3, 5, -1]
    print(exercise_15(data))