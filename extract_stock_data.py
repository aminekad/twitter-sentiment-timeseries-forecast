import os
import json
import argparse
from shutil import copyfile

import pandas as pd


def get_args():
    parser = argparse.ArgumentParser(description='Extracts a given stock data from the stocknet-dataset')
    parser.add_argument('--stock', dest='stock', type=str, required=True, help='stock name')
    parser.add_argument('--target', dest='target', type=str, required=True, help='target directory')
    return parser.parse_args()

def merge_json_files(files, target):
    tweets = []
    for file in files:
        with open(file, 'r') as sample:
            for line in sample:
                data = json.loads(line)
                tweets.append(data)
    with open(target, 'w') as outfile:
        json.dump(tweets, outfile)

def main():
    # parse command line arguments
    args = get_args()

    # get path to price and tweet data for the desired stock
    price_csv = os.path.join("stocknet-dataset", "price", "raw", args.stock+".csv")
    tweets_dir = os.path.join("stocknet-dataset", "tweet", "raw", args.stock)

    # make a directory to extract stock data to
    if not os.path.exists(args.target):
        os.makedirs(args.target)

    # copy csv file
    target_destination = os.path.join(args.target, args.stock+".csv")
    copyfile(price_csv, target_destination)

    # merge json files into one big file to be parsed by pandas
    json_files = [os.path.join(tweets_dir, f) for f in os.listdir(tweets_dir)]
    merged_json_file_name = os.path.join(args.target, args.stock+".json")
    merge_json_files(json_files, target=merged_json_file_name)

if __name__ == '__main__':
    main()
