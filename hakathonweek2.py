import psycopg2
from bs4 import *
import requests
import random as rd
url = 'http://kinoteatr.kg/index.php/category/view?id=17'


name_film = []
genre = []
genres = []
year = []

req = requests.get(url)
scr = req.text
# print (scr)
soup = BeautifulSoup(scr, "html.parser")
all_product_h = soup.find_all(class_ ="card-title text-danger")
for i in all_product_h:
    name_film.append(i.text)   
print(name_film)            


all_product_a = soup.find_all(class_ ="card-text")
for j in all_product_a:
    genre.append(j.text)
# print(genre)


for item in range(len(genre)):
    if item %  2 == 0:
        genres.append(genre[item][6:])
# print (genres)
 
for item in range(len(genre)):
    if item %  2 != 0:
        year.append(genre[item][5:])
# print (year)

database = 'Films'
user = 'postgres'
password = 'kh01052006'
host = '127.0.0.1'
port = '5432'

connection = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
)
print ('''
                                                ПОДКЛЮЧЕНИЯ ПРОШЛО УСПЕШНО!!!
 
                                                ВЫ ЯВЛЯЙТЕСЬ PostgreSQL ПОЛЬЗОВАТЕЛЕМ
''')
cursor = connection.cursor()
 
query = '''insert into list_of_films (name_films,type_genre,year) values '''
for i in range (len(name_film)):
    query += f'''(
        '{name_film[i]}',
        '{genres[i]}',
        '{year[i]}'

    ),'''
print ('INSERT 01')
sql_query = query[:-1]+';'
cursor.execute(sql_query)
connection.commit()
cursor.close()
connection.close()