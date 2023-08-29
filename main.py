#3.1 How many seconds are in an hour?
seconds_in_a_minute = 60
minutes_in_an_hour = 60 
seconds_in_an_hour = seconds_in_a_minute * minutes_in_an_hour
print(seconds_in_an_hour)
#3.2 seconds in an hour change to seconds_per_hour.
seconds_per_hour = seconds_in_an_hour 
print (seconds_per_hour)
#3.3 How many seconds are in a day? 
hours_per_day = 24
seconds_are_in_a_day = seconds_per_hour * hours_per_day
print (seconds_are_in_a_day)
#3.4 calculate again and save the result in a variable called seconds_per_day
seconds_per_day = seconds_are_in_a_day
print (seconds_per_day)
#3.5 Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
division_result = seconds_per_day / seconds_per_hour
print (division_result)
#3.6 Divide seconds_per_day by seconds_per_hour, using integer (//) division
division_result = seconds_per_day // seconds_per_hour
print (division_result)
