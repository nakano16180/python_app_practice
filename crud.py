#!/usr/bin/env python3
import sys, os
import datetime
import pprint


data_dir = 'database'

def create_data(data_name, data):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        with open(data_dir +"/"+ data_name +'.csv', "w") as file:
            file.write(data+'\n')


def read_data(data_path):
    if not os.path.exists(data_path):
        print("Can't read data. please check data name.")
    else:
        with open(data_path, "r") as file:
            data = file.readlines()
            return data

def update_data():
    pass

def delete_data():
    pass

create_data("test", "aaa,AAA,日本語,111")
data = read_data("database/test.csv")

pprint.pprint(data)