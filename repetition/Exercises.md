

## Python exercise (mainly repetition)
Do these exercises if you feel a bit rusty of don't have much experience programming Python.

#### Before you start
In the following exercises you will create a small program for finding sequence matches (of a query sequence against a set of sequences). Start by creating a directory where you will write your code:
```
mkdir sequence_matcher
```

Now create a file `sequence_matcher.py` in this directory. In the following exercises, write all your code in this file.

#### Exercise 1 (if/else)

```python
query_sequence = "CCGCG"
reference_sequence = "ACCAGATCCACTACT"
````

Given the two variables above, write python code to check whether the query sequence is found within the reference sequence. Print "Match!" if is found and "No match!" if it is not found.

Hint: You can check whether a string is inside another string in python with the `in` operator, e.g. 
 ```python
 if some_string in other_string:
    # do something
```


#### Exercise 2 (functions)
Move the code from exercise 1 into a function. The function should take two parameters, a query string and a reference string, and return `True` if the query string can be found inside the reference sequence. Name the function `sequence_has_pattern`:

```python
def sequence_has_pattern(reference_sequence, query_sequence):
    # continue here, remember to return True/False in the end
```

Test your function, e.g. like this:
```python
result = sequence_has_pattern("ACTGAC", "AC")
print(result)  # This should print True if everything is correct
```


#### Exercise 3 (reading from file)
We now want to read a bunch of sequences from a file. Download [this file](https://raw.githubusercontent.com/ivargr/python-bioinformatics/master/repetition/sequences.txt) (tip: right click and select "save link as") and make sure you save it in the same folder that you write your Python script.

Each line in the file contains a sequence. 

Write Python code to read each line in the file. For each line, check if the query sequence "TTC" is found within the sequence on that line, by calling the `sequence_has_pattern` method you have created previously. If there is a match, print the whole sequence.


#### Exercise 4 (lists)

Create a function `read_sequences_from_file` that takes a file_name as parameter and that reads sequences from a the file (which is like like the file in exercise 3). All the sequences should be put into a list and the function should return that list.

Test your function like this:

```python
sequences = read_sequences_from_file("sequences.txt")
print(sequences)
```

#### Exercise 5 (find matches in a list of sequences)
Create a function `get_sequences_with_pattern` that takes a list of sequences (like the one returned by `read_sequences_from_file`) and a query sequence and that returns all the sequences that contains the pattern (query sequence).

#### Exercise 6 (command line tool)
Your program now has a lot of functions. We want to make this into a reusable program that you can run on the unix command line like this:

```bash
python3 program.py sequences.txt ACTG
```

In the command above we specify two arguments to the python program (the file name and the pattern we want to search for). We can read these arguments in our Python program like this:

```python
import sys
file_name = sys.argv[1]
query_sequence = sys.argv[2]
```

* Modify your code so that it reads a file name and query sequence from command line arguments. 
* Call the functions you have created, and print all the sequences that create a match (make sure nothing else is printed, use logging if you want to print anything else)


You can now test your Python program on the command line like this on the command line:

```bash
python3 program.py sequences.txt ACTG > matching_sequences.txt
```

Check that the file `matching_sequences.txt` now contains the sequences you would expect.

You now have your own small Python program for a specific purpose!



#### Exercise 7: Extra exercise
Do this one if you think the other exercises where too easy.

Modify your program so that the function `sequence_has_matches` takes a second parameter `number_of_allowed_mismatches`. The function should now return true if the pattern matches given the number of allowed mismatches. For instance, if allowed mismatches is 1, the query sequence "ACTG" should have a match in the sequence "ACCGTTT".

NB: We only take into consideration exact mismatches here (base pair substitutions), not deletions or insertions.




