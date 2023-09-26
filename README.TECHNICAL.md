# **Precipitation Analysis from Weather Stations using SQLAlchemy**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image, SQLite, SQLAlchemy, and Flask.

Here are the requisite Terminal commands for the installation of these peripheral modules (SQLite is already installed on macOS):

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

python3 -m pip install sqlalchemy

python3 -m pip install Flask

----

### **Usage:**

----

The IPython notebook, ClimatePy.ipynb, and Flask API, ClimateApp.py, use the files in the Resources Folder and will not run without them.  The IPython Notebook and Flask API must have the following Python scripts in the same folder with them:

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PySubroutines.py

If the folders, Resources, Logs, and Images are not present, the IPython notebook will create them.  The Resources folder holds CSV input files and an SQLite file for the IPython Notebook and Flask API; the Logs folder contains debug and log files from testing the IPython Notebook; and the Images folder has the PNG image files of the IPython Notebook's tables and plots.

To place the IPython notebook in log mode, debug mode, or image mode set the parameter for the appropriate subroutine in coding cell #2 to True. In debug mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in log mode for log information sent to a log file. If the program is in log mode but not debug mode, it displays no debug information, but writes that information to the log file. If the program is in image mode, it writes all DataFrames, hvplot maps, and matplotlib plots to png files in the Images folder.

----

### **Resource Summary:**

----

#### Source code

ClimatePy.ipynb, ClimateApp.py,

#### Input files

hawaii.sqlite, hawaii_measurements.csv, hawaii_stations.csv

#### Output files

n/a

#### SQL script

n/a

#### Software

 Flask, Jupyter Notebook, Matplotlib, Numpy, Pandas, Python 3.11.4, SQLite

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./ClimateApp.py](./ClimateApp.py)

|&rarr; [./ClimatePy.ipynb](./ClimatePy.ipynb)

|&rarr; [./PyConstants.py](./PyConstants.py)

|&rarr; [./PyFunctions.py](./PyFunctions.py)

|&rarr; [./PyLogConstants.py](./PyLogConstants.py)

|&rarr; [./PyLogFunctions.py](./PyLogFunctions.py)

|&rarr; [./PyLogSubRoutines.py](./PyLogSubRoutines.py)

|&rarr; [./PySubRoutines.py](./PySubRoutines.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/ClimatePyFigure21PrecipitationvsDateLast12Months.png](./Images/ClimatePyFigure21PrecipitationvsDateLast12Months.png)
  
  &emsp; |&rarr; [./Images/ClimatePyFigure22PrecipitationHistogramLast12Months.png](./Images/ClimatePyFigure22PrecipitationHistogramLast12Months.png)
  
  &emsp; |&rarr; [./Images/ClimatePyFigure31MostActiveStationTemperatureObservationTOBSHistogram.png](./Images/ClimatePyFigure31MostActiveStationTemperatureObservationTOBSHistogram.png)
  
  &emsp; |&rarr; [./Images/ClimatePyTable21PrecipitationStatisticsLast12Months.png](./Images/ClimatePyTable21PrecipitationStatisticsLast12Months.png)
  
  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20230922ClimatePyDebug.txt](./Logs/20230922ClimatePyDebug.txt)

  &emsp; |&rarr; [./Logs/20230922ClimatePyLog.txt](./Logs/20230922ClimatePyLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

  &emsp; |&rarr; [./Resources/hawaii_measurements.csv](./Resources/hawaii_measurements.csv)

  &emsp; |&rarr; [./Resources/hawaii_stations.csv](./Resources/hawaii_stations.csv)

  &emsp; |&rarr; [./Resources/hawaii.sqlite](./Resources/hawaii.sqlite)

----

### **References:**

----

[Flask API documentation](https://flask.palletsprojects.com/en/2.3.x/api/)

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Matplotlib Documentation](https://matplotlib.org/stable/index.html)

[Numpy documentation](https://numpy.org/doc/1.26/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

[SQLite documentation](https://www.sqlite.org/docs.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

N. James George © 2023. All Rights Reserved.
