import csv

def get_position(path, pos_x, pos_y):
    with open (path, 'r', encoding='utf-8') as file:
        data = csv.reader(file)
        print(list(data)[pos_x][pos_y])

if __name__ == '__main__':
    get_position('task1/train.csv', 0, 3)