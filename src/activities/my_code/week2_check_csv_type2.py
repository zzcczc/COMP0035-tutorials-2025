import csv
from pathlib import Path

if __name__ == '__main__':
 data_file = Path(__file__).parent.parent / 'data' / 'npc_codes.csv'# Your code that locates the file
with open(data_file) as csv_file:## "with" 是指定義一個區塊，當區塊結束時會自動關閉檔案
#类似于csv_file = open(data_file)
#csv_reader = csv.reader(csv_file)
#first_row = next(csv_reader)
#csv_file.close()
 csv_reader = csv.reader(csv_file, delimiter=',')
 first_row = next(csv_reader)
print(first_row)