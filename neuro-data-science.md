
Title : Fundamentals in Neuro Data Science
===========================================

Key words: teaching, mcgill, open data science, neuroscience

Syllabus:
-----------

Neuroscientists rely increasingly on data accessible online and on data science
procedures for their investigations. Data science now offers a key set of
tools and methods to efficiently analyse, visualize and interpret neuroscience
data. Concurrently, there is a growing concern in the life sciences that many
results produced are difficult or even impossible to reproduce. This is
referred to as the reproducibility crisis, which concerns most of biomedical
fields [F. Collin]. 

This first week of the computational neuroscience seminar series is bringing
together software and analytical tools and methods.  It will teach students how
to best use the fundamentals of data science in their daily work to produce
reproducible results. We will take examples in neuroimaging or imaging
genetics, and see how to use computational tools, statistical and machine
learning techniques, and collaborative and open science methodology to generate
results that are statistically solid and computationally reproducible. While a
large part of this course is language agnostic, we will teach and use python
throughout the course. Students will start to work on projects that they will
continue during the following  computational neuroscience seminar weeks.

The course will require that you have some basic programming experience and some
notion of statistical analysis, but will be aimed at life scientists
(neurologists, psychiatrists, pyschologists, neuroscientists) who wish to
improve their research practices, or students who want an introduction to
data science with examples in neuroscience and neuroimaging. We will strive to avoid
the classic problem described in Figure 1. 


~~~~~~~~~~~~~~~~~~~
Monday May 6th
~~~~~~~~~~~~~~~~~~~
 
[Part I: Introduction]

Introduction to the course: (1h PB / JB)
-------------------------------------------
	- Code of conduct
	- logistics
	- Let us know what you know 
	- Motivation
	- Objectives
	- Content
	- Evaluation

Lesson 1: Epistemiology and lesson from the past (2h JB / ?)
-----------------------------------------------------------------
	- A word on Popper and Khun
		* falsifiability
		* what makes a scientific revolution ?
		* lessons for today's neuroscience
	- Reproducibility issues in biology and neuroscience

Discussion and lunch (1h)
---------------------------

[Part II: The computational tools]

Lesson 2: Computational Basics : shell and git (3h JB + PB ?)
-----------------------------------------------------------------
	- Know your shell
	- Know your editor
	- Git: understand the model
		* How to Never lose anything 
		* How do I best collaborate with myself?

~~~~~~~~~~~~~~~~~~~
Tuesday May 7th
~~~~~~~~~~~~~~~~~~~

Lesson 3: Computational Basics : python for programmers (3h JB + ED / ... ? )
-----------------------------------------------------------------------------
	- Why Python : a software glue
	- Python key data structure
	- Beyond simple python: class, decorators, getter/setters, etc
	- Testing framework

Discussion and lunch (1h)
---------------------------

Lesson 4: Git distributed and collaboratif (3h  ED + JB + TG ...)
-----------------------------------------------------------------
	- Git distributed
	- Github and other web based infrastructures for git
	- Git and data: introducing git-annex (and git-lfs)
	- Handling data, the future: DataLad

~~~~~~~~~~~~~~~~~~~
Wednesday May 8th
~~~~~~~~~~~~~~~~~~~

Lesson 5: Scientific python ecosystem (3h JB + NB +  ?)
-----------------------------------------------------------------
	- The basics: Numpy, Scipy, Matplotlib 
	- Python random generator
	- Pandas
	- Seaborn and others
	- jupyter 

Discussion and lunch (1h)
---------------------------

Lesson 6: Containers: Docker and dockerhub (3h GK + SB)
-----------------------------------------------------------------
	- Containers v ersus virtual machines
	- Docker and singularity 
	- Neurodocker 
	- Launching pipelines on HPC 

~~~~~~~~~~~~~~~~~~~
Thursday May 9th
~~~~~~~~~~~~~~~~~~~

[Part III: Data analysis : concept and tools]

Lesson 7: Exploring and visualizing data (3h ?)
-----------------------------------------------------------------
	- Data reduction techniques and visualization 
	- The SVD
	- introduction to clustering techniques
		- kmeans - wards - spectral clustering  
	- tsne

Discussion and lunch (1h)
---------------------------

Lesson 8: Statistical tools - the basics (3h JB / ?)
-----------------------------------------------------------------
	- Sampling - Distributions, CDF,  etc  
	- Null hypothesis significance testing paradigm, notion of effect size
	- GLM
	- P-values, p-hacking, power, PPV
	- NHST: non parametric methods, permutations
	- Scipy stats module + Statsmodels package

~~~~~~~~~~~~~~~~~~~
Friday May 10th
~~~~~~~~~~~~~~~~~~~

Lesson 11: Model comparison, cross validation, Sampling techniques  (PB / JB 3h)
-----------------------------------------------------------------
	- Notion of model validation and model comparison
	- Bootstrap - Jacknife
	- Cross-validation
	- Distributing computation 

Discussion and lunch (1h)
---------------------------

Lesson 12: Machine learning (3h JV / ...)
-----------------------------------------------------------------
	- Prediction and prediction error
	- scikit-learn and ni-learn and exmaple
	- SVM - Random Forest
	- An introduction to deep learning

Recap and miscellaneous
-----------------------------------------------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Saturday May 11th ? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lesson 10: The Bayesian framework (3h)
-----------------------------------------------------------------
	- Bayes basics 
	- Positive predictive values
	- Introduction to pyMC3 / python tools for Bayesian analyses


![How to draw an owl?][owl] 

[owl]:/home/jb/documents/talks_travels/material/draw-an-owl.jpg "How to avoid this issue?"

