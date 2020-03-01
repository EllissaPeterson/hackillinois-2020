def cl(corona, iso):
    corona = corona.drop(index=[10,102])
    corona = corona.replace(to_replace=['Mainland China','Taiwan','Hong Kong','Macau'], value=['China','China','China','China'])
    iso = iso.loc[:,['official_name_en','ISO3166-1-Alpha-3']]
    iso = iso.replace(to_replace=['Russian Federation','Iran (Islamic Republic of)','Republic of Korea','Viet Nam','United States of America','United Kingdom of Great Britain and Northern Ireland'], value=['Russia','Iran','South Korea','Vietnam','US','UK'])
    corona = corona.merge(right=iso, how='left', right_on='official_name_en', left_on='Country/Region')
    corona = corona.drop(columns='official_name_en')
    corona.head()
    return corona