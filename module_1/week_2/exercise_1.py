from typing import List


def exercise1(origin_lst: List[int], k: int):

    return [ max(origin_lst[i:i+k]) for i in range(len(origin_lst)-k+1) ]

if __name__ == "__main__":
    print(exercise1([3 , 4 , 5 , 1 , -44] , 3) )
    print(exercise1([3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1] , 3) )
