"""
File: babynames.py
Name: 
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    if name not in name_data:
        name_data[name] = {
            year: rank}  # 名字不存在，則創建一個新的字典，key是年份 year，value是排名 rank，並將這個字典加入到 name_data 字典中，以名字 name 作為key
    elif year not in name_data[name]:
        name_data[name][year] = rank
    elif name in name_data and year in name_data[name]:
        if int(rank) < int(name_data[name][year]):  # 留下排名前面的
            name_data[name][year] = rank  # 留下排名前面的


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    with open(filename, 'r') as f:
        for line in f:
            tokenization = line.split(',') # 把每一行用，做斷詞斷句
            if len(tokenization) == 1:
                year = tokenization[0].strip() # 把空白＆換行都切掉
            else:
                rank = tokenization[0].strip()
                name1 = tokenization[1].strip()
                name2 = tokenization[2].strip()
                add_data_for_name(name_data, year, rank, name1) # 用add_data_for_name的邏輯方式處理filename中的資料
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames): # 多個filename檔案都需要一次讀取
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {} # 做一個空的dictionary 之後要return,把所有filename處理過的資料都裝進裡面
    for filename in filenames: # filename=檔名, filenames =python list
        add_file(name_data, filename) # 每一個filename檔案都做add＿file這個動作
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    names = []  # 空的list,他會把之後有match到的名字都裝進去
    for name in name_data:
        if target.lower() in name.lower():
            names.append(name)
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
