import json
import pandas as pd
import mysql.connector


#Load database configuration from config.json
with open('config.json') as file:
    config = json.load(file)

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(**config)
    print("Database connection successful")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

# Load data from mysql database into a pandas DataFrame
query = "SELECT * FROM weather"
df = pd.read_sql(query, connection)
print("Data loaded into DataFrame") 

# Display the first few rows of the DataFrame
#print(df.head(10))
# Display DataFrame information
#print(df.info())
# Display summary statistics of the DataFrame
#print(df.describe())    


#day with the highest temperature
max_temp_row = df.loc[df['temp'].idxmax()]
print(f"Day with highest temperature: {max_temp_row['recorded_at']} with temperature {max_temp_row['temp']}")

# average humidity
average_humidity = df['humidity'].mean()
print(f"Average humidity: {average_humidity}")

# rows where temp > 30 and rainfall > 0
high_temp_rainfall = df[(df['temp'] > 30) & (df['rainfall'] > 0)]
print("Days with temperature > 30 and rainfall > 0:")
print(high_temp_rainfall)

# average temp per location
average_temp_per_location = df.groupby('location')['temp'].mean()
print("Average temperature per location:")
print(average_temp_per_location)

# line grapgh of temp vs recorded_at
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
for location, group in df.groupby('location'):
    plt.plot(group['recorded_at'], group['temp'], label=location)
plt.xlabel('Recorded At')
plt.ylabel('Temperature')
plt.title('Temperature over Time by Location')
plt.legend()
plt.show()


# bar chart for average humidity per location
average_humidity_per_location = df.groupby('location')['humidity'].mean()
average_humidity_per_location.plot(kind='bar', figsize=(10, 5))
plt.xlabel('Location')
plt.ylabel('Average Humidity')
plt.title('Average Humidity per Location')
plt.show()

# close the database connection
connection.close()
print("Database connection closed")
