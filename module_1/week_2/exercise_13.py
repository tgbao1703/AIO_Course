from typing import List

def exercise_13(number: int):
    var = 1
    while (number > 1):
        # Your code here
        var *= number
        number -= 1
    return var

if __name__ == "__main__":
    print(exercise_13(4))