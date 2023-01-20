import sys
def getParamsFromTerminal():
    numbers = set(map(int, sys.argv[1].split(',')))
    target = int(sys.argv[2])
    return numbers,target

def format_pairs(pairs):
    formatted_pairs = ""
    for pair in pairs:
        formatted_pairs += "+ " + ",".join(map(str, pair)) + "\n"
    return formatted_pairs    