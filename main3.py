import urllib.request
import re


def reader(target_url):
    data = urllib.request.urlopen(target_url)
    total_length = data.length
    temp_percent = 0
    pattern = r'(\S+) (\S+) (\S+) \[(.*?)\] \"(\S+) (.*?) (\S+)\" (\S+) (\S+) (\".*?\") (\".*?\")'
    count = 0
    temp_length = 0
    f = open('C:\\access.log', 'w')
    for line in data:
        count += 1
        temp_length += len(line.decode('utf-8'))
        current_percent = int((temp_length/total_length)*100)
        if current_percent != temp_percent:
            temp_percent = current_percent
            print(str(current_percent) +'%')
        # f.write(line.decode('utf-8'))
        if count % 10000 == 0:
            print(count)
            result = re.findall(pattern, str(line))
            # print(result)
        f.write(line.decode('utf-8'))
    print(count)


if __name__ == '__main__':
    reader('http://www.almhuette-raith.at/apache-log/access.log')