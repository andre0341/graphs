# Experimenting with Python Graphs

# Instructions
The main is concat_file_creation_scripts, that calls sequentially a series of scripts to manipulate an input and create graphs and a docx
file automatically. 

First step is splitting and polishing data (splitdatafromxls.py).
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

# Next Steps
Simplify and clean the file
