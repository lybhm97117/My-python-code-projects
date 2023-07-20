"""
File: webcrawler.py
Name: Teresa Tien
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features='html.parser')

        # ----- Write your code below this line ----- #
        tags = soup.find_all('td')
        data_list = []
        for tag in tags:
            text = tag.text.split()     # 很多字的字串 省去空白換行 (變成該行所有字都連在一起）
            if len(text) == 1:
                data_list.append(text[0])
        text_count = 0  # 有 rank, male name, male number, female name, female number
        rank_list = []
        male_numbers = 0
        male = ''
        female_numbers = 0
        female = ''
        for word in data_list:
            text_count += 1
            rank_list.append(word)  # [ rank, male name, male number, name, number]
            if text_count % 5 == 0 and text_count <= 1000:  # 只取[0]= rank且rank <1000 condition
                for ch in rank_list[2]:     # 只取male number
                    if ch.isdigit():
                        male += ch
                male_numbers += int(male)
                male = ''
                for ch in rank_list[4]:     # 只取female number
                    if ch.isdigit():
                        female += ch
                female_numbers += int(female)
                female = ''
                rank_list = []
        print('Male Number: ' + str(male_numbers))
        print('Female Number: ' + str(female_numbers))




if __name__ == '__main__':
    main()
