from bs4 import BeautifulSoup
import requests
import csv



class StockScraper:

    def __init__(self ,  url , userSelector , file_path):
        self.url = url
        self.userSelector = userSelector
        self.file_path = file_path

    def scrape_data(self):
        response = requests.get(self.url)
        stock_web_page = response.text

        soup = BeautifulSoup(stock_web_page,"html.parser")
        stock_td = soup.select(selector=self.userSelector)

        stock_li = []
        for stock in stock_td:
                titleText = stock.getText()
                stock_li.append(titleText)

        return stock_li

    def write_data_to_file(self):
        try:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for title in self.scrape_data():
                    writer.writerow([title])
        except IOError:
            print("Error writing to file")