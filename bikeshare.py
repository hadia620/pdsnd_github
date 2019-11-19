import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('\\nWould you like to see data for Chicago, New York, or Washington?').lower()
    while(True):
        if(city == 'chicago' or city == 'new york' or city == 'washington' ):
            break
        else:
            city = input('Enter Correct city: ').lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nWhich month you want to explore? January , February , March , April , May , or June?\n").lower()
    while True:
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june'):
            break
        else:
          month = input('Enter valid month\\n').lower()
        #if month not in ('january' , 'february' , 'march' , 'april' , 'may' , 'june'):
           # print("\noops , month name is incorrect. Please type another month: \n").lower()
           # continue
        #else:
         #   break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('Which day ? monday, tuesday, wednesday, thursday, friday, saturday , sunday ?\n').lower()
    while(True):
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday'):
                break
        else:
                day = input('Enter Correct day: ').lower()
    
    
    #day = input("\nWhich day you want to explore? Monday , Tuesday , Wednesday , Thursday , Friday , Saturday , or Sunday?  \n").lower()
    #while True:
     #   if day not in ('monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday'):
      #      print("\noops , day name is incorrect. Please type another day: \n").lower()
       #     continue
        #else:
         #   break

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
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1 
        df = df[df['Start Time'].dt.month == month]
    
    df = df[df['Start Time'].dt.weekday_name == day.title()]
    print(df.head())
    # extract month and day of week from Start Time to create new columns
    #df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    #df = df[df['month'] == month]
    #df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    no_of_subscribers = df['User Type'].str.count('Subscriber').sum()
    no_of_customers = df['User Type'].str.count('Customer').sum()
    print('\\nNumber of subscribers are {}\\n'.format(int(no_of_subscribers)))
    print('\\nNumber of customers are {}\\n'.format(int(no_of_customers)))

    # TO DO: Display counts of gender
    if('Gender' in df):
        male_counter = df['Gender'].str.count('Male').sum()
        female_counter = df['Gender'].str.count('Female').sum()
        print('\\nNumber of male users are {}\\n'.format(int(male_count)))
        print('\\nNumber of female users are {}\\n'.format(int(female_count)))

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
        most_common_birth_year = st.mode(df['Birth Year'])
    try:
        print('\\n Oldest Birth Year is {}\\n Youngest Birth Year is {}\\n Most popular Birth Year is {}\\n'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))
    except TypeError:
        print('\\n Oldest Birth Year is {}\\n Youngest Birth Year is {}\\n Most popular Birth Year is {}\\n'.format(int(earliest_year), int(recent_year), most_common_birth_year))
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
