import csv
import pandas as pd
from pandas import read_csv

countries_file = 'E:\\Python\\Laba4\\needed Files\\countries.csv'


def write_to_excel(table):
    names = pd.Series([d.split(',')[0] for d in table.name])
    names.name = 'name'
    lat, lng = zip(*[d.split(',')
                     if isinstance(d, str)
                     else ['nan', 'nan']
                     for d in table.latlng])
    lat, lng = map(pd.Series, (lat, lng))
    lat.name = 'latitude'
    lng.name = 'longitude'
    for_export = pd.concat([names, table[['capital', 'ccn3', 'area', 'currencies']], lat, lng], axis=1)
    with pd.ExcelWriter('exported.xls') as excel_writer:
        for_export.to_excel(excel_writer)


def collision(text):
    print('=' * 100)
    print('=' * 25, text, '=' * 53)
    print('=' * 100)


table = read_csv(countries_file, ',')

collision('largest by AREA')
print(table.nlargest(n=10, columns='area')[['area', 'name']])
collision('smallest by AREA')
print(table.nsmallest(10, ['area'])[['area', 'name']])

collision('largest by PEOPLE COUNT')
print(table.nlargest(10, ['ccn3'])[['ccn3', 'name']])
collision('smallest by PEOPLE COUNT')
print(table.nsmallest(10, ['ccn3'])[['ccn3', 'name']])

collision('FRENCH countries')
print(table[table.languages == 'French'][['languages', 'area', 'name']])

collision('Islands')
print(table[table.borders.isnull()][['name']])
write_to_excel(table=table)

collision('Southern Hemisphere')
print(table.where(pd.Series([float(str(d).split(',')[0]) < 0 for d in table.latlng])).name.dropna())

for i, group in table.groupby(table.area):
    print(str(i) + ': ')
    for j, name in enumerate(group.name, 1):
        print(str(j) + '.', name.split(',')[0])