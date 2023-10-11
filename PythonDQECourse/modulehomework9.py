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
import csv
import xml.etree.ElementTree as ET



class NewsGenerator:
    def __init__(self):
        self.feed_data = []

    def adding_news(self, text="default_text", city="default_city"):              #this is news function where we can add news
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #adding current date and time
        self.feed_data.append({"type": "News", "text": text, "city": city, "timestamp": timestamp})
        self.publish_feed()

    def adding_private_ad(self, text="default_text", expiration_date_str="2023-12-31"):        #this is private add function where we can add add
        try:
            expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d")
            days_left = (expiration_date - datetime.now()).days
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        self.feed_data.append({"type": "Private Ad", "text": text, "expiration_date": expiration_date_str, "days_left": days_left})
        self.publish_feed()   #calling the function


    def publish_feed(self):

        file_name = 'default_folder/News$PrviateAd.csv'  #it will be the file name
        file_exists = os.path.isfile(file_name)

        # Open the file in append mode if it exists, or create it if it doesn't
        with open(file_name, "a" if file_exists else "w") as file:
            if not file_exists:
                # If the file is newly created, write an opening bracket to start a JSON array
                file.write("[")

            # Write the feed data
            if file_exists:
                file.write(",\n")  # Separate records with a comma and newline for an existing file
                json.dumps(file, indent=4)

            if not file_exists:
                # If it's a new file, write a closing bracket to finish the JSON array
                file.write("]")
        with open(file_name, "r") as file:
            # Read the file contents
                 file_contents = file.read()
        # Convert the contents to lowercase
        lowercase_contents = file_contents.lower()
        print(lowercase_contents)
        # Count letters (alphabetic characters)
        letter_count = sum(1 for char in file_contents if char.isalpha())

        # Count all words
        words = file_contents.split()
        total_characters = len(words)

        # Count uppercase letters
        uppercase_count = sum(1 for char in file_contents if char.isupper())

        # percentage of uppercase letters
        percentage_uppercase = (uppercase_count / letter_count) * 100 if letter_count > 0 else 0

        # Create a list with the results and headers
        results = [
                    ["Total letters", letter_count],
                    ["Total characters", total_characters],
                    ["Total uppercase letters", uppercase_count],
                    ["Percentage of uppercase letters", f"{percentage_uppercase:.2f}%"]
                 ]

        # Define the CSV file name
        csv_file_name ='default_folder/results.csv'

        # Write the results to a CSV file with headers
        with open(csv_file_name, "w", newline="") as csv_file:
            headers =['Total_letters','Total_characters','Total_uppercase_letters','Percentage_of_uppercase_letters']
            test_write = csv.DictWriter(csv_file, fieldnames=headers,quotechar="'", delimiter =";",quoting=csv.QUOTE_ALL)
            test_write.writeheader()
            writer = csv.writer(csv_file)
            writer.writerows(results)

        print(f"Results written to '{csv_file_name}' as a CSV file with headers.")
        print("News Generator")

def run():
        news_feed_tool = NewsGenerator()
        data_loader = FeedDataLoader()
        publication_loader = JSONProcessor()
        choice = input("Enter the type of news record (News/privateAd/RecordsTextFile/publication/recordsxmlfile): ").lower()
        # choice = sys.argv[0]
        if choice == 'news':
            text = input("Enter the news text: ") or "default_text"  #getting input from user
            city = input("Enter the city: ") or "default_city"
            news_feed_tool.adding_news(text, city)
        elif choice == 'privatead':
            text = input("Enter the ad text: ") or "default_text"
            expiration_date_str = input("Enter the expiration date (YYYY-MM-DD): ") or "2023-12-31"  #here we can add expiration date
            news_feed_tool.adding_private_ad(text, expiration_date_str)
        elif choice == 'recordstextfile':
            file_name = input("Enter the name of the text file to load: ") or "module6text.txt"
            folder_name = input("Enter the folder (test_new_module_6 if empty): ") or "default_folder"
            title = input("To days Latest News") or "default_title"
            text = input("We have won the Match") or "default_text"
            data_loader.load_records(file_name, folder_name, title, text)
        elif choice == 'publication':
            file_name = input("Enter the name of file (default_file if empty): ") or "module8json.json"
            folder_name = input("Enter the name of folder (default_folder if empty): ") or "default_folder"
            title = input("Enter the Publication title (default_title if empty):") or "default_title"
            text = input("Enter the Publication text (default_text if empty):") or "default_text"
            exp_date = input("Enter the Publication expiration date (YYYY-MM-DD) (2023-12-31 if empty):") or "2023-12-31"
            publication_loader.load_json_records(file_name, folder_name, title, text,exp_date)
        elif choice == 'recordsxmlfile':
            file_name = input("Enter the name of file (default_file if empty): ") or "default_file.xml"
            folder_name = input("Enter the name of folder (default_folder if empty): ") or "default_folder"
            idd = input("Enter the Publication title (default_id if empty):") or "default_id"
            title = input("Enter the Publication title (default_title if empty):") or "default_title"
            author = input("Enter the Publication author (default_author if empty):") or "default_author"
            price = input("Enter the Publication price (default_$122 if empty):") or "$122"
            description = input("Enter the Publication description (default_description if empty):") or "default_description"
            expdate = input("Enter the Publication expiration date (YYYY-MM-DD) (2023-12-31 if empty):") or "2023-12-31"
            xmlProcessor.create_or_update_xml(file_name, folder_name, idd,title, author, expdate,price,description)
        else:
            print("Invalid choice. Please select a valid option.")

