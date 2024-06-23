from collections import defaultdict


def exercise2(strings: str):
    tmp_dict = defaultdict(int)
    for char in strings:
        tmp_dict[char] += 1


    return tmp_dict

if __name__ == "__main__":
    print(exercise2("Baby"))
    print(exercise2("smiles"))
