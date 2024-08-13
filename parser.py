from bs4 import BeautifulSoup
import csv


def html_to_csv(html, key_word, city):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class': 'table__wrapper'})
    headers = ['city', 'key_word'] + [header.get_text().strip() for header in table.find_all('th')] + ['region']
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        row_data = [city, key_word] + [cell.get_text().strip() for cell in cells] + [region]
        rows.append(row_data)
    with open('regions_sep.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(headers)
        writer.writerows(rows)


#key_word = 'лечение коронавируса'
#key_word = 'пульсоксиметр и сатурация'
#key_word = 'пропало обоняние'
key_word = 'пропал запах'

city = 'Наро-Фоминск' 
region = 'Москва и область'
html_file = open('query.txt', 'r')
html_block = (html_file.readline())
html_to_csv(html_block, key_word, city)
