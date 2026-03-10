import pandas as pd

def clean_data(df):

    df = df.fillna("Unknown")

    df.columns = df.columns.str.strip()

    return df