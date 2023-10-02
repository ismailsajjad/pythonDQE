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
import sys


class NewsGenerator:
    def __init__(self):
        self.feed_data = []

    def adding_news(self, text, city):              #this is news function where we can add news
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #adding current date and time
        self.feed_data.append({"type": "News", "text": text, "city": city, "timestamp": timestamp})
        self.publish_feed()

    def adding_private_ad(self, text, expiration_date_str):        #this is private add function where we can add add
        try:
            expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d")
            days_left = (expiration_date - datetime.now()).days
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        self.feed_data.append({"type": "Private Ad", "text": text, "expiration_date": expiration_date_str, "days_left": days_left})
        self.publish_feed()   #calling the function


    def publish_feed(self):

        file_name = 'test_new_module_6/Latest_News'  #it will be the file name
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
            print("News Generator")


def run():
        news_feed_tool = NewsGenerator()
        data_loader = FeedDataLoader()
        choice = input("Enter the type of news record (News/privateAd/RecordsTextFile): ").lower()
        # choice = sys.argv[0]
        if choice == 'news':
            text = input("Enter the news text: ")   #getting input from user
            city = input("Enter the city: ")
            news_feed_tool.adding_news(text, city)
        elif choice == 'privatead':
            text = input("Enter the ad text: ")
            expiration_date_str = input("Enter the expiration date (YYYY-MM-DD): ")  #here we can add expiration date
            news_feed_tool.adding_private_ad(text, expiration_date_str)
        elif choice == 'recordstextfile':
            file_name = input("Enter the name of the text file to load: ") or "ismail6.txt"
            folder_name = input("Enter the folder (test_new_module_6 if empty): ") or "default_folder"
            data_loader.load_records(file_name, folder_name)
        else:
            print("Invalid choice. Please select a valid option.")



class FeedDataLoader:
    def __init__(self):
        self.feed_data = []

    def load_records(self, file_name ="ismail6.txt", folder_name="default_folder"):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created.")
        else:
            print(f"Folder '{folder_name}' already exists.")
        file_path = os.path.join(folder_name, file_name)

        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
    # Optionally, write data to the file here
                print(f"File '{file_name}' created inside '{folder_name}'.")
        else:
                print(f"File '{file_name}' already exists inside '{folder_name}'.")
        try:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                print(f"Folder '{folder_name}' created.")
            else:
                print(f"Folder '{folder_name}' already exists.")
            file_path = os.path.join(folder_name, file_name)
            with open(file_path, "a") as file:
                    file.write("Record 1\n")
                    file.write("Record 2\n")
                    file.write("Record 3\n")
                    file.write("Record 4\nRecord 5\nRecord 6\n")
                    print(file)
            with open(file_path, "r") as file:
                    file_contents = file.read()
                    case_normalize = file_contents.lower()
                    print(case_normalize)
            os.remove(file_path)
            print(f"File '{file_path}' removed.")

        except Exception as e:
            print(f"Error loading records from '{file_name}': {str(e)}")

if __name__ == "__main__":
    run()
    # news_feed_tool = NewsGenerator()
    # news_feed_tool.run()
#additional class which allow to provide records by text file
# 1. Define input formate (one or many records)
# 2. default folder or user provided folder
# 3. Remove file if its successfully created
# 4. Apply case normalization function

