from bs4 import BeautifulSoup
import requests
import os


def write_to_csv(filename, string_datas):
    """
    Writes to a specified csv file
    """
    with open(filename, 'a') as fopen:
        fopen.write((' | ').join(string_datas) + '\n')


def is_cityname_in_title(page_selectors, city_name):
    h2_content = str(page_selectors.find(class_='qf-titlebar').h2.contents[0])
    return h2_content.lower().split(" ")[0] == city_name


def get_city_information(city_name, state_name):
    """
    Get a HTTP Response for a particular city and state
    """
    location = city_name+"city"+state_name+",US"
    base_url = 'https://www.census.gov/quickfacts/fact/table/'
    city_link = base_url + location + '/PST045217'
    city_information = requests.get(city_link)
    page_selectors = BeautifulSoup(city_information.text, 'html.parser')
    if is_cityname_in_title(page_selectors, city_name):
        return city_information
    return None


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
            if(column.find('a')):
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
    if not city_information:
        print("City information does not exist")
        return -1
    soup = BeautifulSoup(city_information.text, 'html.parser')
    html_tables = get_html_tables(soup)
    for table in html_tables:
        for section in table.find_all('tbody'):
            for row in section.find_all('tr')[1:]:
                string_columns = get_row_information(row.find_all('td'))
                write_to_csv(filename, string_columns)


if __name__ == "__main__":
    main()
