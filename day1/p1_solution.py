import pandas as pd 
import math

def calc_fuel(mass):
    return math.floor(mass/3)-2

data = pd.read_csv("input.csv") 
data['fuel'] = data['mass'].apply(calc_fuel)
print(data.sum()['fuel'])