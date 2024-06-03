import random
import math
from typing import Any

def exercise3(num_samples: Any, loss_name: str):

    if not num_samples.isnumeric() or int(num_samples) <= 0:
        print("Number of samples must be an integer number greater than 0")
        return

    num_samples = int(num_samples)

    predict = [random.uniform(0, 10) for _ in range(num_samples)]
    target = [random.uniform(0, 10) for _ in range(num_samples)]

    print(f"Loss name: {loss_name}")
    print(f"Number of samples: {num_samples}")

    loss = 0

    for i in range(1,num_samples):
        loss = calculate_loss(i, target[:i], predict[:i])
        print(f"Sample-{i}: predict = {predict[i]}, target = {target[i]}")
        print(f"loss: {loss}")

    loss = calculate_loss(num_samples, target, predict)
    print(f"Sample-{num_samples}: predict = {predict[-1]}, target = {target[-1]}")
    print(f"Final loss: {loss}")

def calculate_loss(num_samples, predict, target):
    match loss_name:
        case 'MAE':
            return sum(abs(t - p) for t, p in zip(target, predict)) / num_samples
        case 'MSE':
            return sum((t - p) ** 2 for t, p in zip(target, predict)) / num_samples
        case 'RMSE':
            return math.sqrt(sum((t - p) ** 2 for t, p in zip(target, predict)) / num_samples)
        case _:
            return 0


if __name__ == "__main__":
    num_samples = input("Input number of samples ( integer number ) which are generated : ")
    loss_name = input("Enter loss name (MAE, MSE, RMSE): ")
    exercise3(num_samples, loss_name)
