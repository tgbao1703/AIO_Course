from typing import List

def exercise_11(list_nums: List[int] = [0, 1, 2]):
    var: int = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)

if __name__ == "__main__":
    print(exercise_11())