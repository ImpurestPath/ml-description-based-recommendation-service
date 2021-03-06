import pandas as pd


def load_all():
    df = pd.read_csv('data/alcohol.csv')
    df['description'] = df['aroma'] + ' ' + df['taste'] + ' ' + df['description']
    return df


def load_by_ids(ids):
    alcohol = pd.read_csv('data/alcohol.csv')
    return alcohol.iloc[ids]
