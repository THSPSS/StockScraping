from stock import StockScraper


url = "http://www.judal.co.kr/?view=themeItem&themeIdx=92"
userSelector = ".themeNameTitleBox"
file_path = "stock_military.txt"


stockscraper = StockScraper(url , userSelector , file_path)
stockscraper.write_data_to_file()

