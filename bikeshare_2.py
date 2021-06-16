import time
import pandas as pd
import numpy as np
import datetime
from datetime import date
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

monthList = ['all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
dayList = ['all','Sunday','Monday',' Tuesday','Wednesday','Thursday','Friday']
cityList = ['chicago','washington','new york','new york city']
decisionList=['day','month','none','both']

month_dict={'january': 1,
 'february': 2,
 'march': 3,
 'april': 4,
 'may': 5,
 'june': 6,
 'july': 7,
 'august': 8,
 'september': 9,
 'october': 10,
 'november': 11,
 'december': 12}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Enter a city [chicago,new york or washington]:")
    city=""
    while(True):
       try:
           city=input("").lower()
           if(correctCity(city)):
               break
           print("Enter a correct city:")
       except:
           print("Enter a correct city:")

    # print("Would you like to filter the data by month, day,both or none:")
    # while(True):
    #     try:
    #         decision=input("").lower()
    #         if(correctDecision(decision)):
    #             break
    #         print("Enter a correct decision:")
    #     except:
    #         print("Enter a correct decision:")

    # get user input for month (all, january, february, ... , june)
    print("Enter a particular month or all if you wish to inspect all months: ")
    month=""
    while(True):
        try:
            month=input("").lower()
            if(correctMonth(month)):
                break
            print("Enter a correct month:")
        except:
            print("Enter a correct month:")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    print("Enter a weekday:")
    day=""
    while(True):
        try:
            day=input()
            if(correctDay(day)):
                break
            print("Enter a correct weekday (make sure first character is upper case):")
        except:
            print("Enter a correct weekday (make sure first character is upper case):")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print("City: {} Month: {} Day: {} ".format(city,month,day))
    if city=="chicago":
        df=pd.read_csv("chicago.csv")
    elif city=="washington":
        df=pd.read_csv("washington.csv")
    else:
        df=pd.read_csv("new_york_city.csv")

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month!="all":
        month_number=month_dict[month]
        df['Month'] = df['Start Time'].dt.month
        df=df[df['Month']==month_number]
    if day!="all":
        df=df[df['Weekday']==day]


    # if decision=="both":
    #     df[df['Month']==month_number & df['Weekday'] ==day]




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def correctCity(city):
    if city in cityList:
        return True
    return False

def correctDay(day):
    if day in dayList:
        return True
    return False

def correctDecision(decision):
    if decision in decisionList:
        return True
    return False

def correctMonth(month):
    if month in monthList:
        return True
    return False

def main():
    while True:
        city, month, day = get_filters()
        print("City: {} Month: {} Day: {} ".format(city,month,day))
        # city="chicago"
        # month="all"
        # day="all"
        df = load_data(city, month, day)
        print(df.head)
        # time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)
        # restart = input('\nWould you like to restart? Enter yes or no.\n')
        # if restart.lower() != 'yes':
        #     break


if __name__ == "__main__":
	main()
