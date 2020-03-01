import clean
import datapackage
import pandas as pd

iso_url = 'https://datahub.io/core/country-codes/datapackage.json'

# to load data package into storage
package = datapackage.Package(iso_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        iso = pd.read_csv(resource.descriptor['path'])
        corona = pd.read_csv('02-29-2020.csv')
        corona = clean.cl(corona, iso)