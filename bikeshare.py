import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter a city - Chicago, New York City, Washington : ").lower()
        if city not in cities:
            print("\nPlease provide one of the cities mentioned - Chicago, New York City, Washington")
            continue
        else:
            break
            
    # TO DO: get user input for month (all, january, february, march,... , june)        
    while True:
        month = input ("\nPlease enter a specific month to filter - january, february, march, april, may, june or type 'all' for no filter: ").lower()
        if month not in months:
            print("\nPlease provide one of the months mentioned to filter by month or 'all': ")
            continue
        else:
            break
            
    # TO DO: get user input for day of week (all, monday, tuesday, wednesday, ... sunday)
    while True:
        day = input("\nPlease enter a specific day of the week to filter or type 'all':\n").lower()
        if day not in days:
            print("\nSorry, provide a valid day of the week to filter by day or 'all'")
            continue
        else:
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
    
    # Load datafile into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month and day of the week to create a new column 
    df['month'] = df['Start Time'].dt.month 
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        
    # Filter by month to create a new data frame
        df = df[df['month'] == month]
        
    # Filter by day of week if applicable
        if day != 'all':
            df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month of the year
    common_month = df['month'].mode()[0]
    print("The most common month is:", common_month)
    
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is:", common_day_of_week)
          
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is:", common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most common start station is:", common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("The most common end station is:", common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most common start and end station is:", common_start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The Total traveled time is:", total_travel_time)
    

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average time traveled is:", mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user types:", user_types)
    
    
    # TO DO: Display counts of gender
    try:
        customer_gender = df['Gender'].value_counts()
        print("Count of the gender:", customer_gender)
    except KeyError:
        print("\nGender Type - Data not available for this city.")
              
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        print("\nEarliest Year:", earliest_year)
    except KeyError:
        print("\nBirth Year Information - Data not available for this city.")
        
     
    try:
      most_recent_year = int(df['Birth Year'].max())
      print('\nMost Recent Year:', most_recent_year)
    except KeyError:
      print("\nMost Recent Year - Birth Year Information:\nData not available for this city.")

    try:
      most_common_year_of_birth = int(df['Birth Year'].mode())
      print('\nMost Common Year of Birth:', most_common_year_of_birth)
    except KeyError:
      print("\nMost Common Year - Birth Year Information:\nData not available for this city.")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
            
            
    # Interactive user input to retieve user data. 5 rows will be displayed when the user chooses yes.
        user_records = input("\nWould you like to view the user records? 'yes' or 'no':\n").lower()
        if user_records in ('yes'):
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                more_user_records = input("\nWould you like to see more user records? 'yes' or 'no':\n").lower()
                if more_user_records != 'yes':
                        break  
        
    # Gets user input to restart from the beginning, giving the opportunity for the user to explore bikeshare data
        restart = input("\nWould you like to restart? 'yes' or 'no': \n").lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


