import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Enter the name of the city you want to analyze (Chicago, New York City or Washington): ')).lower()
        
        if city not in CITY_DATA:
            print('{} is not a valid city. Please choose Chicago, New York City or Washington'.format(city))
            continue 
        else:
            print('You choose {}'.format(city).title())
            break 

    # get user input for month (all, january, february, ... , june)
    MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    while True:
        month = str(input('Enter the name of the month to filter by (january to june), or \'all\' to apply no month filter: ')).lower()
        
        if month not in MONTH_DATA:
            print('{} is not a valid month. Please choose any month from january to june, or \'all\' to apply no month filter'.format(month))
            continue 
        else:
            print('You choose {}'.format(month).title())
            break 

    # get user input for day of week (all, monday, tuesday, ... sunday)
    WEEKDAY = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        day = str(input('Enter the name of the day of week to filter by, or \'all\' to apply no day filter: ')).lower()
        
        if day not in WEEKDAY:
            print('{} is not a valid day of week. Please choose any day, or \'all\' to apply no day filter'.format(weekday))
            continue 
        else:
            print('You choose {}'.format(day).title())
            break 

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['Week Day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june'] 
        imonth = months.index(month) + 1
        df = df[df['month'] == imonth]

    if day != 'all':
        df = df[df['Week Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: ', common_month)

    # display the most common day of week
    common_day = df['Week Day'].mode()[0]
    print('The most common day of week is: ', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour of the day is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', end_station)

    # display most frequent combination of start station and end station trip
    df['comb'] = df['Start Station'] + ' to ' + df['End Station']
    comb_station = df['comb'].mode()[0]
    print('The most frequent combination of start staton and end station trip is: ', comb_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_trav_time = df['Travel Time'].sum()
    print('The total travel time is: ', total_trav_time)

    # display mean travel time
    avg_trav_time = df['Travel Time'].mean()
    print('The average travel time is: ', avg_trav_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The number of users by type of count is: ', user_type)

    # Display counts of gender
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print('The number of users by gender is: ', user_gender)
    else:
        print('Gender information is not available for this city')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earl_birth_yr = df['Birth Year'].min()
        print('The earlies birth year is: ', earl_birth_yr)
    else:
        print('Year of birth information is not available for this city')

    if 'Birth Year' in df:
        rec_birth_yr = df['Birth Year'].max()
        print('The most recent birth year is: ', rec_birth_yr)
    else:
        print('Year of birth information is not available for this city')
    
    if 'Birth Year' in df:
        common_birth_yr = df['Birth Year'].mode()[0]
        print('The most common birth year is: ', common_birth_yr)
    else:
        print('Year of birth information is not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
