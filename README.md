# Pairs Project

This project contains a function find_pairs that finds pairs of integers from a list that sum to a given value.

## How to run

The project requires python 3 to be installed on your system.

To run the script, open a terminal and navigate to the directory containing the script pairs.py.

Run the script with the command:

```bash

python find_pairs.py <numbers> <target>
```
Where <numbers> is a comma separated list of integers and <target> is the target integer.

For example:

```bash
python find_pairs.py 1,9,5,0,20,-4,12,16,7 12
```

This will return:
```bash

+ 5,7
+ 0,12
+ 16,-4

```

## Additional notes
The algorithm is efficient and correct, running in O(n) time.
The script also includes additional functions parse_numbers and handle_input_error for input validation and error handling.

### Todo

[ ] python find_pairs.py 1,9,5,0,20,-4,12,16,7 12
[ ] readable code
[ ] good unit tests
[ ] clean code

[ ] returning the correct results for all possible inputs
[ ] All edge cases should be handled appropriately
[ ] README file explaining how to run the code
