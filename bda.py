#!/usr/bin/env python3.7


import argparse
import json
import glob
import pandas


data_path = "data.json"
filter_path = "filter.json"
output_excel_path = "output/output.xlsx"
output_csv_path = "output/output.csv"


def args_parser():
    parser = argparse.ArgumentParser(description="Program Description:")
    parser.add_argument("-d", "--data", help="-d data_path (default=" + data_path + ")")
    parser.add_argument("-f", "--filter", help="-f filter path (default=" + filter_path + ")")
    parser.add_argument("-o", "--output", help="-o output_path (default=" + output_excel_path + ")")
    args = parser.parse_args()


# returns the list of files defined in the data.json
def __get_data_path():

    # open data json file
    with open(data_path, 'r') as json_file:
        parsed_json = json.load(json_file)

    # retrieve every needed path
    file_list = []
    for path in parsed_json["data"]["path"]:
        if path not in file_list:
            file_list += glob.glob(path)

    return file_list


# 1) load files defined in data.json into a pandas dataframe
def get_data_input():

    # retrieve list of path to analyse
    path_list = __get_data_path()

    all_data = pandas.DataFrame()
    for p in path_list:
        # read_csv(csv_file)
        df = pandas.read_excel(p)
        all_data = all_data.append(df, ignore_index=True)
    return all_data


# 2) apply filters defined in filter.json
def apply_filter(data):

    # open filter json file
    with open(filter_path, 'r') as json_file:
        parsed_json = json.load(json_file)

    # loop over every filters and apply them on the data
    for k, v in parsed_json["filter"].items():
        if type(v) == int:
            # TODO: be able to manage intervals
            data = data[data[k] == v]
        if type(v) == str:
            data = data[data[k].str.contains(v)]
            # TODO: be able to manage regex and other types of filters
            #data[data.Age.str.contains('ville',case=False)]
            #data.filter(like='bbi', axis=0)

    return data


# 3) save filtered data in output file
def save_data(filtered_data):
    print (filtered_data)
    # transpose to look just like the sheet above
    df = pandas.DataFrame(filtered_data).T
    df.to_csv(output_csv_path)
    df.to_excel(output_excel_path)


def main():
    args_parser()
    # 1) retrieve data defined in data.json
    data = get_data_input()
    # 2) apply filters defined in filter.json
    filtered_data = apply_filter(data)
    # 3) save results in output file
    save_data(filtered_data)


if __name__ == "__main__":
    main()

