import urllib.request


def reader(target_url):
    data = urllib.request.urlopen(target_url)
    count = 0
    f = open('C:\\access.log', 'w')
    for line in data:
        count += 1
        f.write(line.decode('utf-8'))
        if count % 1000 == 0:
            print(count)
    print(count)


if __name__ == '__main__':
    reader('http://www.almhuette-raith.at/apache-log/access.log')