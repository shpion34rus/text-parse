import dateutil

def reader(filepath):
    copy = open('C:\\accesscopy.log', 'rw')
    original = open(filepath, 'r')
    for line in original:
        copy.write(line)


if __name__ == '__main__':
    reader('C:\\access.log')
