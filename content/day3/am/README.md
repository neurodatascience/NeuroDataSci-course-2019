# Introduction to Re-executability and Virtualization

The structure of this morning will be as follows:

- An overview of computer architectures and components
- A refresher on reproducibility/re-executability and its relevance in Neuroscience
- An introduction to virtualization:
  - Vrtualenv
  - Conda
  - Containers, and 
  - Virtual Machines
- A case study in selecting virtualization tools:
  - Containing a Python project within a virtualenv
  - Adding non-Python dependencies with Conda
  - Bridging operating systems with Docker
  - Converting to super-computers with Singularity
  - A look at where Virtual Machines become necessary
- Introduction to tools and platforms for effective sharing of tools
- Building our own Python and Docker environments

### Overview of Computers

- [Summary of pieces and Docker, simply](https://blog.usejournal.com/what-is-docker-in-simple-english-a24e8136b90b)

### Reproducibility in Neuroscience

- Operating system **versions** [can cause meaningful differences](https://twitter.com/TristanGlatard/status/896933603128553472)
- Different processing tools [produce different results](https://onlinelibrary.wiley.com/doi/pdf/10.1002/hbm.24603)

### Introduction to Virtualization

![xkcd-python-environments](https://imgs.xkcd.com/comics/python_environment.png)


In short, there are a lot of tools that allow you to *abstract* the build process
of your tools at various levels. For instance, let's look at the following:

![env heirarchy](https://raw.githubusercontent.com/goanpeca/pyday-cali-2019/master/img_source/isolation.png)

We see that at the lowest level we have "bare metal" -- these are applications that
are installed directly on a system. Slightly above that we see virtual machines.
These encapsulate entire operating systems (of any type) and file systems, and
can function completely on their own. Above that, we see Docker containers. These
come with libraries associated with one of many possible Linux/Unix-based operating
systems, and interacy with the operating system of the machine upon which they're
being run. Slightly further we have Conda environments that run natively to an
operating system and install libraries and packages there. These are built directly
within a given operating system. Finally, we have pip virtual environments which are
similar to Conda environments with the exception that they only manage packages
which have been developed and shipped in Python.

Depending on the nature of your analysis, how you wish to distribute it, its
dependencies, and where you'd like to run it, a different level of virtualization
may be appropriate. As a rule of thumb, let's say:

| Tool | Description | Do I want to do this? |
|:--|:--|:--|
| Pip Virtualenv | "I want to install and package Python libraries on my machine" | Yes! |
| Conda | "I want to install and package Python libraries and other tools on my machine" | Yes! |
| Docker | "I want to package tools for any machine" | Yes! |
| Virtual Machine | "I want to package an entire machine" | \*Not very often... |


### Case Study in Virtualization


### Introduction to Effective Sharing of Tools

See: [poster on FAIR pipelines with Boutiques and Zenodo](https://figshare.com/articles/fair-pipelines-poster_pdf/8143241)


### Building Virtualenv/Conda and Docker Environments


