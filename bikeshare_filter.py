"""I have actually done on my computer and pasting this here because the workspace provided here is bit slow  and this version is with tme filter and the other is without any time filter just the city filter."""
import csv
import pandas as pd
import time
import datetime
import collections
from collections import Counter
def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    cityname = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    cityname=cityname.lower()
    city_verify=cityname
    if (cityname=='newyork'):
      filename='new_york_city.csv'
      city_df=pd.read_csv(filename)
      return city_df,city_verify
    elif (cityname=='washington'):
      filename='washington.csv'
      city_df=pd.read_csv(filename)
      return city_df,city_verify
    elif (cityname=='chicago'):
      filename='chicago.csv'
      city_df=pd.read_csv(filename)
      return city_df,city_verify
    else:
      print ("Enter only the above given names only")
      exit()
def popular_month(city_file):
    '''This function calculates the month that occurs most often in the start time'''
    city_file["Start Time"] = pd.to_datetime(city_file["Start Time"])
    months= city_file["Start Time"].dt.month
    countmonths= Counter(months)
    max_month=countmonths.most_common()[0:1]
    for x in max_month:
      if (x[0]==1):
        y= 'January'
      elif (x[0]==2):
        y='February'
      elif (x[0]==3):
        y='March'
      elif (x[0]==4):
        y='April'
      elif (x[0]==5):
        y='May'
      elif (x[0]==6):
        y='June'
      elif (x[0]==7):
        y='July'
      elif (x[0]==8):
        y='August'
      elif (x[0]==9):
        y='September'
      elif (x[0]==10):
        y='October'
      elif (x[0]==11):
        y='November'
      elif (x[0]==12):
        y='December'
      print ("Month often seen in start time is {} month and count is {}".format (y,x[1]))
def popular_day(city_file):
    '''This function calculates the day that occurs most often in the start time
    It takes city dataframe as the argument'''
    city_file["Start Time"] = pd.to_datetime(city_file["Start Time"])
    days= city_file["Start Time"].dt.weekday
    countdays= Counter(days)
    max_day=countdays.most_common()[0:1]
    for x in max_day:
      if (x[0]==0):
        y= 'Sunday'
      elif (x[0]==1):
        y='Monday'
      elif (x[0]==2):
        y='Tuesday'
      elif (x[0]==3):
        y='Wednesday'
      elif (x[0]==4):
        y='Thursday'
      elif (x[0]==5):
        y='Friday'
      elif (x[0]==6):
        y='Saturday'
      print ("Day often seen in start time is {}  weekday and count is {}".format (y,x[1]))
def popular_hour(city_file):
    '''This function calculates the hour that occurs most often in the start time
     It takes city dataframe as the argument'''
    city_file["Start Time"] = pd.to_datetime(city_file["Start Time"])
    hours= city_file["Start Time"].dt.hour
    counthours= Counter(hours)
    max_hour=counthours.most_common()[0:1]
    for x in max_hour:
      print ("Day often seen in start time is {} th hour and count is {}".format (x[0],x[1]))
def popular_stations(city_file):
    '''This function calculates the popular start station and the end station
    It takes city dataframe as the argument'''
    start_station=city_file.groupby(["Start Station"]).size()
    end_station=city_file.groupby(["End Station"]).size()
    print ("The most comon start staion is {} and its count is{} ".format(start_station.idxmax(),start_station.max()))
    print ("The most common end station is {} and its count is {}".format(end_station.idxmin(),end_station.max()))
def popular_trip(city_file):
    '''This function calculates the popular trip between start station and the end station'''
    trip=city_file.groupby(["Start Station", "End Station"]).size()
    print ("The most common trip is between start station {} and end station {} and the count is {}".format(trip.idxmax()[0],trip.idxmax()[1],trip.max()))
