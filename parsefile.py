import datetime
import re
import time
import sqlalchemy
from sqlalchemy import create_engine, VARCHAR
from sqlalchemy import MetaData, Table, Column, Integer
import psycopg2
import urllib.request


engine = create_engine('postgresql://postgres:qwerty@localhost:5432/parsertest')

'''
meta = MetaData()
users_table = Table('uparser', meta,
    Column('id', Integer, primary_key=True),
    Column('ip', VARCHAR(20))
    Column('dtimefield', )
    Column('httpmethod', String(50))
    Column('httppath', String(50))
    Column('name', String(50))
    Column('name', String(50))
    Column('name', String(50))
    Column('name', String(50))
    Column('name', String(50))
)
'''

def reader(target_url):
    # pattern = r'(\S+) (\S+) (\S+) \[([^:]+):(\d+:\d+:\d+) ([^\]]+)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) (\".*?\") (\".*?\")'
    pattern = r'(\S+) (\S+) (\S+) \[(.*?)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) (\".*?\") (\".*?\")'
    data = urllib.request.urlopen(target_url)
    file = open('C:\\access.log')
    for string in file:
        if string.__len__() < 5:
            continue
        result = re.findall(pattern, string)
        res = result[0]
        # dt = time.strptime(result[0][3])
        datetime.datetime.strptime(res[3], '%d/%b/%Y:%H:%M:%S %z')
        print(result)


if __name__ == '__main__':
    reader('http://www.almhuette-raith.at/apache-log/access.log')
