

## Exercise on virtual environments and python packages

Note: Make sure you have done the [repetition exercise](../repetition) before you do this one. You will need the code from that exercise.


## Before you start
You can do these exercises either on your computer (if you have a unix shell) or on the UIO login nodes (`ssh yourusername@login.uio.no`). If you do them on the login nodes, and you did the previous exercise on your computer, you should move your code to your UIO home area first:
```
scp path/to/sequence_matcher yourusername@login.uio.no:.
```

The above command moves the folder `sequence_matcher` to your home area.


## Exercise 1: Create a virtual environment
Start by creating a virtual environment that you can install packages in. We will call it `sequence_matcher_environment`. You can create it wherever you want, but it can be nice to have it in the same directory as the code you wrote in part 1.

```bash
python3 -m venv sequence_matcher_environment
```

A new directory called `sequence_matcher_environment` should now have been created. Use a unix command to verify that the directory exists. This directory contains a full python installation. 

To activate this python installation, run:
```
source sequence_matcher_environment/bin/activate
```

Your command line prompt should now start with `(sequence_matcher_environment)` to indicate that this environment is active.

When you now use `python3`, you will use the Python from this environment. You can check this by using the unix command `which` to find out what `python3` is pointing to:

```
which python3
```

This will return a path, which should lead to somewhere inside your virtual environment directory.


## Exercise 2: Install a package inside your virtual environment
We want to install the package `pyfaidx`, which is a Python package for reading fasta files.

Run the appropriate commands for installing the package. Look at the lecture slides if you are unsure what command to run.

Try uninstalling `pyfaidx` and then installing it again. Run the command `python3 -m pip list` before and after uninstalling to list all the packages you have installed.

## Exercise 3: Turn your own code into a package
Copy the following code and paste it into a file `setup.py` inside the directory where you wrote `sequence_matcher.py`:

```python
from distutils.core import setup

setup(name='SequenceMatcher',
      version='1.0',
      description='A package for detecting patterns in sequences',
      author='Your Name',
      author_email='username@uio.no',
      py_modules=['sequence_matcher'],
      install_requires=["pyfaidx"]
      )
```

Feel free to change any of the information (name, email, description).

Now, install your package (remember to be positioned in the same directory):

```
python3 -m pip install -e .
```

Verify first, by listing all Python packages, that the package is installed:

```
python3 -m pip list
```

Also, verify that you now can use this package from anywhere:
```
# First go somewhere else
cd ~
# Start a python shell
python3
```
Inside the python shell, try to import a function from your package:
```
from sequence_matcher import read_sequences_from_file
```

If nothing happens, it means the import went fine and everything is working.


## Exercise 4: Extending your package
We now want to extend our sequence matcher to be able to find matches on a real reference genome. In order to do that, we will use python package `pyfaidx` to read sequences from a reference genome (in a fasta file).

* Start by downloading [this fasta file](hg19_chr20.fasta?raw=true) which contains chr20 on the hg19 reference genome.
* Test that pyfaidx is working by opening an interactive Python shell (just type `python3` in the same directory that you have the hg19_chr20.fasta file).

Do the following in the interactive python shell: 
```python
# Import Fasta from the pyfaidx package
from pyfaidx import Fasta
# make a reference object
reference = Fasta("hg19_chr20.fasta")

# Try extracting a sequence (choose any region)
print(reference["20"][100000:100010])
```

In the code above, we access the chromosome 20 by indexing `reference` by 20. We then extract a sequence by indexing again using "slicing" (`[from:to]`). Play around with this in the interactive shell until you feel comfortable with extracting sequences.

Make a new function `region_has_pattern` in sequence_matcher.py. The function should take four arguments:
* A fasta file name (e.g. hg19_chr20.fasta)
* A chromosome
* A start position
* An end position
* A query sequence (pattern) that we want to check whether is found within the region or not

You can use this code skeleton:
```python
def region_has_pattern(fasta_file_name, chromosome, start, end, query_sequence):
    # step 1: extract the region from the fasta file using pyfaidx
    # remember to have imported Fasta from pyfaidx in the top of your python file
    # step 2: check whether the query sequence is found within this region or not
    # return True/False
```


