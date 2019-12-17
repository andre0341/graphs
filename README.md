# Project
Graphs. Experimenting with Python Graphs.
A repository to see how some Python graphs work. 

## Getting Started
### Prerequisites
Before using the files, make sure you have installed the latest version of Pandas, PlotLib, Numpy and Seaborn.
Suggested but not mandadtory the usage of Python 3.8+.

## Installing
To install Pandas from terminal 
> pip install pandas

To install matplotlib
> pip install matplotlib

To install numpy
> pip install numpy

To install seaborn
> pip install seaborn

## Instructions
The main is concat_file_creation_scripts, that calls sequentially a series of scripts to manipulate an input and create graphs and a docx
file automatically. 

First step is splitting and polishing data (splitdatafromxls.py).
`splitdatafromxls()`

Function splitdatafromxls requires no input, searches for an xml file (PMI-network-data.xmls) and uses line 1 (row 0 is considered the
header, row 1 is the first line with useful data).
splitdatafromxls retuns a dictionary with data extracted.

Strategia Produzione
createlollipopgraph receives requires a dictionary with data as input, takes some values and create a lollipop graph. saves the graph
as png for later usage and returns nothing.

Ricerca e Innovazione
createspidergraph() and createradargraph() both require the same dictionary as input, extract some values, save the graph as png (one 
with tecnologie 4.0 and ricerca&innovazione.

creategenericradargraph is the first experiment to create a generic function to print data as radar/spider graph without specifying the 
variables. Problem right now is Python seems to prefer avoiding the use of variables names as dynamic input for graph variales. 
Read line 23 for more info (Dataframe "group").
Some data manipulation is performed:
[:-1] to trim the % from original input
cast as integers
avoid 0 to have prettier graph

createdoctemplate creates a new docx with the name as the company (extracted from the xls file) and uploades the images created in
previous steps.

### Built With
* [Pandas](https://pandas.pydata.org/)
* [MatPlotLib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Numpy](https://numpy.org/) 
* [Pip](https://pypi.org/project/pip/) Package Manager

### Contributors
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us

### Versioning
Right now it's manual versioning. MAJOR.MINOR.PATCH format.  

### Authors
Andrea Vaccarella - Initial work - graphs and docs
See also the list of contributors who participated in this project.

### License
This project is not under any license at the time being.
This project will probably be released under the MIT License - (check the LICENSE.md file for details later)

### Acknowledgments
Hat tip to anyone whose code was used!

### Next Steps
Simplify and clean the file
