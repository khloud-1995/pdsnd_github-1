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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Please choose the city you need information about from this list : chicago ,new york city , washington : ')
        city=city.lower()
        if city not in CITY_DATA :
            print('Please Enter a Correct City ')
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month=input('Please choose the month you want information about from this list : all, january, february,merch ,april , may, june : ')
        month=month.lower()
        month_list=['january', 'february','march' ,'april' , 'may', 'june']
        if month != 'all' and month not in month_list :
            print('Please Enter a Correct Month ')
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Please choose the day of week you want information about from this list : all, sunday, monday,tuesday,wednesday,thursday,friday,saturday : ').lower()
    #day=day.lower()
        day_list=['sunday', 'monday','tuesday','wednesday','thursday','friday','saturday']
        if day != 'all' and day not in day_list :
            print('Please Enter a Correct Day ')
        else:
            break
    #print(city, month, day)
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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['month_name']=df['Start Time'].dt.month_name()
    df['day']=df['Start Time'].dt.day_name()
    #print(df)
    if month == 'all' and day == 'all':
     #print ("correct")  this is used to check the result 
     return df
 
    elif month == 'all' and day !='all':
     df=df[df['day']== day.title()]
     return df
 
    elif month != 'all' and day =='all':
     df=df[df['month_name']==month]
     return df
    else:
     df=df[df['month_name']==month & df['day']== day.title()]
     return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month_name'].mode()[0]
    print('the commonly month is : ', common_month )

    # display the most common day of week -> we used the mode to show the value 
    common_day=df['day'].mode()[0]

    # display the most common start hour
    df['Start_hour']=df['Start Time'].dt.hour
    common_hour=df['Start_hour'].mode()[0]

    
    print('the commonly day of week is : ', common_day )
    print('the commonly start hour is : ', common_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    commen_Start_St=df['Start Station'].mode()[0]

    # display most commonly used end station
    commen_end_St=df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip -> we compine the stations to find the mode compination 
    df['Start_End_Stations']=(df['Start Station']+ ' - ' + df['End Station'])
    comment_start_end_St=df['Start_End_Stations'].mode()[0]
    

    print('the commonly start station is : ', commen_Start_St )
    print('the commonly end station is : ', commen_end_St )
    print('the most frequent combination of start station and end station : ', comment_start_end_St )
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('the total travel time in seconds is : ', total_travel_time )

    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('the mean travel time in seconds is : ', mean_travel_time )
    

    print("\nThis took %s seconds." , (time.time() - start_time))
    print('-'*40)


def user_stats(df): 
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types 
    total_users=df['User Type'].count()

    print('the counts of users is : ', total_users )
    print('the counts of users type is :\n ',df['User Type'].value_counts() )

    # Display counts of gender 
    if 'Gender' in df:
        Blank_Values=df.isnull().sum()
        print('the counts of users Gender is :\n ', df['Gender'].value_counts() )
    else :
        print('sorry this City has no gender information')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year=df['Birth Year'].min()
        recent_year=df['Birth Year'].max()
        common_year=df['Birth Year'].mode()[0]
        print('the earliest year of birth is : ', earliest_year )
        print('the recent year of birth is : ', recent_year )
        print('the common year of birth is : ', common_year )
        print('the Blank values are : \n', Blank_Values )
    else :
        print('sorry this City has no Birth Year information')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def Raw_Data(df): 
  """Displays Raw data of bikeshare."""
  print('\n show Raw Data...\n')
  start_time = time.time()
   
  i=0
  Answer=input('Do you want to view 5 Raws of the origenal Data ? Yes / No \n').lower()

  while True:
       if Answer=='yes':
         print('Raw Data : \n',df.iloc[i:i+5])
         Answer=input('Do you want to view 5 Raws of the origenal Data ? Yes / No \n').lower()
         i=i+5
       else:
         break
    
   
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
        Raw_Data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
