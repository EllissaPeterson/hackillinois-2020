import clean_set
import pandas as pd

corona_set = pd.read_csv('02-29-2020.csv')
iso_set = pd.read_csv('https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv')
clean_set.clean(corona_set, iso_set)