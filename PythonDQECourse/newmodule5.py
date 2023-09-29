import json
from datetime import datetime, timedelta

class NewsFeedTool:
    def __init__(self):
        self.feed_data = []
        print("5")
    def publish_feed(self):
        return f"TEXT NEWS: {self.text}\n{self.city}\n{self.timestamp}\n"
        pass

    def TextNewsRecord(self):
        text = 'this is first text' #input("Enter the news text: ")
        city = 'warsaw is city'  #input("Enter the city: ")
        print("2")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("3")
        self.feed_data.append({"type": "News", "text": text, "city": city, "timestamp": timestamp})


    def PrivateAdRecord(self):
        text = input("Enter the ad text: ")
        expiration_date_str = input("Enter the expiration date (YYYY-MM-DD): ")
        expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d")
        days_left = (expiration_date - datetime.now()).days
        self.feed_data.append({"type": "Private Ad", "text": text, "expiration_date": expiration_date_str, "days_left": days_left})


    # def add_custom_record(self):
    #     custom_type = input("Enter the custom record type: ")
    #     # Define your custom record data collection logic here
    #     # For example:
    #     data = input("Enter custom record data: ")
    #     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     self.feed_data.append({"type": custom_type, "data": data, "timestamp": timestamp})

    def publish_feed(self):
        print("7")
        file_name = 'file_test_ismail'#input("Enter the file name to save the feed (e.g., news_feed.txt): ")
        with open(file_name, "w") as file:
            for record in self.feed_data:
                file.write(json.dumps(record) + '\n')
        print(f"Feed published to {file_name}")

    def create_and_publish_news_record(self):
            record_type = 'news' #input("Enter the type of news record (News/privateAd): ").lower()
            if record_type == "news":
                print("1")
                news_ismail =self.TextNewsRecord()
            elif record_type == "privateAd":
                self.PrivateAdRecord()
            else:
                print("Invalid record type.")
                return


            with open("news_feed.txt", "a") as file:
                file.write(news_ismail.publish_feed())
                print("News record published successfully.")

if __name__ == "__main__":
    news_feed_tool = NewsFeedTool()
    news_feed_tool.create_and_publish_news_record()
