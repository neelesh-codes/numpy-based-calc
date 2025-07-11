
if __name__ == "__main__":
    import numpy as np
    print("Welcome to this calculator")
    print("As you saw this calculator is writtent in numpy and python it will be super fast.")
    print("Now without wasting time let's start the app: ")

    name = input("Enter your name: ")
    preferd_name = input("Enter your name the app will call you: ")

    details = np.array([name, preferd_name])
    print(f"Real Name: {details[0]}")
    print(f"Preferd Name: {details[1]}")

