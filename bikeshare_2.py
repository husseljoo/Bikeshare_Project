import time
import pandas as pd
import numpy as np
import datetime
from datetime import date
import calendar


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
dayList = ['all','Sunday','Monday',' Tuesday','Wednesday','Thursday','Friday']
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
           if(city in CITY_DATA):
               break
           print("Enter a correct city:")
       except:
           print("Enter a correct city:")


    print("Enter a particular month or all if you wish to inspect all months: ")
    month=""
    while(True):
        try:
            month=input("").lower()
            if((month in month_dict) or month=="all"):
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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Weekday'] = df['Start Time'].dt.day_name()
    df['Month'] = df['Start Time'].dt.month

    if month!="all":
        month_number=month_dict[month]
        df=df[df['Month']==month_number]
    if day!="all":
        df=df[df['Weekday']==day]

    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    if month=='all':
        max_month=df['Month'].value_counts().idxmax()
        for key,val in month_dict.items():
            if val==max_month:
                max_month=key
                break
        print("The most common month is {}".format(max_month.capitalize()))

    # display the most common day of week

    if day=='all':
        max_day=df['Weekday'].value_counts().idxmax()
        print("The most common weekday is {}".format(max_day))

    # display the most common start hour

    df['Hour']=df['Start Time'].dt.hour
    max_hour=df['Hour'].value_counts().idxmax()
    print("The most common hour is {}".format(max_hour))

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    max_start_station=df['Start Station'].value_counts().idxmax()
    print("The most common start station is {}".format(max_start_station))

    # display most commonly used end station

    max_end_station=df['End Station'].value_counts().idxmax()
    print("The most common end station is {}".format(max_end_station))

    # display most frequent combination of start station and end station trip

    max_comb=df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most common start/end station combination is {} and {}".format(max_comb[0],max_comb[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    sum_trip=df['Trip Duration'].sum()
    print("The total of the trip is {}".format(sum_trip))

    # display mean travel time
    mean_trip=df['Trip Duration'].mean()
    print("The mean of the trip is {}".format(mean_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print("User Type Counts is :")
    user_series=df.groupby(['User Type']).size()
    user_index=list(user_series.index)
    user_values=list(user_series.tolist())
    user_display=list(zip(user_index,user_values))

    for a,b in user_display:
        print("{}: {}".format(a,b))

    # Display counts of gender
    if (city!="washington"):
        print("\nGender Counts is :")
        gender_series=df.groupby(['Gender']).size()
        gender_index=list(gender_series.index)
        gender_values=list(gender_series.tolist())
        gender_display=list(zip(gender_index,gender_values))
        for a,b in gender_display:
            print("{}: {}".format(a,b))

    # Display earliest, most recent, and most common year of birth
        print()
        early_year=df['Birth Year'].min()
        print("The earliest birth year is {}\n".format(int(early_year)))

        latest_year=df['Birth Year'].max()
        print("The latest birth year is {}\n".format(int(latest_year)))

        common_year=df['Birth Year'].value_counts().idxmax()
        print("The most birth year is {}\n".format(int(common_year)))


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def correctDay(day):
    if day in dayList:
        return True
    return False

def main():
    while True:
        city, month, day = get_filters()
        print("City: {} Month: {} Day: {} ".format(city,month.capitalize(),day))
        df = load_data(city, month, day)
        if df.empty:
            print("There is no data that satisifies the criteria you chose!")
        else:
            time_stats(df,month,day)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df,city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

