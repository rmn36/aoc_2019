import pandas as pd 
import math

def calc_fuel(mass):
    return math.floor(mass/3)-2

def calc_fuel_recur(mass):
    fuel = calc_fuel(mass)
    if fuel <= 0:
        return 0
    else:
        more_fuel = calc_fuel_recur(fuel)
    return fuel + more_fuel

data = pd.read_csv("input.csv") 
data['fuel'] = data['mass'].apply(calc_fuel_recur)
print(data.sum()['fuel'])