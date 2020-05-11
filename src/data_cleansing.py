import pandas as pd

def load_codified_data(trainortest):
    if trainortest=="train":
        data=pd.read_csv(f"./output/data_cleaned.csv",index_col="Unnamed: 0")
    elif trainortest=="test":
        data=pd.read_csv(f"./input/diamonds_test.csv",index_col="Unnamed: 0")
        cut={"Fair":0, "Good":1, "Very Good":2, "Premium":3, "Ideal":4}
        color={"J":0,"I":1,"H":2,"G":3,"F":4,"E":5,"D":6}
        clarity={"I1":0, "SI2":1, "SI1":2, "VS2":3, "VS1":4, "VVS2":5, "VVS1":6, "IF":7}
        data.cut=data.cut.map(cut)
        data.color=data.color.map(color)
        data.clarity=data.clarity.map(clarity)
    return data