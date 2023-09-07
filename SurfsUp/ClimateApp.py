#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#*******************************************************************************************
 #
 #  File Name:  ClimateApp.py
 #
 #  File Description:
 #      This Python script, ClimatePy.ipynb, is a Flask API based on the queries 
 #      in ClimatePy.ipynb.  Here is a list of the functions for each route:
 #
 #      all_available_routes
 #      precipitation
 #      stations
 #      tobs
 #      start_route
 #      start_end_route
 #      
 #      Here is a list of support functions:
 #      
 #      ReturnMostActiveStationIDAsString
 #      ReturnDateOneYearPriorAsString
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  09/06/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyFunctions as function

import datetime as dt
import numpy as np

from flask import Flask, jsonify

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[ ]:


CONSTANT_LOCAL_FILE_NAME \
    = 'ClimateApp.py'

CONSTANT_SQL_LITE_DATABASE_FILE \
    = "sqlite:///Resources/hawaii.sqlite"


# In[ ]:


#################################################
# Database Setup
#################################################

# This line of code generates the engine to the correct sqlite file.
engineSQLAlchemyEngineObject \
    = create_engine \
        (CONSTANT_SQL_LITE_DATABASE_FILE)


# This line of code reflects an existing database schema into a new model.
baseSQLAlchemyDeclarativeMetaObject \
    = automap_base()


# This line of code reflects the database tables.
baseSQLAlchemyDeclarativeMetaObject \
    .prepare \
        (engineSQLAlchemyEngineObject, 
         reflect \
             = True)


# These lines of code save the references to the tables in the sqlite file .
stationSQLAlchemyDeclarativeMetaObject \
    = baseSQLAlchemyDeclarativeMetaObject \
        .classes \
        .station

measurementDeclarativeMetaObject \
    = baseSQLAlchemyDeclarativeMetaObject \
        .classes \
        .measurement


# Each function correctly creates and binds the session 
# between the python app and database (see below).


# In[ ]:


#################################################
# Flask Setup
#################################################
appFlaskAppObject = Flask(__name__)


# In[ ]:


#################################################
# Support Functions
#################################################

#*******************************************************************************************
 #
 #  Function Name:  ReturnMostActiveStationIDAsString
 #
 #  Function Description:
 #      This function returns the ID for the most active station.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnMostActiveStationIDAsString():
    
    try:
        
        sessionSQLAlchemySessionObject \
            = Session \
                (engineSQLAlchemyEngineObject)
        
        mostActiveStationsListOfSQLAlchemyEngineRowObject \
            = sessionSQLAlchemySessionObject \
                .query \
                    (measurementDeclarativeMetaObject \
                        .station, 
                     func \
                        .count \
                            (measurementDeclarativeMetaObject \
                                .station)) \
                        .group_by \
                            (measurementDeclarativeMetaObject \
                                .station) \
                        .order_by \
                            (func \
                                .count \
                                    (measurementDeclarativeMetaObject \
                                        .station) \
                                    .desc()) \
                    .all()
        
        sessionSQLAlchemySessionObject \
            .close()
            
        return \
            mostActiveStationsListOfSQLAlchemyEngineRowObject[0][0]
    
    except:
        
        return \
            'USC00519281'


# In[ ]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnDateOneYearPriorAsString
 #
 #  Function Description:
 #      This function returns the date one year prior to the most recent date 
 #      in the data set.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnDateOneYearPriorAsString():
    
    try:

        sessionSQLAlchemySessionObject \
            = Session \
                (engineSQLAlchemyEngineObject)
        
        mostRecentDatesSQLAlchemyEngineRowObject \
            = sessionSQLAlchemySessionObject \
                .query \
                    (measurementDeclarativeMetaObject \
                        .date) \
                        .order_by \
                            (measurementDeclarativeMetaObject \
                                .date \
                            .desc()) \
                    .first()
        
        sessionSQLAlchemySessionObject \
            .close()
        
        
        
        mostRecentDateStringVariable \
            = mostRecentDatesSQLAlchemyEngineRowObject[0]
        
        
        return \
            function \
                .ReturnDateFromOneYearPriorAsString \
                    (mostRecentDateStringVariable)
        
    except:
        
        return \
            '2016-08-23'


# In[ ]:


#################################################
# Flask Routes
#################################################

