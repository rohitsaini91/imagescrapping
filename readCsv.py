import csv

with open('images.csv') as f:
    reader = csv.reader(f)
    images = list(reader)

for img in images:
    print(img[1])
