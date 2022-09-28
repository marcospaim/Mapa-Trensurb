import csv
import os
def get_estacoes():
    path = os.path.dirname(__file__)
    #directory = os.path.abspath(os.path.join(os.path.abspath(os.path.join(path, os.pardir)), os.pardir))
    directory = path
    directory = directory+'/estacoes.csv'
    with open(directory, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data = {i: data[i][:] for i in range(len(data))}
        #print(data)
    return data

def get_path():
    path = os.path.dirname(__file__)
    #directory = os.path.abspath(os.path.join(os.path.abspath(os.path.join(path, os.pardir)), os.pardir))
    directory = path
    directory = directory+'/TUE 102.csv'
    with open(directory, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data = {i: data[i][1:3] for i in range(1, len(data), 1)}
        #print(data)
    return data


if __name__ == "__main__":
    get_path()