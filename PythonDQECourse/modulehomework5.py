# Home Work:
# Create a tool which will do user generated news feeds:
# 1. User select what data type he want to add
# 2. Provide record type required data
# 3. Records is published on text file in special format

#Need to implement
# 1. News - text and city input.Data is calculated during publishing
# 2. Prictae ad - text and expiration date as input. Day left is calculated during publishing.
# 3. Your unique one with unique publish rules.

import json
import os
from datetime import datetime, timedelta

class NewsGenerator:
    def __init__(self):
        self.feed_data = []

    def adding_news(self):              #this is news function where we can add news
        text = input("Enter the news text: ")   #getting input from user
        city = input("Enter the city: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #adding current date and time
        self.feed_data.append({"type": "News", "text": text, "city": city, "timestamp": timestamp})
        self.publish_feed()

    def adding_private_ad(self):        #this is private add function where we can add add
        text = input("Enter the ad text: ")
        expiration_date_str = input("Enter the expiration date (YYYY-MM-DD): ")  #here we can add expiration date
        try:
            expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d")
            days_left = (expiration_date - datetime.now()).days
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        self.feed_data.append({"type": "Private Ad", "text": text, "expiration_date": expiration_date_str, "days_left": days_left})
        self.publish_feed()   #calling the function


    def publish_feed(self):

        file_name = 'Latest_News'           #it will be the file name
        file_exists = os.path.isfile(file_name)

        # Open the file in append mode if it exists, or create it if it doesn't
        with open(file_name, "a" if file_exists else "w") as file:
            if not file_exists:
                # If the file is newly created, write an opening bracket to start a JSON array
                file.write("[")

            # Write the feed data
            if file_exists:
                file.write(",\n")  # Separate records with a comma and newline for an existing file
            json.dump(self.feed_data, file, indent=4)

            if not file_exists:
                # If it's a new file, write a closing bracket to finish the JSON array
                file.write("]")

    def run(self):
        choice = input("Enter the type of news record (News/privateAd): ").lower()
        if choice == 'news':
            self.adding_news()
        elif choice == 'privateAd':
            self.adding_private_ad()
        else:
            print("Invalid choice. Please select a valid option.")

        print("News Generator")

if __name__ == "__main__":
    news_feed_tool = NewsGenerator()
    news_feed_tool.run()