#*******************************************************************************************
 #
 #  Flask API Route Name:  all_available_routes
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the route URL, '/'; the route lists all available routes in the
 #      Flask API.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/')
def all_available_routes():
    
    messageStringVariable \
        = f'WELCOME TO THE CLIMATE API!\n' \
        + f'Here is a list of the available routes:\n\n' \
        + f'* Precipitation:\n' \
        + f'  /api/v1.0/precipitation\n\n' \
        + f'* List of Stations:\n' \
        + f'  /api/v1.0/stations\n\n' \
        + f'* List of temperature observations for the previous year:\n' \
        + f'  /api/v1.0/tobs\n\n' \
        + f'* To calculate the minimum, average, and maximum temperatures\n' \
        + f'  for a specific start date:\n' \
        + f'  /api/v1.0/[start_date format:yyyy-mm-dd]\n\n' \
        + f'* To calculate the minimum, average, and maximum temperatures\n' \
        + f'  for a specific range of dates:\n' \
        + f'  /api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]\n\n'
    
    return \
        messageStringVariable


# In[ ]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  precipitation
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the precipitaton URL, '/api/v1.0/precipitation'; the route converts 
 #      the query results fromthe precipitation analysis (id est, retrieve only 
 #      the last 12 months of data) to a dictionary and return the JSON 
 #      representation to the caller.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/precipitation')
def precipitation():

    precipitationListOfDictionaries \
        = []
    
    
    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)

    # This line of code performs a query to retrieve the last twelve months 
    # of precipitation data.
    precipitationDataListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (measurementDeclarativeMetaObject \
                    .date, 
                 measurementDeclarativeMetaObject \
                    .prcp) \
                    .filter \
                        (measurementDeclarativeMetaObject.date >= ReturnDateOneYearPriorAsString()) \
                .all()
    
    sessionSQLAlchemySessionObject \
        .close()


    # This line of code creates a dictionary from the data and appends it to a List.
    for date, prcp in precipitationDataListOfSQLAlchemyEngineRowObject:
        
        precipitationDictionary \
            = {}
        
        precipitationDictionary \
            ['date'] \
                = date
        
        precipitationDictionary \
            ['prcp'] \
                = prcp
        
        precipitationListOfDictionaries \
            .append \
                (precipitationDictionary)

        
    # This line of code returns the JSON representation of the dictionary.
    return \
        jsonify \
            (precipitationListOfDictionaries)


# In[ ]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  stations
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the stations URL, '/api/v1.0/stations'; the route returns to the 
 #      caller the JSON representation of a list of stations.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/stations')
def stations():

    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)
    
    # This line of code performs a query to retrieve a list of stations.
    stationListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (stationSQLAlchemyDeclarativeMetaObject \
                    .station) \
                    .order_by \
                        (stationSQLAlchemyDeclarativeMetaObject \
                            .station) \
                .all()

    sessionSQLAlchemySessionObject \
        .close()

    
    # This line of code converts the List of SQLAlchemy Row Objects into a normal List.
    stationList \
        = list \
            (np \
                .ravel \
                    (stationListOfSQLAlchemyEngineRowObject))

    
    return \
        jsonify \
            (stationList)


# In[ ]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  tobs
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the tobs URL, '/api/v1.0/tobs'; the route converts the query results 
 #      of the dates and temperature observations of the most active station for 
 #      the previous year to a dictionary and returns the JSON representation 
 #      to the caller.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/tobs')
def tobs():
    
    tobsActiveStationListofDictionaries \
        = []
    
    
    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)

    # This line of code performs a query to retrieve the dates 
    # and temperature observations from the most active station.
    tobsListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (measurementDeclarativeMetaObject \
                    .date,
                 measurementDeclarativeMetaObject \
                    .tobs,
                 measurementDeclarativeMetaObject \
                    .prcp) \
                    .filter \
                        (measurementDeclarativeMetaObject.date >= ReturnDateOneYearPriorAsString()) \
                    .filter \
                        (measurementDeclarativeMetaObject.station == ReturnMostActiveStationIDAsString()) \
                            .order_by \
                                (measurementDeclarativeMetaObject \
                                    .date) \
                .all()

    sessionSQLAlchemySessionObject \
        .close()

    
    # This line of code creates a dictionary from the data and appends it to a List.
    for date, tobs, prcp in tobsListOfSQLAlchemyEngineRowObject:
        
        tobsDictionary \
            = {}
        
        tobsDictionary \
            ['date'] \
                = date
        
        tobsDictionary \
            ['tobs'] \
                = tobs
        
        tobsDictionary \
            ['prcp'] \
                = prcp
        
        tobsActiveStationListofDictionaries \
            .append \
                (tobsDictionary)

        
    # This line of code returns the JSON representation of the dictionary.
    return \
        jsonify \
            (tobsActiveStationListofDictionaries)


