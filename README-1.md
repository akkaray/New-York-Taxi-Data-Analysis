# Taxi Assignment
 Taxi Assignment
1.What datetime range does your data cover?  How many rows are there total?
Changed the string of datetime to datetime object and found the max and min values of data,created a loop for 100000 columns for total number of rows
2.What are the field names?  Give descriptions for each field.Give some sample data for each field.
Printed the first 2 rows of data for the field names and the sample data to be displayed 
3.What MySQL data types / len would you need to store each of the fields?
int(xx), varchar(xx),date,datetime,bool, decimal(m,d)
have writen the column names and their corresponding data types in the excel sheet
4.What is the geographic range of your data (min/max - X/Y)?Plot this (approximately on a map)
Found the min and max of the 4 columns of lattitudes and longitudes,checked for the min and max values of the output,assigned the output to variables so as to retrive its corresponding items but the code did not work properly and i was unable to plot them as points,note:I have taken the lattitude as 0 to 180 and longitude range as 0 to 90 for drop_off lat and long as thats the complete range.
5.What is the average trip distance? (You should use Haversine Distance)Draw a histogram of the trip distances binned anyway you see fit.
Used the Haversine Distance formula and called it for the trip distance field and so found the average distance,but could not figure out on the binning process so did not plot the graph.
7.What are the distinct values for each field? (If applicable)
Used the key value method as showed in the previous assignments to find the unique values and print it into a dictionary 
8.For other numeric types besides lat and lon, what are the min and max values?
Used the max and min functions of python
9.Create a chart which shows the average number of passengers each hour of the day. (X axis should have 24 hours)
used split() to split the hours from date time and then used the keys method to get the number for each hour and created a graph in excel. 
![Image of chart](Images/Picture)
10.Create a new CSV file which has only one out of every thousand rows.
Created a new subset of csv using the writer with a column for every 1000 rows
11.Repeat step 9 with the reduced dataset and compare the two charts.
Used the same method as in step 9 to get another histogram of subsetfile,drew a graph in excel and compared the two graphs.
![Image of chart](Images/subset picture)
