import numpy as np
import pandas as pd

# cleaning up data
# removing unwanted columns and adding the sum of the incidents happened in all the regions in a particular day
temp = pd.read_csv('./data/time_series_19-covid-Confirmed.csv')
confirmed_total = pd.DataFrame(temp.iloc[:, 5:].sum(), columns=["confirmed"])

temp = pd.read_csv('./data/time_series_19-covid-Deaths.csv')
death_total = pd.DataFrame(temp.iloc[:, 5:].sum(), columns=["deaths"])

temp = pd.read_csv('./data/time_series_19-covid-Recovered.csv')
recovered_total = pd.DataFrame(temp.iloc[:, 5:].sum(), columns=["recovered"])

# joining the result of the 3 parameters according to date
result = pd.concat([confirmed_total, death_total, recovered_total],
                   join='inner', axis=1)

# saving the result into json and csv
result.to_json('./output/data.json')
result.to_csv('./output/data.csv')