class xmlProcessor:
    def create_or_update_xml(file_name1 = 'default_file.xml', folder_name = 'default_folder',idd = 'default_id', title = 'default_title', author = 'default_author',
                             expdate = '2023-12-31',price = '$122',description = 'default_description'):

    # Check if the  folder exists

        try:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                print(f"Folder '{folder_name}' created.")
            else:
                print(f"Folder '{folder_name}' already exists.")
            file_name = os.path.join(folder_name, file_name1)

        except Exception as e:
            print(f"Error loading records from '{file_name}': {str(e)}")

        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        # If file exists
            tree = ET.parse(file_name)
            root = tree.getroot()
        else:
        # If file doesn't exist, create a new root element
            root = ET.Element("book_catalog")
            tree = ET.ElementTree(root)

    # Get user input for book details
        book = ET.Element("book", id = idd)
        bauthor = ET.Element("author")
        bauthor.text = author
        btitle = ET.Element("title")
        btitle.text = title
        bexpdate = ET.Element("expdate")
        bexpdate.text = expdate
        bprice = ET.Element("price")
        bprice.text = price
        bdescription = ET.Element("description")
        bdescription.text = description

    # Add book elements to the root
        book.extend([bauthor, btitle, bexpdate, bprice, bdescription])
        root.append(book)
        ET.dump(root)
    # Indentation
        indent(root)

    # Save the updated XML to the file
        tree.write(file_name, xml_declaration=True, encoding="utf-8")

def indent(elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

class FeedDataLoader:
    def __init__(self):
        self.feed_data = []

    def load_records(self, file_name ="module6text.txt", folder_name="default_folder", title = "default_title", text = "default_text"):
        self.feed_data.append({"type": "News", "text": title, "city": text})
        try:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                print(f"Folder '{folder_name}' created.")
            else:
                print(f"Folder '{folder_name}' already exists.")
            file_path = os.path.join(folder_name, file_name)

            if not os.path.exists(file_path):
                with open(file_path, "w") as file:
                    print(f"File '{file_name}' created inside '{folder_name}'.")
            else:
                print(f"File '{file_name}' already exists inside '{folder_name}'.")

            file_path = os.path.join(folder_name, file_name)
            self.load_records_function(file_path)

        except Exception as e:
            print(f"Error loading records from '{file_name}': {str(e)}")

    def load_records_function(self,file_path):
        with open(file_path, "a") as file:
            if file_path:
                file.write(",\n")  # Separate records with a comma and newline for an existing file
                json.dump(self.feed_data, file, indent=4)
                    # file.write(title"\n")
                    # file.write("Record 2\n")
                    # file.write("Record 3\n")
                    # file.write("Record 4\nRecord 5\nRecord 6\n")
                    # print(file)
        with open(file_path, "r") as file:
                file_contents = file.read()
                case_normalize = file_contents.lower()
                print(case_normalize)
        os.remove(file_path)
        print(f"File '{file_path}' removed.")

class JSONProcessor:
    def __init__(self):
        self.feed_data = {}
    def load_json_records(self,file_name = 'module8json.json', folder_name = 'default_folder', title = 'default_title', text = 'default_text',exp_date = '2023-12-31'):
        self.feed_data = {"type": "Publication", "title": title, "text": text, "exp_date": exp_date}
        self.publish_json_feed(file_name,folder_name)

    def publish_json_feed(self,file_name,folder_name):
        try:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                print(f"Folder '{folder_name}' created.")
            else:
                print(f"Folder '{folder_name}' already exists.")
            file_path = os.path.join(folder_name, file_name)

                # Check if the JSON file exists
            if os.path.exists(file_path):
        # If the file exists, load the existing JSON data
                with open(file_path, "r") as json_file:
                    records_dict = json.load(json_file)
            else:
         # If the file doesn't exist, initialize an empty dictionary
                records_dict = {}

        # Determine the next sequential key
            next_key = str(len(records_dict) + 1)
            # Add the sample record to the dictionary with the next sequential key
            records_dict[next_key] = self.feed_data

        # Save the updated JSON data to the JSON file
            with open(file_path, "w") as json_file:
                json.dump(records_dict, json_file, indent=4)

            print(f"JSON data updated and saved to '{file_path}'")

        except Exception as e:
            print(f"Error loading records from '{file_name}': {str(e)}")

if __name__ == "__main__":
    run()

