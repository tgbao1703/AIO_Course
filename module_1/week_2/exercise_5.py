def exercise5(N: int):
    list_of_numbers = []
    result = ""

    for i in range(1, 5):
        list_of_numbers.append(i)

    if N in list_of_numbers:
        result = "True"
    if N not in list_of_numbers:
        result = "False"

    return result
    
if __name__ == "__main__":
    N = 2
    results = exercise5(N)
    print(results)