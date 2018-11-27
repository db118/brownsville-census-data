from bs4 import BeautifulSoup
import requests
import os
from src import config


def write_to_csv(filename, string_data):
    """
    Writes to a specified csv file
    """
    with open(filename, 'a') as fopen:
        fopen.write((' | ').join(string_data) + '\n')


def is_cityname_in_title(page_selectors, city_name):
    h2_content = page_selectors.find(class_='qf-titlebar').h2.contents
    if h2_content:
        return str(h2_content[0]).lower().split(" ")[0] == city_name
    return False


def get_city_information(city_name, state_name):
    """
    Get a HTTP Response for a particular city and state
    """
    location = city_name + "city" + state_name + ",US"
    city_link = config.US_BUREAU['base_url'] \
        + location \
        + config.US_BUREAU['tag']
    city_information = requests.get(city_link)
    page_selectors = BeautifulSoup(city_information.content, 'html.parser')
    if not is_cityname_in_title(page_selectors, city_name):
        raise Exception('City information is not avaliable')
    return city_information


def clear_csv_file(filename):
    """
    Removes csv file
    """
    if os.path.exists(filename):
        os.remove(filename)


def get_row_information(info_columns):
    row_information = []
    for index, column in enumerate(info_columns):
        if index == 0:
            row_information.append(column.find('span').contents[0])
        else:
            if column.find('a'):
                row_information.append('X')
            else:
                row_information.append(column.contents[-1])
    return row_information


def get_html_tables(soup):
    # Get html graph table
    return soup.find(class_='qf-facttable').find_all(class_='type')[1:]


def main():
    """
    Scrapes data from the US census bureau and stores it in a
    specified csv file
    """
    filename = "test_data.csv"
    clear_csv_file(filename)
    city_information = get_city_information("brownsville", "texas")
    soup = BeautifulSoup(city_information.text, 'html.parser')
    html_tables = get_html_tables(soup)
    for table in html_tables:
        for section in table.find_all('tbody'):
            for row in section.find_all('tr')[1:]:
                string_columns = get_row_information(row.find_all('td'))
                write_to_csv(filename, string_columns)


if __name__ == "__main__":
    main()
