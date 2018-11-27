from bs4 import BeautifulSoup
import requests
import os
from src import config


def write_to_csv(filename, string_data):
    """
    Writes to a specified csv file
    """
    with open(filename, 'a') as fopen:
        fopen.write(' | '.join(string_data) + '\n')


def is_cityname_in_title(page_selectors, city_name):
    h2_content = page_selectors.find(class_='qf-titlebar').h2.contents
    if not h2_content:
        return False
    return str(h2_content[0]).lower().split(" ")[0] == city_name


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


def get_row_information(info_columns):
    row_information = []
    if len(info_columns) == 0:
        return row_information
    row_information.append(info_columns[0].find('span').contents[0])
    for column in info_columns:
        if column.find('a'):
            row_information.append('X')
        else:
            row_information.append(column.contents[-1])
    return row_information


def get_html_tables(soup):
    return soup.find(class_='qf-facttable').find_all(class_='type')[1:]


def main():
    """
    Scrapes data from the US census bureau and stores it in a
    specified csv file
    """
    city_name = "brownsville"
    state_name = "texas"
    city_information = get_city_information(city_name, state_name)
    soup = BeautifulSoup(city_information.content, 'html.parser')
    html_tables = get_html_tables(soup)
    scrap_html_tables(html_tables)


def clear_csv_file(filename):
    """
    Resets csv file
    """
    if os.path.exists(filename):
        os.remove(filename)


def scrap_html_tables(html_tables):
    clear_csv_file(config.FILE_NAME)
    for table in html_tables:
        for section in table.find_all('tbody'):
            for row in section.find_all('tr')[1:]:
                table_row_data = row.find_all('td')
                row_data = get_row_information(table_row_data)
                write_to_csv(config.FILE_NAME, row_data)


if __name__ == "__main__":
    main()
