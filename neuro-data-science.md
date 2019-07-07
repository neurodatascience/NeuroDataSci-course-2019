
Title : Fundamentals in Neuro Data Science
===========================================

Key words: teaching, mcgill, open data science, reproducibiliy, neuroscience, neuroimaging

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

The course will require that you have basic programming experience and one or more
undergraduate course(s) in statistical analysis (or equivalent experience),
but it will be aimed at life scientists (neurologists, psychiatrists, 
pyschologists, neuroscientists) who wish to improve their research practices, 
or students who want an introduction to data science with examples in neuroscience 
and neuroimaging.

The first week, outlined below, can be conceptually divided into three sections:

- Part I: Introduction and Motivation  
- Part II: Reproducibility and Data Management Tools  
- Part III: Data analysis: concept and tools  

---

## Schedule at a Glance
---

#### Monday, August 5th
    - 09:00 - Course Introduction
    - 10:00 - Epistemology and lessons from the past
    - 12:00 - Lunch
    - 13:00 - Installation time and troubleshooting.
    - 14:00 - Git and Github
    - 17:00 - Dismissal

#### Tuesday, August 5th
    - 09:00 - Python for Data Analysis
    - 12:00 - Lunch
    - 13:00 - Standards for project management and organization
    - 16:00 - Assessment 1

#### Wednesday, August 5th
    - 09:00 - Using and building Containers
    - 12:00 - Lunch
    - 13:00 - Guest Lecture on Binder + Jupyter
    - 14:00 - High-Performance Computing and Compute Canada
    - 16:00 - Assessment 2

#### Thursday, August 5th
    - 09:00 - Exploring and Visualizing Data
    - 12:00 - Lunch
    - 13:00 - Guest Lecture on TBA
    - 14:00 - Some statistical tools and pitfalls
    - 16:00 - Dismissal

#### Friday, August 5th
    - 09:00 - Introduction to Machine Learning
    - 13:00 - Lunch
    - 14:00 - Introduction to Deep Learning
    - 17:00 - Assessment 3
---

# Full Schedule
---

## Monday, August 5th

### 9:00 - Course Introduction (JB Poline)
An introduction to BrainHack School, including a brief history, motivation, 
objectives, evaluation process and code of conduct. This will be followed by an 
outline of the four-week course proposed across Concordia, McGill, Polytechnique 
and Université de Montréal, followed by an introduction to Week 1.

**Learning Objectives:** 
    - Become familiar with the objectives and logistics of BrainHack school.

### 10:00 - Epistemology and lessons from the past (JB Poline)

An in-depth exploration of the facets and challenges of neuroscience that 
created the need for initiatives like BrainHack School. This will included an 
overview of some classical epistemological contexts, and topics related to 
reproducibility, falsifiability, and statistics.

**Learning Objectives:** Understand the greater context that created the need for 
the tools you will learn to use in BrainHack school.


### 12:00 - Lunch

### 13:00 - Installation time and troubleshooting: 1 hour

### 14:00 - Git and GitHub (JB Poline)

Interactive session where students will become familiar with the shell, 
followed by a deep dive into the Git model for distributed version-control and 
collaboration. The aim of this workshop will be not only to understand the 
basics of Git, but also understand how to never lose any work, and how to 
successfully collaborate with oneself.

**Learning Objectives:** 1) Transition to using the shell regularly and comfortably; 
2) An understanding of how Git works and how to use Git and Github for 
version-control; 3) …

---

## Tuesday, August 6th

### 09:00 - Python for data analysis (Jake Vogel and Greg Kiar)

A presentation on why to use Python for data analysis, followed by an 
interactive workshop. The workshop will cover key data structures, 
automation basics, and the concept of functional programming. Students will 
also be introduced to the most common packages used for Python data analysis, 
including Numpy, Scipy, Matplotlib, Pandas and Nibabel. Finally, students will 
learn how to convert neuroimages to analyzable data.

**Learning Objectives:** 1) Use a python interpreter and text editor to write and 
execute python scripts. 2) Use python to convert neuroimages and spreadsheets 
to data to analyze and visualize.


### 12:00 - Lunch: 1 hour

### 13:00 Standards for project management and organization (Elizabeth Dupre & ...?)

