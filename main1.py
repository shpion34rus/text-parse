import re
import urllib.request # the lib that handles the url stuff


def reader(target_url):
    data = urllib.request.urlopen(target_url)  # it's a file like object and works just like a file
    count = 0
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    for line in data:  # files are iterable
        if count == 0:  # отсекаем 0-вую итерацию т.к. там '\b'
            count += 1
            continue

        response = str(line).split('"')
        ipaddr = re.findall(regexp, response[0])[0]
        try:
            date = response[0][response[0].index('[')+1: response[0].index(']')]
        except ValueError:
            print('didn\'t recognized time string!')

        httpcode = response[2][:4]
        responsebody = response[5]

        count += 1
        if count % 1000 == 0:
            print(count)
    print(count)


if __name__ == '__main__':
    reader('http://www.almhuette-raith.at/apache-log/access.log')