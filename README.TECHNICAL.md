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

To place the IPython notebook in Log Mode, Debug Mode, or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Debug Mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in Log Mode for log information sent to a log file. If the program is in Log Mode but NOT Debug Mode, it displays no debug information, but writes that information to the log file. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG files in the Images Folder.

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

|&rarr; [./Table-Of-Contents-PAFWSUS.md](./Table-Of-Contents-PAFWSUS.md)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/ClimatePyFigure24MinimumMaximumandAverageTemperaturesByYear.png](./Images/ClimatePyFigure24MinimumMaximumandAverageTemperaturesByYear.png)
  
  &emsp; |&rarr; [./Images/ClimatePyFigure32TemperatureObservationsTOBs2010Histogram.png](./Images/ClimatePyFigure32TemperatureObservationsTOBs2010Histogram.png)
  
  &emsp; |&rarr; [./Images/ClimatePyFigure33TemperatureObservationsTOBs2011Histogram.png](./Images/ClimatePyFigure33TemperatureObservationsTOBs2011Histogram.png)
  
  &emsp; |&rarr; [./Images/ClimatePyFigure34TemperatureObservationsTOBs2012Histogram.png](./Images/ClimatePyFigure34TemperatureObservationsTOBs2012Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure35TemperatureObservationsTOBs2013Histogram.png](./Images/ClimatePyFigure35TemperatureObservationsTOBs2013Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure36TemperatureObservationsTOBs2014Histogram.png](./Images/ClimatePyFigure36TemperatureObservationsTOBs2014Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure37TemperatureObservationsTOBs2015Histogram.png](./Images/ClimatePyFigure37TemperatureObservationsTOBs2015Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure38TemperatureObservationsTOBs2016Histogram.png](./Images/ClimatePyFigure38TemperatureObservationsTOBs2016Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure39TemperatureObservationsTOBs20178monthsHistogram.png](./Images/ClimatePyFigure39TemperatureObservationsTOBs20178monthsHistogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure411TotalPrecipitationvsYear.png](./Images/ClimatePyFigure411TotalPrecipitationvsYear.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure421PrecipitationvsTime2010.png](./Images/ClimatePyFigure421PrecipitationvsTime2010.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure422Precipitation2010Histogram.png](./Images/ClimatePyFigure422Precipitation2010Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure431PrecipitationvsTime2011.png](./Images/ClimatePyFigure431PrecipitationvsTime2011.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure432Precipitation2011Histogram.png](./Images/ClimatePyFigure432Precipitation2011Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure441PrecipitationvsTime2012.png](./Images/ClimatePyFigure441PrecipitationvsTime2012.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure442Precipitation2012Histogram.png](./Images/ClimatePyFigure442Precipitation2012Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure451PrecipitationvsTime2013.png](./Images/ClimatePyFigure451PrecipitationvsTime2013.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure452Precipitation2013Histogram.png](./Images/ClimatePyFigure452Precipitation2013Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure461PrecipitationvsTime2014.png](./Images/ClimatePyFigure461PrecipitationvsTime2014.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure462Precipitation2014Histogram.png](./Images/ClimatePyFigure462Precipitation2014Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure471PrecipitationvsTime2015.png](./Images/ClimatePyFigure471PrecipitationvsTime2015.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure472Precipitation2015Histogram.png](./Images/ClimatePyFigure472Precipitation2015Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure481PrecipitationvsTime2016.png](./Images/ClimatePyFigure481PrecipitationvsTime2016.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure482Precipitation2016Histogram.png](./Images/ClimatePyFigure482Precipitation2016Histogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure491PrecipitationvsTime20178Months.png](./Images/ClimatePyFigure491PrecipitationvsTime20178Months.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure492Precipitation20178MonthsHistogram.png](./Images/ClimatePyFigure492Precipitation20178MonthsHistogram.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure3101TemperatureObservationsTOBs20102017Histograms.png](./Images/ClimatePyFigure3101TemperatureObservationsTOBs20102017Histograms.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure3102TemperatureObservationsTOBsDistribution.png](./Images/ClimatePyFigure3102TemperatureObservationsTOBsDistribution.png)

  &emsp; |&rarr; [./Images/ClimatePyFigure4103Precipitation20102017Distribution.png](./Images/ClimatePyFigure4103Precipitation20102017Distribution.png)

  &emsp; |&rarr; [./Images/ClimatePyTable23MostActiveStationIDsandTOBSByYear.png](./Images/ClimatePyTable23MostActiveStationIDsandTOBSByYear.png)

  &emsp; |&rarr; [./Images/ClimatePyTable24MinimumMaximumandAverageTemperaturesByYear.png](./Images/ClimatePyTable24MinimumMaximumandAverageTemperaturesByYear.png)

  &emsp; |&rarr; [./Images/ClimatePyTable32TemperatureObservationsTOBs2010SummaryStatistics.png](./Images/ClimatePyTable32TemperatureObservationsTOBs2010SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable33TemperatureObservationsTOBs2011SummaryStatistics.png](./Images/ClimatePyTable33TemperatureObservationsTOBs2011SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable34TemperatureObservationsTOBs2012SummaryStatistics.png](./Images/ClimatePyTable34TemperatureObservationsTOBs2012SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable35TemperatureObservationsTOBs2013SummaryStatistics.png](./Images/ClimatePyTable35TemperatureObservationsTOBs2013SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable36TemperatureObservationsTOBs2014SummaryStatistics.png](./Images/ClimatePyTable36TemperatureObservationsTOBs2014SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable37TemperatureObservationsTOBs2015SummaryStatistics.png](./Images/ClimatePyTable37TemperatureObservationsTOBs2015SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable38TemperatureObservationsTOBs2016SummaryStatistics.png](./Images/ClimatePyTable38TemperatureObservationsTOBs2016SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable39TemperatureObservationsTOBs20178MonthsSummaryStatistics.png](./Images/ClimatePyTable39TemperatureObservationsTOBs20178MonthsSummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable42Precipitation2010SummaryStatistics.png](./Images/ClimatePyTable42Precipitation2010SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable43Precipitation2011SummaryStatistics.png](./Images/ClimatePyTable43Precipitation2011SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable44Precipitation2012SummaryStatistics.png](./Images/ClimatePyTable44Precipitation2012SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable45Precipitation2013SummaryStatistics.png](./Images/ClimatePyTable45Precipitation2013SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable46Precipitation2014SummaryStatistics.png](./Images/ClimatePyTable46Precipitation2014SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable47Precipitation2015SummaryStatistics.png](./Images/ClimatePyTable47Precipitation2015SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable48Precipitation2016SummaryStatistics.png](./Images/ClimatePyTable48Precipitation2016SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable49Precipitation20178MonthsSummaryStatistics.png](./Images/ClimatePyTable49Precipitation20178MonthsSummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable3101TemperatureObservationsTOBs20102017SummaryStatistics.png](./Images/ClimatePyTable3101TemperatureObservationsTOBs20102017SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable3102TemperatureObservationsTOBs20102016CorrelationMatrix.png](./Images/ClimatePyTable3102TemperatureObservationsTOBs20102016CorrelationMatrix.png)

  &emsp; |&rarr; [./Images/ClimatePyTable4101PrecipitationvsTime20102017.png](./Images/ClimatePyTable4101PrecipitationvsTime20102017.png)

  &emsp; |&rarr; [./Images/ClimatePyTable4101TemperatureObservationsTOBs20102017SummaryStatistics.png](./Images/ClimatePyTable4101TemperatureObservationsTOBs20102017SummaryStatistics.png)

  &emsp; |&rarr; [./Images/ClimatePyTable4102Precipitation20102017Histograms.png](./Images/ClimatePyTable4102Precipitation20102017Histograms.png)

  &emsp; |&rarr; [./Images/ClimatePyTable4102TemperatureObservationsTOBs20102016CorrelationMatrix.png](./Images/ClimatePyTable4102TemperatureObservationsTOBs20102016CorrelationMatrix.png)

  &emsp; |&rarr; [./Images/ClimatePyTable4111TotalPrecipitationvsTime20102017.png](./Images/ClimatePyTable4111TotalPrecipitationvsTime20102017.png)

  &emsp; |&rarr; [./Images/ClimatePyTable4112TotalPrecipitation20102017SummaryStatistics.png](./Images/ClimatePyTable4112TotalPrecipitation20102017SummaryStatistics.png)
  
  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20230930ClimatePyDebug.txt](./Logs/20230930ClimatePyDebug.txt)

  &emsp; |&rarr; [./Logs/20230930ClimatePyLog.txt](./Logs/20230930ClimatePyLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/hawaii_measurements.csv](./Resources/hawaii_measurements.csv)

  &emsp; |&rarr; [./Resources/hawaii_stations.csv](./Resources/hawaii_stations.csv)

  &emsp; |&rarr; [./Resources/hawaii.sqlite](./Resources/hawaii.sqlite)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

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
