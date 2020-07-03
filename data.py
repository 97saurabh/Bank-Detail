from myapp.models import bankDetails
import csv
def start():
    i = 0
    with open("test.csv","r",encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(i)
                i = i + 1
                created = bankDetails.objects.get_or_create(
                ifsc = row[0],
                bank_id = row[1],
                branch = row[2],
                address = row[3],
                city = row[4],
                district = row[5],
                state = row[6],
                bank_name = row[7]
                )
