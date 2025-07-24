def date_format(date):
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]
    return f'{year}-{month}-{day}'