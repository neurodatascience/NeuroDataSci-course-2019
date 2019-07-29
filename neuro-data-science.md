
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
    - 13:00 - Using and building Containers
    - 16:30 - Assessment 1
    - 17:00 - Dismissal
    - 18:00 - Optional social event

#### Wednesday, August 5th
    - 09:00 - Standards for project management and organization
    - 12:00 - Lunch
    - 13:00 - Guest Lecture on Binder
    - 14:00 - High-Performance Computing and Compute Canada
    - 17:00 - Dismissal

#### Thursday, August 5th
    - 09:00 - Introductory statistics
    - 12:00 - Lunch
    - 13:00 - Guest Lecture on estimation of connectivity
    - 14:00 - Classical machine learning
    - 17:00 - Dismissal

#### Friday, August 5th
    - 09:00 - Introduction to Deep Learning
    - 12:00 - Lunch
    - 13:00 - Multivariate statistics and matrix factorizations
    - 16:00 - Assessment 2
    - 17:00 - Dismissal
---

# Full Schedule
---

## Monday, August 5th

### 9:00 - Course Introduction (JB Poline)
An introduction to BrainHack School, including a brief history, motivation,
objectives, evaluation process, and code of conduct.
There will be an outline of the four-week course proposed across Concordia, McGill, Polytechnique and Université de Montréal,
followed by an introduction to Week 1.

**Learning Objectives:**
    - Become familiar with the objectives and logistics of BrainHack school.

### 10:00 - Epistemology and lessons from the past (JB Poline)

An in-depth exploration of the facets and challenges of neuroscience that
created the need for initiatives like BrainHack School. This will included an
overview of some classical epistemological contexts, and topics related to
reproducibility, falsifiability, and statistics.

**Learning Objectives:** Understand the greater context that created the need for
the tools you will learn to use in BrainHack school.

| Content       | Time allotted | Instructor  |
| ------------- |:--------------:|-------------|
| Summary of current reproducibility problems     | 1 hour | JB Poline |
| Popper and Kuhn     | 1 hour | JB Poline |


### 12:00 - Lunch

### 13:00 - Installation time and troubleshooting: 1 hour

### 14:00 - Git and GitHub (JB Poline, TBD)

Interactive session where students will become familiar with the shell,
followed by a deep dive into the Git model for distributed version-control and
collaboration. The aim of this workshop will be not only to understand the
basics of Git, but also understand how to never lose any work, and how to
successfully collaborate with oneself.

**Learning Objectives:** 1) Transition to using the shell regularly and comfortably,
2) an understanding of how Git works,
and 3) how to use Git and Github for version-control.

| Content       | Time allotted | Instructor  |
| ------------- |:--------------:|-------------|
| Introduction to the shell     | 1 hour | JB Poline |
| Introduction to git for version control    | 1 hour | JB Poline |
| Introduction to github for collaboration    | 1 hour | JB Poline |

---

## Tuesday, August 6th

### 09:00 - Python for data analysis (Peer Herholz, Greg Kiar)

A presentation on why to use Python for data analysis, followed by an
interactive workshop. The workshop will cover key data structures,
automation basics, and the concept of functional programming. Students will
also be introduced to the most common packages used for Python data analysis,
including Numpy, Scipy, Matplotlib, Pandas and Nibabel. Finally, students will
learn how to convert neuroimages to analyzable data.

**Learning Objectives:** 1) Use a python interpreter and text editor to write and
execute python scripts.
2) Use python to convert neuroimages and spreadsheets to data to analyze and visualize.

| Content       | Time allotted | Instructor  |
| ------------- |:--------------:|-------------|
| Variables, types, and comparisons     | 20 minutes | Greg Kiar |
| Logic, looping, and functions    | 20 minutes | Greg Kiar |
| Debugging, scripts, and file I/O    | 20 minutes | Greg Kiar |
| File parsing in standard python     | 1 hour | Greg Kiar |
| Libraries and the scientific python ecosystem    | 20 minutes | Peer Herholz |
| Better data management    | 10 minutes | Peer Herholz |
| Stepwise neuroimaging workflow in python    | 30 minutes | Peer Herholz |

### 12:00 - Lunch: 1 hour

### 13:00 - Containers (Peer Herholz, Greg Kiar, & Liza Levitis)

A large challenge to reproducibility lies in the fact that scientists use
different versions of different tools across different platforms and operating
systems, all of which are in constant flux. Virtual machines and containers
help to create static environments tailored to one’s analyses, which can be
easily shared. This lesson will include an overview (and interactive workshop?)
of popular containers in neuroscience, including Docker, Singularity and
Neurodocker.

**Learning objectives:** 1) Understand the difference between Virtual Machines (VMs) and containers.
2) Learn why, when and how to containerize your code, tool or analyses.

| Content       | Time allotted | Instructor  |
| ------------- |:--------------:|-------------|
| What is a computer     | 20 minutes | Greg Kiar |
| Reproducibility / re-executability    | 10 minutes | Greg Kiar |
| Introduction to Virtualenv, Conda, Containers    | 1.5 hours | Peer Herholz |
| Boutiques / Zenodo for effective data sharing    | 10 minutes | Greg Kiar |
| Package python environment from morning session    | 50 minutes | Liza Levitis |


