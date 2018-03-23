from bs4 import BeautifulSoup
import requests
import os

"""
   Writes to a specified csv file
"""
def write_to_csv(filename, string_datas):
    with open(filename, 'a') as fopen:
        fopen.write((' | ').join(string_datas) + '\n')

"""
   Scrapes data from the US census bureau and stores it in a  
   specified csv file
"""
def main():
    location = "brownsvillecitytexas,US"
    
    # Get desired location data from US census bureau
    page = requests.get('https://www.census.gov/quickfacts/fact/table/'+ location +'/PST045217')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    filename = "test_data.csv"

    if(os.path.exists(filename)):
        os.remove(filename)

    # Get graph table
    div_tables = soup.find(class_='qf-facttable')
    tables = div_tables.find_all(class_='type')[1:]
    for index,table in enumerate(tables):
        sections = table.find_all('tbody')
        for section in sections:
            rows = section.find_all('tr')[1:]
            for row in rows:
                columns = row.find_all('td')
                string_columns = []
                for index, column in enumerate(columns):
                    if index == 0:
                        string_columns.append(column.find('span').contents[0])
                    else:
                        if(column.find('a')):
                            data = column.find('a')
                            if(data.contents[0] == "NA"):
                                string_columns.append('NA')
                            else:
                                string_columns.append('X')
                        else:
                            string_columns.append(column.contents[-1])
                write_to_csv(filename, string_columns)

                
if __name__ == "__main__":
    main()


