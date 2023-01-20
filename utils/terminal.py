import sys
def get_params_from_terminal():
    numbers = set(map(int, sys.argv[1].split(',')))
    target = int(sys.argv[2])
    return numbers,target

def format_pairs(pairs):
    formatted_pairs = "\n"
    for pair in pairs:
        formatted_pairs += "+ " + ",".join(map(str, pair)) + "\n"
    return formatted_pairs

def print_pairs(pairs):
    print(format_pairs(pairs))


def show_error_terminal():
    print("Error: Please provide a list of numbers and a target as arguments. Example: python pairs.py 1,2,3,4 5")