# In[ ]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  start_route
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the start URL, '/api/v1.0/<start_date>'; the route returns to the
 #      caller a JSON list of the minimum, maximum, and average temperatures 
 #      for a specified start date.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          startDateStringParameter
 #                          This input parameter is the start date of the query.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/<start_date>')
def start_route \
        (startDateStringParameter):
   
    temperaturesListOfDictionaries \
        = []


    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)

    # This line of code performs a query to retrieve the temperature metrics
    # based on a start date.
    temperaturesListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (func \
                    .min \
                        (measurementDeclarativeMetaObject \
                            .tobs), 
                 func \
                    .max \
                        (measurementDeclarativeMetaObject \
                            .tobs), 
                 func \
                    .avg \
                        (measurementDeclarativeMetaObject \
                            .tobs)) \
                    .filter \
                        (measurementDeclarativeMetaObject.date >= startDateStringParameter) \
                .all()

    sessionSQLAlchemySessionObject \
        .close()

    
    # This line of code creates a dictionary from the data and appends it to a List.
    for minTemp, maxTemp, avgTemp in temperaturesListOfSQLAlchemyEngineRowObject:
        
        temperaturesDictionary \
            = {}
        
        temperaturesDictionary \
            ['min_temp'] \
                = minTemp
        
        temperaturesDictionary \
            ['max_temp'] \
                = maxTemp
        
        temperaturesDictionary \
            ['avg_temp'] \
                = avgTemp
        
        temperaturesListOfDictionaries \
            .append \
                (tobsDictionary)

        
    # This line of code returns the JSON representation of the dictionary.
    return \
        jsonify \
            (temperaturesListOfDictionaries)


# In[ ]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  start_end_route
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the start URL, '/api/v1.0/<start_date>'; the route returns to the
 #      caller a JSON list of the minimum, maximum, and average temperatures 
 #      for a specified date range.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          startDateStringParameter
 #                          This input parameter is the start date of the query.
 #  String
 #          endDateStringParameter
 #                          This input parameter is the end date of the query.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/<start_date>/<end_date>')
def start_end_route \
        (startDateStringParameter, 
         endDateStringParameter):
    
    temperaturesListOfDictionaries \
        = []


    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)

    # This line of code performs a query to retrieve the temperature metrics
    # based on a date range.
    temperaturesListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (func \
                    .min \
                        (measurementDeclarativeMetaObject \
                            .tobs), 
                 func \
                    .max \
                        (measurementDeclarativeMetaObject \
                            .tobs), 
                 func \
                    .avg \
                        (measurementDeclarativeMetaObject \
                            .tobs)) \
                    .filter \
                        (measurementDeclarativeMetaObject.date >= startDateStringParameter) \
                    .filter \
                        (measurementDeclarativeMetaObject.date <= endDateStringParameter) \
                .all()

    sessionSQLAlchemySessionObject \
        .close()

    
    # This line of code creates a dictionary from the data and appends it to a List.
    for minTemp, maxTemp, avgTemp in temperaturesListOfSQLAlchemyEngineRowObject:
        
        temperaturesDictionary \
            = {}
        
        temperaturesDictionary \
            ['min_temp'] \
                = minTemp
        
        temperaturesDictionary \
            ['max_temp'] \
                = maxTemp
        
        temperaturesDictionary \
            ['avg_temp'] \
                = avgTemp
        
        temperaturesListOfDictionaries \
            .append \
                (tobsDictionary)

        
    # This line of code returns the JSON representation of the dictionary.
    return \
        jsonify \
            (temperaturesListOfDictionaries)


# In[ ]:


if __name__ == '__main__': 
    appFlaskAppObject.run()


# In[ ]:




