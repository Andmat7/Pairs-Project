# Pairs Project

This project contains a function find_pairs that finds pairs of integers from a list that sum to a given value.

## How to run

The project requires python 3 to be installed on your system.

To run the script, open a terminal and navigate to the directory containing the script pairs.py.

Run the script with the command:

```bash

python pairs.py <numbers> <target>
```
Where <numbers> is a comma separated list of integers and <target> is the target integer.

For example:

```bash
python pairs.py 1,9,5,0,20,-4,12,16,7 12
```

This will return:
```bash
[(12, 0), (5, 7), (16, -4)]
```

## Input validation

The script validates the input and returns an error message if invalid input is provided. The input must be a string of comma separated integers followed by an integer.
Evaluation

The algorithm is efficient and correct, running in O(n) time.
## Additional notes

The script also includes additional functions parse_numbers and handle_input_error for input validation and error handling.




```
> app 1,9,5,0,20,-4,12,16,7 12
​
+ 12,0
+ 5,7
+ 16,-4
​
```
### Todo
[ ]readable code
[ ] Your app doesn't need to have identical input/output mechanisms.

[ ]you could read from a file instead of the command line.
[ ]good unit tests
[ ]clean code

[ ] returning the correct results for all possible inputs
[ ]Any assignment that doesn't return the correct answer for the sample input
above will fail.
[ ]You can assume that all input values are integers. 
[ ] You can assume that there aren't any repeat values in the list.
[ ]All edge cases should be handled appropriately
[ ] clean and readable code
[ ]README file explaining how to run the code
