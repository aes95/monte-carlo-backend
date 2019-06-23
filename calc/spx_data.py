import datetime, decimal, csv
from calc.models import Index

with open('calc/data/VBMFX.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None) #skip header
    for row in reader:
        mo = int(row[0])
        year = int(row[1])
        
        Index.objects.create(
            index_name='VBMFX',
            date=datetime.date(year, mo, 1),
            high = decimal.Decimal(row[3]),
            low = decimal.Decimal(row[4]),
            adj_close = decimal.Decimal( row[-2]),
            mo_return = decimal.Decimal(row[-1])
        )
