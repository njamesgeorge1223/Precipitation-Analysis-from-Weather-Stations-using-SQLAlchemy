# **Precipitation Analysis from Weather Stations using SQLAlchemy**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image, SQLite, SQLAlchemy, and Flask.

Here are the requisite Terminal commands for installation of these peripheral modules (in this order) (SQLite is already installed on macOS:

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

The IPython notebook, ClimatePy.ipynb, and Flask API, ClimateApp.py, use the files in the Resources Folder and will not run without them.  These files must have the following Python scripts in the same folder with them:

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PySubroutines.py

If the folders, Resources, Logs, and Images are not present, the IPython notebook will create them.  The Resources folder holds CSV input files for the IPython Notebook; the Logs folder contains debug and log files from testing the IPython Notebook; and the Images folder has the PNG image files of the IPython Notebook's tables and plots.

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

Jupyter Notebook, Python 3.11.4, Pandas, Matplotlib, Numpy, Flask, SQLite

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./PyConstants.py](./PyConstants.py)

|&rarr; [./PyFunctions.py](./PyFunctions.py)

|&rarr; [./PyLogConstants.py](./PyLogConstants.py)

|&rarr; [./PyLogFunctions.py](./PyLogFunctions.py)

|&rarr; [./PyLogSubRoutines.py](./PyLogSubRoutines.py)

|&rarr; [./PySubRoutines.py](./PySubRoutines.py)

|&rarr; [./Pymaceuticals.ipynb](./Pymaceuticals.ipynb)

|&rarr; [./PymaceuticalsFunctions.py](./PymaceuticalsFunctions.py)

|&rarr; [./PymaceuticalsSubRoutines.py](./PymaceuticalsSubRoutines.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/PymaceuticalsFigure421TumorVolumeLastbyDrugRegimenDistribution.png](./Images/PymaceuticalsFigure421TumorVolumeLastbyDrugRegimenDistribution.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure521LastGreatestTimepointDistribution.png](./Images/PymaceuticalsFigure521LastGreatestTimepointDistribution.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure611DrugRegimenbyNumberofDataPoints.png](./Images/PymaceuticalsFigure611DrugRegimenbyNumberofDataPoints.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure641DrugTreatmentRegimenbyDataPointsPerMouse.png](./Images/PymaceuticalsFigure641DrugTreatmentRegimenbyDataPointsPerMouse.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure741MouseWeightDistributionsforEachTreatmentGroup.png](./Images/PymaceuticalsFigure741MouseWeightDistributionsforEachTreatmentGroup.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure820MalevsFemaleMouseDistributionAll.png](./Images/PymaceuticalsFigure820MalevsFemaleMouseDistributionAll.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure821MalevsFemaleMouseDistributionCapomulin.png](./Images/PymaceuticalsFigure821MalevsFemaleMouseDistributionCapomulin.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure822MalevsFemaleMouseDistributionCeftamin.png](./Images/PymaceuticalsFigure822MalevsFemaleMouseDistributionCeftamin.png)

  &emsp; |&rarr; [./Images/PymaceuticalsFigure823MalevsFemaleMouseDistributionInfubinol.png](./Images/PymaceuticalsFigure823MalevsFemaleMouseDistributionInfubinol.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure824MalevsFemaleMouseDistributionKetapril.png](./Images/PymaceuticalsFigure824MalevsFemaleMouseDistributionKetapril.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure825MalevsFemaleMouseDistributionNaftisol.png](./Images/PymaceuticalsFigure825MalevsFemaleMouseDistributionNaftisol.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure826MalevsFemaleMouseDistributionPlacebo.png](./Images/PymaceuticalsFigure826MalevsFemaleMouseDistributionPlacebo.png)

  &emsp; |&rarr; [./Images/PymaceuticalsFigure827MalevsFemaleMouseDistributionPropriva.png](./Images/PymaceuticalsFigure827MalevsFemaleMouseDistributionPropriva.png)
  
  &emsp; |&rarr; 
