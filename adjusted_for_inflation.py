# determines inflation adjusted amount for an amount
# reads from local csv file with two fields: year and amount
# 1979,1000
# returns a comma seperated list with year, old value, current value
# change the_year if it is not 2016

import re, urllib, csv

csv_file = "ag.csv"
the_year = 2016


def get_new_value(year,amount,current=the_year):
    link = "https://www.statbureau.org/calculate-inflation-price-jsonp?jsoncallback=&country=united-states&start=" + str(year) + "/1/1&end=" + str(current) + "/1/1&amount=" + str(amount) + "&format=true"
    f = urllib.urlopen(link)
    new = f.read()
    new = re.sub(' ', '',new)
    new = re.sub('\("', '',new)
    new = re.sub('"\)', '',new)
    new = re.sub('\$', '',new)
    new = re.sub(',', '',new)
    
    return new




with open(csv_file, 'r') as csvfile:
    the_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in the_csv:
        year = int(row[0])
        amount = row[1]
        new_amount = get_new_value(year, amount)
        print str(year) + "," + amount + "," + new_amount



    
