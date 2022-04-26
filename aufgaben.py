import pandas 

dataframe: pandas.DataFrame = pandas.read_csv('csv_data/flughafenkuerzel.csv', sep=';')
print(dataframe.values.tolist())

dataframe.columns = ['city', 'postal code', 'abrv.']
print(dataframe)

