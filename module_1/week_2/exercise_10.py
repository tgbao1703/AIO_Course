

from typing import List


def exercise_10(integers: List[int], number: int = 1):
  return [element == number for element in integers]

if __name__ == "__main__":

    my_list = [1, 2, 3, 4]
    print(exercise_10(my_list, 2))
