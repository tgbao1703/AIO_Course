import math

def sigmoid(x: int|float):
    return 1/(1 + math.exp(-x))

def relu(x: int|float):
    return 0 if x <= 0 else x

def elu(x: float, alpha: float = 0.01):
    return alpha*(math.exp(x) - 1) if x <= 0 else x

def activations():
    dict_map = {"sigmoid": sigmoid,
                "relu": relu,
                "elu": elu}

    x = input("Input x = ")

    if not is_number(x):
        print("x must be a number")
        return

    type = input("Input activation Function ( sigmoid | relu | elu ) ")

    if func := dict_map.get(type):
        print(f"f({x}) = {func(float(x))}")
        return

    print(f"function {type} dose not support")

def is_number(n) :
    try :
        float(n) # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True

if __name__ == "__main__":

    activations()
