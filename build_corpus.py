# import required modules
import wikipedia
import pandas as pd
import requests_cache
import traceback
import os
import glob

from bs4 import BeautifulSoup
import requests

df = pd.DataFrame(columns=['Text'])

# got to data dir
# for each csv file, open using pandas and loop title column
# Replace _ with space
# Create new df file for each csv file with all pages
# export in each case
path = 'C://Users//abhis//Desktop//Reimplement-NLP4SE-1//data'
os.chdir(path)
requests_cache.install_cache('data')
for file in list(glob.glob('*.csv')):
    try:
        dataframe = pd.read_csv(file)
    # dataframe = pd.read_csv(
    #     'C://Users//abhis//Desktop//Reimplement-NLP4SE-1//data/ae.csv')
        for id in dataframe['pageid']:
            data = requests.get(
                'https://en.wikipedia.org/w/api.php?action=query&prop=info&pageids='+str(id)+'&inprop=url&format=json')
            data = data.json()
            page = data['query']['pages'][str(id)]['title']
            text = wikipedia.page(page).content
            df = df.append({'Text': text}, ignore_index=True)
    except Exception as e:
        traceback.print_exc()

    finally:
        print(file+' processing done.')
        print(df.shape)
        df.to_csv(file+'_1.csv')
# print(data)
# dataframe['title'] = dataframe['title'].map(lambda x: x.replace("_", " "))
# print(dataframe['title'])


# print(df['Text'])
