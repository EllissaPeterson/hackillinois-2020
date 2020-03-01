from urllib2 import Request, urlopen
import json
from pandas.io.json import json_normalize

request=Request('https://www.kaggle.com/max-mind/world-cities-database/download/fIa40mQCPcC6ZJIDQR4Y%2Fversions%2FOH1ToFMEYfoKbCjSUppD%2Ffiles%2Fworldcitiespop.csv?datasetVersionNumber=3')
response = urlopen(request)
elevations = response.read()
data = json.loads(elevations)
json_normalize(data['results'])

data_url = 'https://raw.githubusercontent.com/lutangar/cities.json/master/cities.json'

# to load data package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        data = pd.read_csv(resource.descriptor['path'])
        print (data)