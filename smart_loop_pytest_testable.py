
#refactored by perplexity for pytest testability


def get_int(input_func=input, prompt="What's x? "):
    while True:
        try:
            return int(input_func(prompt))
        except ValueError:
            print("x is not an integer")

def main():
    x = get_int()
    print(f"x is {x}")













# def get_int(input_func=input, prompt="What's x? "):
#     while True:
#         try:
#             value = input_func(prompt)
#             x = int(value)
#             return x
#         except ValueError:
#             print("x is not an integer")

# def main():
#     x = get_int()
#     print(f"x is {x}")


