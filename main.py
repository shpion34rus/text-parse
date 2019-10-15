import re
from dateutil.parser import parse
from dateutil.tz import gettz

def reader():
    # result = re.findall(r'\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}´ +`\d{4}', '178.35.0.41 - - [12/Dec/2015:18:44:48 +0100]')
    #result = re.findall(r'\[(.*?)\]', '178.35.0.41 - - [12/Dec/2015:18:44:48 +0100]')
    # pattern = r'/(\S+) (\S+) (\S+) \[([^:]+):(\d+:\d+:\d+) ([^\]]+)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) (\".*?\") (\".*?\")/'
    string = '178.35.0.41 - - [12/Dec/2015:18:44:48 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"'
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    result = re.findall(pattern, string)
    print(result[0])
    pattern = r'\[(.*?)\]'
    result = re.findall(pattern, string)
    print(result[0])
    pattern = r'(\S+) (\S+) (\S+) \[([^:]+):(\d+:\d+:\d+) ([^\]]+)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) (\".*?\") (\".*?\")'
    result = re.findall(pattern, string)
    print(result)

    # parse


if __name__ == '__main__':
    reader()
