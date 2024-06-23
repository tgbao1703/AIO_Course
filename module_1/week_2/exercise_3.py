from collections import defaultdict

def exercise3(file_path):
    counter = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                counter[word] += 1
    return counter


if __name__ == "__main__":
    file_path = "module_1\\week_2\\P1_data.txt"
    result = exercise3(file_path)
    print(result["man"])

