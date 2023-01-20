import sys

def find_pairs(numbers, target):
    # Create an empty set to store the numbers
    num_set = set()
    # Create an empty list to store the pairs
    pairs = []

    # Iterate through the list of numbers
    for num in numbers:
        # Check if the current number's complement (target - num) is in the set
        if target - num in num_set:
            # If it is, add it to the pairs list
            pairs.append((num, target - num))
        else:
            # If not, add the current number to the set
            num_set.add(num)
    return pairs

if __name__ == '__main__':
    try:
        numbers = list(map(int, sys.argv[1].split(',')))
        target = int(sys.argv[2])
        print(find_pairs(numbers, target))
    except IndexError:
        print("Error: Please provide a list of numbers and a target as arguments. Example: python pairs.py 1,2,3,4 5")
