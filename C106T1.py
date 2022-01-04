import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    sizeofTV=[]
    timespent=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            sizeofTV.append(float(row["size"]))
            timespent.append(float(row["time"]))
    return{"x":sizeofTV,"y":timespent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of Tv and Average time spent watching Tv in a week :-  \n--->",correlation[0,1])
  
def setup():
    data_path="tv.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)


setup()