Neuroscience is rapidly moving from isolated analysis in the void to 
collaboration, translation and data sharing/hosting. New challenges have thus 
arisen relating to project organization, sharing of tools and data and 
standardization of protocols across labs and environments. We will review tools 
for general project organization (e.g. Project TIER and DRESS protocol) and 
standardization (BIDS), and cover the basics of creating a sharable package or 
toolset.

**Learning Objectives:** 1) Understand the challenges and responsibilities of 
effectively sharing data and tools. 2) …


### 16:00: Assessment 1

---

## Wednesday, August 7th

### 09:00 - Containers (Greg Kiar & Elizabeth Levitis)

A large challenge to reproducibility lies in the fact that scientists use 
different versions of different tools across different platforms and operating 
systems, all of which are in constant flux. Virtual machines and containers 
help to create static environments tailored to one’s analyses, which can be 
easily shared. This lesson will include an overview (and interactive workshop?) 
of popular containers in neuroscience, including Docker, Singularity and 
Neurodocker.

**Learning objectives:** 1) Understand the difference between Virtual Machines and 
containers. 2) Learn why, when and how to containerize your code, tool or 
analyses.


### 12:00 - Lunch

### 13:00 - Guest Lecture: Jupyter and Binder (Felix-Antoine Fortin)

Abstract TBA

### 14:00 - High-Performance Computing (Felix-Antoine Fortin)

Abstract TBA

### 16:00 - Assessment 2: 0.5 hours

---

## Thursday, August 8th

###  09:00 Exploring and visualizing data (Elizabeth Dupre & JB Poline)

Data analysis should always be preceded by a period where one learns about 
one’s dataset. In this interactive workshop, students will use different 
techniques in Python to visualize characteristics of, and relationships 
between, data. This will include steps for describing data, reducing data (PCA, 
ICA, clustering), basic statistical analysis, and power analysis.

**Learning Objectives:** 1) Use python to visualize statistical relationships. 2) Run a 
basic statistical model using python. 3) Understand common pitfalls and gotchas 
of statistical analysis, and how to avoid them. 4) Learn rationale, dangers and 
best practices of data-reduction and execute a data-reduction pipeline using 
python.

### 12:00 - Lunch

### 13:00 - Guest Lecture: Topic TBA (Causal analysis?) (Manjari Narayan)

Abstract TBA

### 14:00 - Some statistical tools and their pitfalls (Manjari Narayan, JB Poline)
Life science and medicine researchers often rely on a series of classical tools for data analysis
and the null hypothesis testing framework. In this session, we will present some of
the classical (and maybe not so classical) tools often used by this community (eg
GLM, ANOVAs, mixed effect models, analysis of correlations, power analysis). We will 
show how to use them in an appropriate manner and point to the potential issues as well 
as to alternatives in a non parametric context. Examples of models and results will be 
demonstrated in a hands on session. 

**Learning Objectives:** 1) Have a more in depth understanding of the clasical statistical
data analysis tools. 2) Know some of their limitations and pitfalls. 3) Know how non
parametric alternatives to classical statistics can improve the solidity of the results. 

---

## Friday, August 9th

### 09:00 Introduction to machine learning (Jake Vogel & Estefany Suarez)

Machine learning has rapidly become a popular approach in Neuroscience. We will 
overview what machine learning actually is, when it is useful and when it is 
not, important themes and best practices, and some of the most common 
algorithms. An interactive workshop will involve using Python to perform model 
comparison, feature selection, prediction using classification and regression 
algorithms, feature interpretation, and other topics 
like bagging/consensus.

**Learning Objectives:** 1) Undersand how and when to include machine learning in 
your study design; 2) Learn to avoid the many mistakes commonly made in machine 
learning studies; 3) Use python to perform a machine learning pipeline from 
end to end.

### 13:00 Lunch

### 14:00 Introduction to Deep Learning (Jessica Thompson & ...?)

Deep learning and AI are gaining extreme popularity within all strata of 
science, and even in popular culture. This lecture will cover what deep 
learning actually is, when it is and is not appropriate for data analysis, 
some basic examples of common and highly successful algorithms, and a review of 
best practices. (An interactive workshop will demonstrate how to use Python to 
construct an execute a deep learning model.

**Learning Objectives:** 1) Understand when deep learning is an appropriate tool
for analysis. 2) Run a basic deep learning model.

### 17:00 - Assessment 3
