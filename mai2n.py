import re
from collections import Counter
import csv


def reader(filepath):
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    # f = open(filepath)
    with open(filepath) as f:
        log = f.read()
        ips_list = re.findall(regexp, log)
    # print(ips_list)
    return ips_list


def count(ips_list):
    return Counter(ips_list)


def write_csv(count):
    with open('C:\\output.csv', 'w') as csvfile:
        header = ['IP', 'Frequency']
        writer = csv.writer(csvfile, dialect='excel', delimiter=',')
        # writer.writerow(header)

        for item in count:
            writer.writerow((item, count[item]))


if __name__ == '__main__':
    # reader('C:\\access.log')
    write_csv(count(reader('C:\\access.log')))