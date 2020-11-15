# Exercises (DNA analyser)
Do these if you found the friday exercises a bit difficult.

### Introduction
In these exercises we are making a small Python tool for analysing DNA sequences. We will, for instance, write code for computing the GC content in a string of DNA and counting the number of certain nucleotides. We will call our tool `dna_analyser`.

Start by making a new directory called `dna_analyser` somewhere on your computer or on your UIO home area:

```
mkdir dna_analyser
```

Make a new file called `gc_content.py` inside this directory (you make more files in the same direcotry later)

Remember that you should be positioned inside this directory in the terminal when you run your Python code.


### Exercise 1: Counting nucleotides
In the following exercises, write all your code in the `gc_content.py` file.

As an example, we now want to work with the DNA sequence `AACCTGGG`.

**a)** Store this sequence in a variable in Python. You can name your variable `sequence`.

**b)** Write code for finding the number of G's and C's in the sequence. Remember that you can count the number of occurences of a substring in a string with:

```
number_of_occurences = sequence.count("some substring")
```

Print the number of G's and C's and check that the numbers are correct.



<details>
    <summary>
    View hint/solution
    </summary>

```python
# We create a string containing our sequence and store it in a variable
sequence = "AACCTGGG"
# You can count the number of Gs in a string like this:
n_g = sequence.count("G")
# The variable nG now contains the number
print(n_g)
# We do the same again for C
n_c = sequence.count("C")
print(n_c)
```
</details>


### Exercise 2: Computing GC-content
GC-content for a sequence is defined as the number of Gs and Cs divided by the sequence length. E.g., if half of the sequence contains G or C, then the GC content should be 0.5.

Continue writing your code in the same file, below the code you wrote in Exercise 1.

**a**) Find the length of your sequence by using the `len` function. Print the length and check that it is correct.

**b**) Compute the GC-content and store it in a variable. Print the GC-content and manually verify that the number is correct.

<details>
<summary>View hint/solution</summary>
```python
length_of_sequence = len(sequence)
gc_content = .... write the formula here ....
print("The GC-content is", gc_content)
```
</details>


### Exercise 3: Make a function for computing the GC content
**a)** Put the code from exercise 1/2 inside a function. Name the function `compute_gc_content`. It should take one argument `sequence` and return the GC-content.

You can use this skeleton code:
```
def compute_gc_content(sequence):
    # compute the gc content here
    # return the gc-content (change the dots)
    return ..... 
```

**b)** Test your function by *calling* the function with a sequence, e.g. like this:
```
some_sequence = "AACC"
result = compute_gc_content(some_sequence)
print(result)
```


### Exercise 4: Make a command line tool
Before you continue, make sure your code looks something like this:
<details>
    <summary>View solution (do not view before you have tried yourself)</summary>
    
```python

def compute_gc_content(sequence):
    n_c = sequence.count("C")
    n_g = sequence.count("G")
    length = len(sequence)
    gc_content = (n_c + n_g) / length
    return gc_content

sequence = "AACCTGGG"
result = compute_gc_content(sequence)
print("Gc content is ", result)
```
    
</details>


You now have code for computing the GC-content for a specific sequence. But we don't want to go in an edit the code every time we want to compute the GC-content for a new sequence. Instead, it would be very nice to be able to run the Python script from the command line and specify the sequence we want to analyse. We can do this by using command line arguments.

First import `sys` in the top of your file. This gives us access to reading the command line arguments:

```python
# Include this line in the top of your file
import sys
```

Instead of having your sequence defined in your code like this:
```python
sequence = "AACCTGGG"
```
... we now want to read the sequence from the first command line argument:
```python
sequence = sys.argv[1]
```

Do this change, and try running your Python program by specifying a sequence as the first argument:

```python
python3 gc_content.py GCA
```
Note: You may use `python` instead of `python3` depending on your environment.

Try running your tool a few times with different sequences to see that it works.


### Exercise 5: A few improvements
We now allow any sequence to be specified. Try for instance running your tool with the sequence `XYZ` and see what happens.

It is a good idea to always validate user input. This way, mistakes in a pipeline (e.g. another tool that outputs invalid sequences) can be detected as early as possible.

Define a new function `sequence_is_valid` that takes a sequence as argument and returns `True` if the sequence is valid DNA and `False` if not.

This function is a bit complicated to write, since you need to check whether every base is valid. Here is a way to do that:
* Make a for-loop where you iterate over each letter in the sequence
* For each letter (nucleotide), check if it is either equal to A, C, T or G (you can also include N)
* If it is equal, do nothing
* If it is not equal, return False
* In the end, after the for-loop is done, return True (this way we return True if all the letters are valid

 

<details>
    <summary>View solution (do not view before you have tried yourself)</summary>
    
```python
def sequence_is_valid_dna(sequence):
    for base in sequence:
        if base is not "A" and base is not "C" and base is not "G" and base is not "T" and base is not "N":
            return False
            
        return True
```
    
</details>


After writing the function, change your code so that the program first checks if the sequence from the command line is valid. If it is not valid, print a message to the user describing that the sequence is not valid. If it is valid, continue computing the GC-content like before.



