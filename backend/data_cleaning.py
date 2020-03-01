import clean
import pandas as pd

iso = pd.read_csv('iso.csv')
corona = pd.read_csv('02-29-2020.csv')
corona = clean.cl(corona, iso)