def users(city_file):
    '''This function gives the  are the counts of each user type
     It takes city dataframe as the argument'''
    user=city_file['User Type'].tolist()
    coustomer=0
    subscriber=0
    for i in range(len(user)):
      if (user[i]=='Customer'):
        coustomer+=1
      elif (user[i]=='Subscriber'):
        subscriber+=1
    print ("Total number of coustomer users are {}".format(coustomer))
    print ("Total number of subscriber users are {}".format(subscriber))
def genders(city_file):
    '''This function gives the counts of each gender type
    It takes city dataframe as the argument'''
    gender=city_file['Gender'].tolist()
    male=0
    female=0
    for i in range(len(gender)):
      if (gender[i]=='Male'):
        male+=1
      elif (gender[i]=='Female'):
        female+=1
    print ("Total number of male users {}".format(male))
    print ("Total number of femlae users {}".format(female))
def trip_duration(city_file):
    '''This function gives the total and average duration of all the trips
    It takes city dataframe as the argument'''
    time_sec=city_file['Trip Duration'].sum()
    ave_time_sec=city_file['Trip Duration'].mean()
    print ("Total  time for trip durations in minutes is {} and in hours is {} and seconds is {}".format((time_sec)/60,(time_sec)/(60*60),time_sec))
    print ("Average time for trip durations in minutes is {} and in hours is {} and seconds is {}".format((ave_time_sec)/60,(ave_time_sec)/(60*60),ave_time_sec))
def birth_years(city_file):
    ''' This function gives the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    '''
    age=city_file['Birth Year']
    common_age=city_file.groupby(["Birth Year"]).size()
    print ("The earliest birth year was {}".format(int(age.max())))
    print ("The recent birth year was {}".format(int(age.min())))
    print ("The most comon birth year is {} and its count is{} ".format(common_age.idxmax(),common_age.max()))
def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        nonegiven    Returns:
        nonegiven    '''
    # Filter by city (Chicago, New York, Washington)7
    city,city_verify = get_city()
    city["Start Time"] = pd.to_datetime(city["Start Time"])
    time_period=input("do you want any filters to be applied that is month day or both or none \n")
    if (time_period=='month'):
        month_given=input("enter month as number for example January=1\n")
        if (1<=int(month_given)<=12):
          city=city.loc[(city['Start Time'].dt.month==int(month_given))]
        else:
          print ("Enter within the range")
          exit()
    elif (time_period=='day'):
      day_given=input("enter day as number for example Sunday=1\n")
      if (0<=int(day_given)<=6):
        city=city.loc[(city['Start Time'].dt.weekday==int(day_given))]
      else:
        print ("Enter with in range")
        exit()
    elif (time_period=='both'):
      month_given=input("Enter the month as number for example January=1 \n")
      day_given=input("enter day \n")
      if (bool(0<=int(day_given)<=6) & bool(1<=int(month_given)<=12)):
        city=city.loc[(city['Start Time'].dt.weekday==int(day_given)) & (city['Start Time'].dt.month==int(month_given))]
      else:
        print ("Enter with  in the range of days")
        exit()
    elif (time_period=='none'):
    	city=city
    else:
      print ("Enter a valid option")
      statistics()
        
    start_time = time.time()
    popular_month(city)

        #TODO: call popular_month function and print the results
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic that is popular day...")
    start_time = time.time()
    popular_day(city)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic that is popular hour...")
    popular_hour(city)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic that is popular stations both start and end...")
    popular_stations(city)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic that is poplar trip between start and end station...")
    popular_trip(city)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic that is count of users...")
    users(city)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic that is trip duration...")
    trip_duration(city)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic that is genders count...")
    if (city_verify=='washington'):
      print ("The column was not there for the current dataset")
      restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
      if restart.lower() == 'yes':
        statistics()
      else:
        print ("Exit Application done")
        exit()
    else:
      genders(city)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic that is recent and old birth years...")
    birth_years(city)
    print("That took %s seconds." % (time.time() - start_time))
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
      statistics()
    else:
        print ("Exit Application done")
statistics()

