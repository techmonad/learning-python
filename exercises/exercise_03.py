import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("../data/Filetest.csv", sep="\t")
    print(df.loc[1:10])
    print(df.iloc[1:10])
    print(df.shape)
