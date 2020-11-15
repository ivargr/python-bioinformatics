#Exercises
Do these if you found the friday exercises okay.

### Exercise 1
Start by doing all the [easy exercises](Exercises2.md). The rest of the exercises here build
on that code. In the following exercises, we want to extend the program created in the previous exercises so that we can compute the GC-content on many sequences.

### Exercise 2: Read sequences from a file.

Change the program so that instead of taking a sequence from the command line, you take a file name. Instead of computing the GC-content for a single sequence, go through the lines in the file (there is one sequence on each line) and compute the GC content for every sequence. For every sequence, print the sequence, a space, and then the GC-content for that sequence.

<details>
<summary>Click to see a hint on how to solve this exercise</summary>

Remember that you can open a file like this:
```
file = open("filename.txt")
```
.. and that you can iterate over the files using a for loop:
```
for line in file:
    # line is now a variable pointing to a line in the file
    # It is often a good idea to strip the line (remove newline character at the end)
    line = line.strip()
```
</details>


### Exercise 3
If we want to re-use the function `compute_gc_content` in other Python script, we can import the function from this file.

Create a file `test.py` in the same directory.

In the top of the file, insert this line in order to import the function:

```
# Import the function from gc_content
from gc_content import compute_gc_content
```

Try to run test.py now. Your program will most likely crash, and you will notice that  all the code from `gc_content.py` is running when importing the file.

That is not ideal, since we want to be able to import the function `compute_gc_content` without ending up with running all the code in that file.

This can be solved by putting the code we don't want to run inside an if-test that checks whether or not this file is being imported or being run as a python script:

```
if __name__ == "__main__":
    # Code inside here will not run if we import this file
```

Change the file `gc_content.py` so that all the code that reads commmand line arguments and so on is inside an if-clause like the one above. Only the function `compute_gc_content` and imports should be outside.

Now run test.py again and check that it doesn't crash. Try to call the function `compute_gc_content` from test.py and check that it works.

If everything works, it means you now have created a function that you can re-use in other Python scripts. In the next part of this course, we'll see how we can make your program into a package so that it is even easier to re-use it.
