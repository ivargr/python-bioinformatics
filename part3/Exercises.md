

## Exercise on virtual environments and python packages

This exercise build on the code you wrote for computing GC-content. We will now make that program into a Python package that can be easily re-used.


## Before you start
You can do these exercises either on your computer (if you have a unix shell, git-bash or similar) or on the UIO login nodes (`ssh yourusername@login.uio.no`). If you do them on the login nodes, and you did the previous exercise on your computer, you should move your code to your UIO home area first:
```
scp path/to/dna_analyser yourusername@login.uio.no:.
```

The above command moves the folder `dna_analyser` to your home area.


## Exercise 1: Create a virtual environment
Start by creating a virtual environment that you can install packages in. We will call it `dna_analyser_environment`. You can create it wherever you want, but it can be nice to have it in the same directory that you have the `gc_content.py` file.

```bash
python3 -m venv dna_analyser_environment 
```

A new directory called `dna_analyser_environment` should now have been created. Use the unix command `ls` to verify that the directory exists. This directory contains a full python installation. 

To activate this python installation, run:
```
source dna_analyser_environment/bin/activate
```

**NOTE** If you are windows using gitbash, the command is slightly different:
```
source dna_analyser_environment/Scripts/activate
```


Your command line prompt should now start with `(dna_analyser_environment)` to indicate that this environment is active. In gitbash, the text will show above the line.

When you now use `python3`/`python`, you will use the Python from this environment. You can check this by using the unix command `which` to find out what `python3`/`python` is pointing to:

```
which python3
# .. or which python
```

This will return a path, which should lead to somewhere inside your virtual environment directory.


## Exercise 2: Install a package inside your virtual environment
We want to try to install the package `pyfaidx`, which is a Python package for reading fasta files.

Run the appropriate commands for installing the package. Look at the lecture slides if you are unsure what command to run.

Try uninstalling `pyfaidx` and then installing it again. Run the command `python3 -m pip list` before and after uninstalling to list all the packages you have installed.

## Exercise 3: Turn your own code into a package
Copy the following code and paste it into a file `setup.py` inside the directory where you wrote `gc_content.py`:

```python
from distutils.core import setup

setup(name='DnaAnalyser',
      version='1.0',
      description='A package for various DNA-analyses',
      author='Your Name',
      author_email='username@uio.no',
      py_modules=['gc_content'],
      install_requires=["pyfaidx"]
      )
```

Feel free to change any of the information (name, email, description).

Now, install your package (remember to be positioned in the same directory) by running the following command:

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
# or use python if that is the command you are using to run pytyhon 3 
```
Inside the python shell, try to import a function from your package:
```
from gc_content import compute_gc_content 
```

If nothing happens, it means the import went fine and everything is working.


## Exercise 4: Extending your package
We now want to extend our program so that we can compute the GC content on a segment of a real reference genome. In order to do that, we will use python package `pyfaidx` to read sequences from a reference genome (in a fasta file).

* Start by downloading [this fasta file](hg19_chr20.fasta?raw=true) (right click and click save link as) which contains chr20 on the hg19 reference genome.
* Test that pyfaidx is working by opening an interactive Python shell (just type `python3` in the same directory that you have the hg19_chr20.fasta file).

Try to do the following in an interactive python shell (which you get by just typing python/python3 in the terminal):
```python
# Import Fasta from the pyfaidx package
from pyfaidx import Fasta
# make a reference object
reference = Fasta("hg19_chr20.fasta")

# Try extracting a sequence (choose any region)
print(str(reference["20"][100000:100010]))

```

In the code above, we access the chromosome 20 by indexing `reference` by 20. We then extract a sequence by indexing again using "slicing" (`[from:to]`). Play around with this in the interactive shell until you feel comfortable with extracting sequences.

Make a new function `compute_gc_content_in_region` in gc_content.py. The function should take four arguments:
* A fasta file name (e.g. hg19_chr20.fasta)
* A chromosome
* A start position
* An end position

You can use this code skeleton:
```python
def compute_gc_content_in_region(fasta_file_name, chromosome, start, end):
    # step 1: extract the region from the fasta file using pyfaidx
    reference = Fasta(fasta_file_name)
    region_dna = str(reference[chromosome][start:end])
    # remember to have imported Fasta from pyfaidx in the top of your python file

    # step 2: compute the GC content by calling the function compute_gc_content on region_dna
    # remember to return the gc-content in the end
```


## Exercise 5
In the previous exercises, your program took an argument from the command line representing either a sequence (if you did the easy exercises) or a file name (if you did the difficult exercises). We now want to change the python script so that a fasta file name (e.g. hg19_chr20.fasta) is the first argument, a chromosome is the second, a start position is the third and an end position is the fourth argument. Then, we want to call the function `compute_gc_content_in_region` using that information and print the GC content of that region.

For instance, we would be able to run this on the command line:
```
python3 gc_content.py hg19_chr20.fasta 20 2000000 2000020
``` 

Do the necessary changes to your program to make this work.

Note that since the fasta file only contains chromosome 20, pyfaidx will crash if you try to pick out a region outside chromosome 20.


## Exercise 6: Run your tool from anywhere
You now have a command line tool, but you will need to run the exact python-file everytime you want to use it. You will typically use a tool like this in a pipeline, and then it is a bit of a hassle to always remember to specify the exact path to the python file.

We can make our tool even easier to use by giving it a separate command line command.

Change setup.py by adding the following lines inside the function call to `setup`:
```
entry_points = {
        'console_scripts': ['funniest-joke=funniest.command_line:main'],
    }
```

Your setup.py file should then look something like this:
```


from distutils.core import setup

setup(name='DnaAnalyser',
      version='1.0',
      description='A package for various DNA-analyses',
      author='Your Name',
      author_email='username@uio.no',
      py_modules=['gc_content'],
      install_requires=["pyfaidx"],
      entry_points = {
            'console_scripts': ['gc_content=gc_content:main'],
        }
)
```

The `gc_content=gc_content:main` line tells Python to create a command `gc_content`. When that command is run in the terminal, the function `main` inside the file `gc_content.py` should be run. We don't have a function called `main` now, so create a function main in gc_content.py:

```
def main():
    print("Hi")  # we will change this soon
```

We need to uninstall our package and install it again for the system to register the new command:

```
python3 -m pip uninstall DnaAnalyser
python3 -m pip install -e .
```

Now, try typing `gc_content` in the terminal. You should see "hi" printed.


We now want all the code which is under `if __name__ == "__main__"` to instead be inside the main-function. Simply remove the `if __name__ ...` line and move the code inside the main function. 

Try running `gc_content hg19_chr20.fasta 20 100 200` now. You should be able to run this command from anywhere on your system (just make sure you have the path to hg19_chr20.fasta correct).



### A few notes in the end
You now know how to turn a small Python script into an actual program that you can run on the command line. This is a very useful techinique if you are making lots of Python scripts for performing small tasks. Often, these scripts end up lying around never to be used again. Now, you can instead make sure these scripts are of high quality, and make them into command line tools so that you can use them again in various projects. This means that Python can be a powerful tool in your bioinformatics toolkit.
