#!/usr/bin/env python3.7


import argparse
import json
import glob


data_path = "data.json"
filter_path = "filter.json"
output_excel_path = "output/output.xlsx"
output_csv_path = "output/output.csv"
log_path = "log/xldr.log"


def args_parser():
    parser = argparse.ArgumentParser(description="Program Description:")
    parser.add_argument("-d", "--data", help="-d data_path (default=" + data_path + ")")
    parser.add_argument("-f", "--filter", help="-f filter path (default=" + filter_path + ")")
#    parser.add_argument("-o", "--output", help="-o output_path (default=" + output_path + ")")
    parser.add_argument("-l", "--log", help="-l log_path (default=" + log_path + ")")
    args = parser.parse_args()


# retrieve path of every needed file for the analysis
def get_data_path(data_path):
    # open data json file
    with open(data_path, 'r') as json_file:
        parsed_json = json.load(json_file)

    # retrieve every needed path
    file_list = []
    for path in parsed_json["data"]["path"]:
        if path not in file_list:
            file_list += glob.glob(path)

    return file_list


# load every files into a pandas dataframe
def excel_load(path_list):
    all_data = pd.DataFrame()
    for p in path_list:
        # read_csv(csv_file)
        df = pd.read_excel(p)
        all_data = all_data.append(df, ignore_index=True)
    return all_data


import pandas as pd


# apply filters descrived in filter_path
def excel_filter(df):

    with open(filter_path, 'r') as json_file:
        parsed_json = json.load(json_file)

    print(parsed_json["filter"])

    for k, v in parsed_json["filter"].items():
        if type(v) == int:
            df = df[df[k] == v]
        if type(v) == str:
            df = df[df[k].str.contains(v)]
            #df[df.Age.str.contains('ville',case=False)]
            #df.filter(like='bbi', axis=0)

    print (df)
    return df


def excel_save_file(filtered_data):
    print("output saved in " + output_excel_path)
    print("output saved in " + output_csv_path)
    df = pd.DataFrame(filtered_data).T  # transpose to look just like the sheet above
    df.to_csv(output_csv_path)
    df.to_excel(output_excel_path)


def main():
    print("_main")
    args_parser()

    # retrieve path to analyse
    path_list = get_data_path(data_path)

    # 1) load files
    all_data = excel_load(path_list)

    # apply filters
    filtered_data = excel_filter(all_data)

    # save result in output file
    excel_save_file(filtered_data)


if __name__ == "__main__":
    main()