### 16:30: Assessment 1

---

## Wednesday, August 7th

### 9:00 Standards for project management and organization (Elizabeth DuPre)

Neuroscience is rapidly moving from isolated analysis in the void to
collaboration, translation and data sharing/hosting. New challenges have thus
arisen relating to project organization, sharing of tools and data and
standardization of protocols across labs and environments. We will review tools
for general project organization (e.g. Project TIER and DRESS protocol) and
standardization (BIDS), and cover the basics of creating a sharable package or
toolset.

**Learning Objectives:** 1) Understand the challenges and responsibilities of
effectively sharing data and tools. 2)

| Content       | Time allotted | Instructor  |
| ------------- |:--------------:|-------------|
| BIDS, Project Tier, and SciCrunch     | 1 hour | Elizabeth DuPre |
| Project Jupyter    | 1 hour | Elizabeth DuPre |
| pyBIDS, BIDS App practical    | 1 hours | Elizabeth DuPre |

### 12:00 - Lunch

### 13:00 - Guest Lecture: Binder (Felix-Antoine Fortin)

Abstract TBA

### 14:00 - Advanced Research Computing (Felix-Antoine Fortin)

A presentation on what is Compute Canada and advanced research computing
(ARC) intertwined with an interactive workshop. The workshop will focus on
connecting to a computing cluster with SSH, accessing the scientific
softwares and interacting with the job scheduler Slurm.

**Learning Objectives:** 1) Understand what is Compute Canada and ARC
2) Learn how to connect to an ARC cluster
and 3) Learn how to write and submit jobs to Slurm

| Content       | Time allotted | Instructor  |
| ------------- |:--------------:|-------------|
| Introduction to Compute Canada     | 45 min | Félix-Antoine Fortin |
| Connection and file transfer with SSH  | 30 min | Félix-Antoine Fortin |
| Loading scientific software with Lmod    | 30 min | Félix-Antoine Fortin |
| Creation and submission of jobs with Slurm    | 1 hour | Félix-Antoine Fortin |
| Introduction to data transfer with Globus    | 15 min | Félix-Antoine Fortin |

---

## Thursday, August 8th

###  09:00 Some statistical tools (Elizabeth DuPre & Jake Vogel)

Life science and medicine researchers often rely on a series of classical tools for data analysis and the null hypothesis testing framework.
In this session, we will present some of the classical tools often used by this community, particularly linear regression and GLM.
We will show how to use them in an appropriate manner and point to alternatives in a non parametric context.
Examples of models and results will be demonstrated in a hands on session.

**Learning Objectives:** 1) Use python to visualize variables.
2) Run a basic linear statistical model using python (statsmodels).
3) Introduce the general linear model (GLM).
4) Introduce non-parametric inference.

| Content       | Time allotted | Instructor  |
| ------------- |:--------------:|-------------|
| Visualizations to understand your data | 30 minutes | Jake Vogel |
| Basic statistcal testing in python | 30 minutes | Elizabeth Dupre |
| Intro to multiple testing and data reduction | 20 minutes | Elizabeth Dupre |
| Stretch break / extra time | 10 minutes | E'rbody |

### 10:30 - Guest Lecture: Statistical decomposition (Bratislav Misic)

### 12:00 - Lunch

### 13:00 - Guest Lecture: Estimation of connectivity (Manjari Narayan)

Abstract TBA

### 14:00 - Introduction to machine learning (Jake Vogel & Estefany Suarez)

Machine learning has rapidly become a popular approach in Neuroscience. We will
overview what machine learning actually is, when it is useful and when it is
not, important themes and best practices, and some of the most common
algorithms. An interactive workshop will involve using Python to perform model
comparison, feature selection, prediction using classification and regression
algorithms, feature interpretation, and other topics
like bagging/consensus.

**Learning Objectives:** 1) Understand how and when to include machine learning in
your study design; 2) Learn to avoid the many mistakes commonly made in machine
learning studies; 3) Use python to perform a machine learning pipeline from
end to end.

| Content       | Time allotted | Instructor  |
| ------------- |:--------------:|-------------|
| Key concepts in machine learning | 1.25 hours | Estefany Suarez |
| Caffiene break | 15 minutes | E'rbody |
| Nilearn for machine learning with neuroimaging data | 1.5 hours | Jake Vogel |

---

## Friday, August 9th

### 09:00 Introduction to Deep Learning (Joseph Viviano)

Deep learning and AI are gaining extreme popularity within all strata of
science, and even in popular culture. This lecture will cover what deep
learning actually is, when it is and is not appropriate for data analysis,
some basic examples of common and highly successful algorithms, and a review of
best practices. (An interactive workshop will demonstrate how to use Python to
construct an execute a deep learning model.

**Learning Objectives:** 1) Understand when deep learning is an appropriate tool
for analysis. 2) Run a basic deep learning model.

| Content       | Time allotted | Instructor  |
| ------------- |:--------------:|-------------|
| | |  |

### 12:00 Lunch

### 13:00 Multivariate statistics and matrix factorizations ()

**Learning Objectives:** 1) Introduce common decompositions such such as PCA, NMF.
2) Demonstrate how to perform decompositions in Python.
3) Discuss why and how decompositions can be integrated into a machine learning framework.

### 16:00 - Assessment 2
