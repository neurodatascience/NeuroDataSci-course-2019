# Introduction to Python

The structure of this morning will be as follows:

- An overview of structures and datatypes in Python programming:
  - Python and IPython shells
  - Variables, types, comparisons
  - Logic, looping, and functions
  - Scripts, debugging, and file access
- An exercise in loading data the "*hard way*":
  - Download [the Boston Housing dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data) and [its column names](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.names)
  - Loading and interpreting data (***without*** libraries)
- Introduction to Data Science in Python:
  - Libraries and the scientific Python ecosystem
  - Loading data the easy way
  - Walking through an analysis

### Overview of Python

**Requirements**: Python, IPython

Flow:
- Open the Python shell
- Declare a simple variable or two (i.e. `a = 2`)
- Compare variables
- Try seeing what we did with "history," realize we should switch to IPython
- Demonstrate `history`, `ls`, and other useful things
- Redo the same thing, change the datatypes, keep comparing
- Introduce lists, loop over values
- Make decisions based on values in list
- Write a function containing the loop with conditional
- Move that into a script
- Introduce the debugger
- Write "results" to a file


### Loading data the *hard way*

**Requirements**: Python, IPython, [the Boston Housing dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data) and [its column names](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.names)

Flow:
- Create an empty script
- Find where your data file is on disk and write a command to open it
- Print its contents
- Determine how your data should be split/parsed
- Discuss plan for separating the values
- Demonstrate string splitting and stripping
- Discuss casting and datatypes
- Introduce try-except blocks
- Pick "some" method for storing the rows of data (likely list-of-lists)
- Load the header data now and agree this format is annoying/not convenient
- Introduce dictionaries and use them instead
- Agree there must be a better way
- Take a break and wait for your day to be saved in the next section :)


### Introduction to Data Science in Python

- (P; 20 min; live coding) Libraries and the scientific python ecosystem
- (P; 10 min; live coding) Better data management, quick solution w/ pandas
* load an image with nifti (nibabel)
* load an atlas (nilearn)
* extract phenotypic data (pandas)
* use statsmodel to do an anova
* visualize a slice (matplotlib)
* Compute the sum of square (numpy)
* compute the correlation matrix from the ROI (nilearn)

