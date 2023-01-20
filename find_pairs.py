from utils.terminal import format_pairs, getParamsFromTerminal

def find_pairs(numbers_list, target):
    without_complement = set() # A set to collect the numbers that do not have a partner
    pairs = set() # to collect all pairs that match the target sum.

    for num in numbers_list:
        # Check if the current number's complement (target - num) is in the set
        complement = target - num
        if complement in without_complement:
            # If it is, add it to the pairs set
            pair = frozenset({num, complement})
            pairs.add(pair)
        else:
            # If number is not matched, add it to the unmatched numbers
            without_complement.add(num)
    return pairs

try:
    numbers, target = getParamsFromTerminal()
    print(format_pairs(find_pairs(numbers, target)))
except IndexError:
    print("Error: Please provide a list of numbers and a target as arguments. Example: python pairs.py 1,2,3,4 5")
