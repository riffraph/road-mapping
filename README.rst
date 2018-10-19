############
road mapping
############

How to test
----

    tox -e py36

This will:
* package the code
* install dependencies 
* create a virtual environment
* invoke the test runner


How to run
----

    python3 app.py -v [inputFilePath] [outputFolderPath]



Dependencies
----

Runtime:

    Python3

Packages:

* Graphviz
    - used to generate diagrams

    pip install Graphviz


* OpenPyXl
    -  used to open and read Excel 2010 xlsx files

    pip install openpyxl

* PyTest
    - used for unit testing

    pip install pytest