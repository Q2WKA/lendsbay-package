import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def add_month(date: pd.Timestamp):
    if date.month < 12:
        d = str(date.year)+'-'+str(date.month+1)+'-'+str(date.day)+' '+str(date.time())
        return pd.to_datetime(d)
    else:
        d = str(date.year+1)+'-'+str(1)+'-'+str(date.day)+' '+str(date.time())
        return pd.to_datetime(d)

def drop_tz(table: pd.DataFrame):  
    if 'datetime64[ns, UTC]' in table.dtypes.value_counts(0):  
        for i in table.select_dtypes(include=['datetime64[ns, UTC]'], exclude=None).columns:  
            table.loc[:,i] = table.loc[:,i].dt.tz_localize(None)  
          
    return(table)

def normalize_duration(row):
    if row.period == 'once':
        return row.duration / 31
    else:
        return row.duration

print(add_month(pd.to_datetime('today')))