[./Images/PymaceuticalsFigure828MalevsFemaleMouseDistributionRamicane.png](./Images/PymaceuticalsFigure828MalevsFemaleMouseDistributionRamicane.png)

  &emsp; |&rarr; [./Images/PymaceuticalsFigure829MalevsFemaleMouseDistributionStelasyn.png](./Images/PymaceuticalsFigure829MalevsFemaleMouseDistributionStelasyn.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure7311TumorVolumesvsMouseWeightsPlotswithHighCorrelation.png](./Images/PymaceuticalsFigure7311TumorVolumesvsMouseWeightsPlotswithHighCorrelation.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure8210MalevsFemaleMouseDistributionZoniferol.png](./Images/PymaceuticalsFigure8210MalevsFemaleMouseDistributionZoniferol.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsFigure8211MalevsFemaleMouseDistribution.png](./Images/PymaceuticalsFigure8211MalevsFemaleMouseDistribution.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsGraph351CapomulinTreatmentofMousel897.png](./Images/PymaceuticalsGraph351CapomulinTreatmentofMousel897.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsGraph351CapomulinTreatmentofMousem601.png](./Images/PymaceuticalsGraph351CapomulinTreatmentofMousem601.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsGraph352CeftaminTreatmentofMousew151.png](./Images/PymaceuticalsGraph352CeftaminTreatmentofMousew151.png)
  
  &emsp; |&rarr; [./Images/PymaceuticalsGraph353InfubinolTreatmentofMousea577.png](./Images/PymaceuticalsGraph353InfubinolTreatmentofMousea577.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph353InfubinolTreatmentofMousec139.png](./Images/PymaceuticalsGraph353InfubinolTreatmentofMousec139.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph354KetaprilTreatmentofMousep189.png](./Images/PymaceuticalsGraph354KetaprilTreatmentofMousep189.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph354KetaprilTreatmentofMouseu327.png](./Images/PymaceuticalsGraph354KetaprilTreatmentofMouseu327.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph355NaftisolTreatmentofMouser701.png](./Images/PymaceuticalsGraph355NaftisolTreatmentofMouser701.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph355NaftisolTreatmentofMousey601.png](./Images/PymaceuticalsGraph355NaftisolTreatmentofMousey601.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph356PlaceboTreatmentofMouses152.png](./Images/PymaceuticalsGraph356PlaceboTreatmentofMouses152.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph356PlaceboTreatmentofMousey478.png](./Images/PymaceuticalsGraph356PlaceboTreatmentofMousey478.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph357ProprivaTreatmentofMousei635.png](./Images/PymaceuticalsGraph357ProprivaTreatmentofMousei635.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph357ProprivaTreatmentofMouses187.png](./Images/PymaceuticalsGraph357ProprivaTreatmentofMouses187.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph358RamicaneTreatmentofMousej989.png](./Images/PymaceuticalsGraph358RamicaneTreatmentofMousej989.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph358RamicaneTreatmentofMouses508.png](./Images/PymaceuticalsGraph358RamicaneTreatmentofMouses508.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph359StelasynTreatmentofMousek862.png](./Images/PymaceuticalsGraph359StelasynTreatmentofMousek862.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph359StelasynTreatmentofMouses565.png](./Images/PymaceuticalsGraph359StelasynTreatmentofMouses565.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph731TumorVolumesvsMouseWeightsWithRegressionCapomulin.png](./Images/PymaceuticalsGraph731TumorVolumesvsMouseWeightsWithRegressionCapomulin.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph732TumorVolumesvsMouseWeightsWithRegressionCeftamin.png](./Images/PymaceuticalsGraph732TumorVolumesvsMouseWeightsWithRegressionCeftamin.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph733TumorVolumesvsMouseWeightsWithRegressionInfubinol.png](./Images/PymaceuticalsGraph733TumorVolumesvsMouseWeightsWithRegressionInfubinol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph734TumorVolumesvsMouseWeightsWithRegressionKetapril.png](./Images/PymaceuticalsGraph734TumorVolumesvsMouseWeightsWithRegressionKetapril.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph735TumorVolumesvsMouseWeightsWithRegressionNaftisol.png](./Images/PymaceuticalsGraph735TumorVolumesvsMouseWeightsWithRegressionNaftisol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph736TumorVolumesvsMouseWeightsWithRegressionPlacebo.png](./Images/PymaceuticalsGraph736TumorVolumesvsMouseWeightsWithRegressionPlacebo.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph737TumorVolumesvsMouseWeightsWithRegressionPropriva.png](./Images/PymaceuticalsGraph737TumorVolumesvsMouseWeightsWithRegressionPropriva.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph738TumorVolumesvsMouseWeightsWithRegressionRamicane.png](./Images/PymaceuticalsGraph738TumorVolumesvsMouseWeightsWithRegressionRamicane.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph739TumorVolumesvsMouseWeightsWithRegressionStelasyn.png](./Images/PymaceuticalsGraph739TumorVolumesvsMouseWeightsWithRegressionStelasyn.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph3510ZoniferolTreatmentofMousea401.png](./Images/PymaceuticalsGraph3510ZoniferolTreatmentofMousea401.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph3510ZoniferolTreatmentofMouseq633.png](./Images/PymaceuticalsGraph3510ZoniferolTreatmentofMouseq633.png)

  &emsp; |&rarr; [./Images/PymaceuticalsGraph7310TumorVolumesvsMouseWeightsWithRegressionZoniferol.png](./Images/PymaceuticalsGraph7310TumorVolumesvsMouseWeightsWithRegressionZoniferol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable111CompleteMedicalStudyDataFrame.png](./Images/PymaceuticalsTable111CompleteMedicalStudyDataFrame.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable121MouseIDswithDuplicateTimepoints.png](./Images/PymaceuticalsTable121MouseIDswithDuplicateTimepoints.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable122AllMouseIDswithDuplicateTimepointsRecords.png](./Images/PymaceuticalsTable122AllMouseIDswithDuplicateTimepointsRecords.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable221SummaryStatisticsTumorVolume.png](./Images/PymaceuticalsTable221SummaryStatisticsTumorVolume.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable421TumorVolumeStatisticsforCapomulin.png](./Images/PymaceuticalsTable421TumorVolumeStatisticsforCapomulin.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable422TumorVolumeStatisticsforCeftamin.png](./Images/PymaceuticalsTable422TumorVolumeStatisticsforCeftamin.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable423TumorVolumeStatisticsforInfubinol.png](./Images/PymaceuticalsTable423TumorVolumeStatisticsforInfubinol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable424TumorVolumeStatisticsforKetapril.png](./Images/PymaceuticalsTable424TumorVolumeStatisticsforKetapril.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable425TumorVolumeStatisticsforNaftisol.png](./Images/PymaceuticalsTable425TumorVolumeStatisticsforNaftisol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable426TumorVolumeStatisticsforPlacebo.png](./Images/PymaceuticalsTable426TumorVolumeStatisticsforPlacebo.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable427TumorVolumeStatisticsforPropriva.png](./Images/PymaceuticalsTable427TumorVolumeStatisticsforPropriva.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable428TumorVolumeStatisticsforRamicane.png](./Images/PymaceuticalsTable428TumorVolumeStatisticsforRamicane.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable429TumorVolumeStatisticsforStelasyn.png](./Images/PymaceuticalsTable429TumorVolumeStatisticsforStelasyn.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable521LastGreatestTimepointStatisticsforCapomulin.png](./Images/PymaceuticalsTable521LastGreatestTimepointStatisticsforCapomulin.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable522LastGreatestTimepointStatisticsforCeftamin.png](./Images/PymaceuticalsTable522LastGreatestTimepointStatisticsforCeftamin.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable523LastGreatestTimepointStatisticsforInfubinol.png](./Images/PymaceuticalsTable523LastGreatestTimepointStatisticsforInfubinol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable524LastGreatestTimepointStatisticsforKetapril.png](./Images/PymaceuticalsTable524LastGreatestTimepointStatisticsforKetapril.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable525LastGreatestTimepointStatisticsforNaftisol.png](./Images/PymaceuticalsTable525LastGreatestTimepointStatisticsforNaftisol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable526LastGreatestTimepointStatisticsforPlacebo.png](./Images/PymaceuticalsTable526LastGreatestTimepointStatisticsforPlacebo.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable527LastGreatestTimepointStatisticsforPropriva.png](./Images/PymaceuticalsTable527LastGreatestTimepointStatisticsforPropriva.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable528LastGreatestTimepointStatisticsforRamicane.png](./Images/PymaceuticalsTable528LastGreatestTimepointStatisticsforRamicane.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable529LastGreatestTimepointStatisticsforStelasyn.png](./Images/PymaceuticalsTable529LastGreatestTimepointStatisticsforStelasyn.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable621InfubinolStatisticalOutlier.png](./Images/PymaceuticalsTable621InfubinolStatisticalOutlier.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable622StatisticalOutlierMouseRecords.png](./Images/PymaceuticalsTable622StatisticalOutlierMouseRecords.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable641MouseIDbyNumberofDataPoints.png](./Images/PymaceuticalsTable641MouseIDbyNumberofDataPoints.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable642DrugTreatmentRegimenbyDataPointCategoryNumberofMice.png](./Images/PymaceuticalsTable642DrugTreatmentRegimenbyDataPointCategoryNumberofMice.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable740MouseIDbyDrugRegimenandWeight.png](./Images/PymaceuticalsTable740MouseIDbyDrugRegimenandWeight.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable741MouseWeightStatisticsforCapomulin.png](./Images/PymaceuticalsTable741MouseWeightStatisticsforCapomulin.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable742MouseWeightStatisticsforCeftamin.png](./Images/PymaceuticalsTable742MouseWeightStatisticsforCeftamin.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable743MouseWeightStatisticsforInfubinol.png](./Images/PymaceuticalsTable743MouseWeightStatisticsforInfubinol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable744MouseWeightStatisticsforKetapril.png](./Images/PymaceuticalsTable744MouseWeightStatisticsforKetapril.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable745MouseWeightStatisticsforNaftisol.png](./Images/PymaceuticalsTable745MouseWeightStatisticsforNaftisol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable746MouseWeightStatisticsforPlacebo.png](./Images/PymaceuticalsTable746MouseWeightStatisticsforPlacebo.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable747MouseWeightStatisticsforPropriva.png](./Images/PymaceuticalsTable747MouseWeightStatisticsforPropriva.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable748MouseWeightStatisticsforRamicane.png](./Images/PymaceuticalsTable748MouseWeightStatisticsforRamicane.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable749MouseWeightStatisticsforStelasyn.png](./Images/PymaceuticalsTable749MouseWeightStatisticsforStelasyn.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable811MouseGenderCountDistributionbyDrugRegimen.png](./Images/PymaceuticalsTable811MouseGenderCountDistributionbyDrugRegimen.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable812MouseGenderPercentDistributionbyDrugRegimen.png](./Images/PymaceuticalsTable812MouseGenderPercentDistributionbyDrugRegimen.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable4210TumorVolumeStatisticsforZoniferol.png](./Images/PymaceuticalsTable4210TumorVolumeStatisticsforZoniferol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable5210LastGreatestTimepointStatisticsforZoniferol.png](./Images/PymaceuticalsTable5210LastGreatestTimepointStatisticsforZoniferol.png)

  &emsp; |&rarr; [./Images/PymaceuticalsTable7410MouseWeightStatisticsforZoniferol.png](./Images/PymaceuticalsTable7410MouseWeightStatisticsforZoniferol.png)

  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20230922PymaceuticalsDebug.txt](./Logs/20230922PymaceuticalsDebug.txt)

  &emsp; |&rarr; [./Logs/20230922PymaceuticalsLog.txt](./Logs/20230922PymaceuticalsLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/MouseMetaData.csv](./Resources/MouseMetaData.csv)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

  &emsp; |&rarr; [./Resources/StudyResults.csv](./Resources/StudyResults.csv)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/) \

[Python Documentation](https://docs.python.org/3/contents.html) \

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html) \

[Matplotlib Documentation](https://matplotlib.org/stable/index.html) \

[Numpy documentation](https://numpy.org/doc/1.26/) \

----

### **Authors and Acknowledgment:**

----

### Copyright

N. James George © 2023. All Rights Reserved.
