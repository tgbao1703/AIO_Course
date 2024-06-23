from typing import List

def function_helper(x: int, data: List[int]):
    for i in data:
        # Your code here
        # Neu x == i thi return 0
        if x == i:
            return 0
    return 1

def exercise_16(data: List[int]):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res

if __name__ == "__main__":
    lst = [9, 9, 8, 1, 1]
    print(exercise_16(lst))