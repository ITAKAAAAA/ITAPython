from urllib import request

url_csv = 'https://sample-videos.com/csv/Sample-Spreadsheet-100-rows.csv'
def download_stock_data(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'googl.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(url_csv)