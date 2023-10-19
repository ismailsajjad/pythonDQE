# Create a tool which will calculate straight-line distance between different cities based on coordinates:
#  1. User will provide two city names by console interface
#  2. If tool do not know about city coordinates, it will ask user for input and store it in SQLite database for future use
#  3. Return distance between cities in kilometers


import sqlite3
import math

# Function to create the SQLite database
def create_table_in_database():
    try:
        conn = sqlite3.connect('homework_coordinates.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cities (
                city_name TEXT PRIMARY KEY,
                latitude REAL,
                longitude REAL
            )
        ''')
        conn.commit()
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Function to retrieve city coordinates from the database
def get_coordinates_city(city_name):
    try:
        conn = sqlite3.connect('homework_coordinates.db')
        cursor = conn.cursor()
        sql_query = cursor.execute('SELECT latitude, longitude FROM cities WHERE city_name = ?', (city_name,))
    # print(sql_query)
        result = cursor.fetchone()
        print(result)
        return result
    except:
        print(f"Please check the citcy name: {city_name}")
        return None
# Function to store city coordinates in the database
def store_coordinates_city(conn,city_name, latitude, longitude):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO cities (city_name, latitude, longitude) VALUES (?, ?, ?)', (city_name, latitude, longitude))
        conn.commit()
    except Exception as e:
        print(f"Error loading connection'{conn}'")

# Function to calculate the distance between two cities
def calculate_distance(city1, city2, conn):
    city1_result = get_coordinates_city(city1)
    try:
        if city1_result is None:
            print(f"Coordinates for {city1} not found. Please provide them:")
            lat1 = float(input(f"Enter latitude for number of float{city1}: "))
            lon1 = float(input(f"Enter longitude for number of float{city1}: "))
            store_coordinates_city(conn,city1, lat1, lon1)
        else:
            var1, var2 = city1_result
        # Convert latitude and longitude from degrees to radians
            lat1 = math.radians(var1)
            lon1 = math.radians(var2)
    except:
        print(f"Please check the data in'{lat1,lon1}'")

    city2_result = get_coordinates_city(city2)
    try:
        if city2_result is None:
            print(f"Coordinates for {city2} not found. Please provide them:")
            lat2 = float(input(f"Enter latitude for number of float{city2}: "))
            lon2 = float(input(f"Enter longitude for number of float{city2}: "))
            store_coordinates_city(conn,city2, lat2, lon2)
        else:
            var1, var2 = city2_result
        # Convert latitude and longitude from degrees to radians
            lat2 = math.radians(var1)
            lon2 = math.radians(var2)
    except:
        print(f"Please check the data in'{lat2,lon2}'")
    # Radius of the Earth in kilometers
    radius = 6371

    # Haversine formula to calculate the distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance

if __name__ == "__main__":
    conn = create_table_in_database()
    city1 = input("Enter the name of the first city: ")
    city2 = input("Enter the name of the second city: ")
    distance = calculate_distance(city1, city2,conn)
    conn.close()
    print(f"The distance between {city1} and {city2} is approximately {distance:.2f} kilometers.")
