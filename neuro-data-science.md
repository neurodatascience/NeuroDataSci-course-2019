
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

[Part II: Reproducibility and Data Management Tools]

Lesson 2: Computational Basics : shell and git (3h JB + PB ?)
-----------------------------------------------------------------
	- Know your shell
	- Know your editor
	- Git: understand the model
		* How to Never lose anything 
		* How do I best collaborate with myself?
	- Git distributed
	- Github and other web based infrastructures for git

~~~~~~~~~~~~~~~~~~~
Tuesday May 7th
~~~~~~~~~~~~~~~~~~~

Lesson 3: Standards for project management and organization (3h ED / JB / ? )
-----------------------------------------------------------------------------
	- Project hygiene
	- BIDS
	- OSF?
	- Binders?

Discussion and lunch (1h)
---------------------------
Lesson 4: Containers: Docker and dockerhub (3h GK + SB)
-----------------------------------------------------------------
	- Containers versus virtual machines
	- Docker and singularity 
	- Neurodocker (<--?)
	- Launching pipelines on HPC 


~~~~~~~~~~~~~~~~~~~
Wednesday May 8th
~~~~~~~~~~~~~~~~~~~

[Part III: Data analysis : concept and tools]
Lesson 5: Computational Basics : python for programmers (3h JB + NB + JV)
-----------------------------------------------------------------
	- Why Python : a software glue
	- Python key data structures
	- Automation basics: For loops, conditional statements, and funtional programming
	- The data analysis suite: Numpy, Scipy, Matplotlib, Pandas, Nibabel 
	- From images to data in Python

Discussion and lunch (1h)
---------------------------

External gives a talk (1 hr) 
-----------------------------------------------------------------
External gives a lesson? (1 hr) -- Or a survey of open datasets -- Or spillover of previous section
-----------------------------------------------------------------
Python practice? (1 hr)
-----------------------------------------------------------------

~~~~~~~~~~~~~~~~~~~
Thursday May 9th
~~~~~~~~~~~~~~~~~~~

[Part III: Data analysis : concept and tools]

Lesson 6: Exploring, visualizing and preparing data (3h ?)
-----------------------------------------------------------------
	-- Getting to know your dataset:
		-- Visualizing data
		-- Describing data (basic stats in python)
		-- Data reduction (SVD, clustering, ICA)
	-- Model comparison, cross-validation, sampling techniques
		- Notion of model validation and model comparison
		- Bootstrap - Jacknife
		- Cross-validation

Discussion and lunch (1h)
---------------------------

Lesson 7: Machine learning (3h JV / ...)
-----------------------------------------------------------------
	- Prediction and prediction error
	- Feature selection
	- Classification
	- Regression
	- Bagging/consensus
	- Feature interpretation
	- An introduction to deep learning

~~~~~~~~~~~~~~~~~~~
Friday May 10th
~~~~~~~~~~~~~~~~~~~

Project brainstorm
-----------------------------------------------------------------
	- Students present project ideas

Discussion and lunch (1h)
---------------------------

Lesson XXX: Bonus time that is unused -- 3 hours saved to put whatever we want in
-----------------------------------------------------------------
	

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

