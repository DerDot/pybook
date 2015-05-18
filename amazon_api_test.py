from amazon.api import AmazonAPI
import json
from datetime import date

with open('amazon.config') as configfile:
    config = json.load(configfile)

amazon = AmazonAPI(config['AWS_ACCESS_KEY_ID'],
                   config['AWS_SECRET_ACCESS_KEY'],
                   config['AWS_ASSOCIATE_TAG'],
                   region='US')

results = amazon.search(Author='Terry Pratchett',
                        Sort='-publication_date',
                        SearchIndex='Books')

for item in results:
    if item.publication_date >= date.today():
        if item.edition != "Reprint" and item.binding == "Hardcover":
            print(item.title)
            print(item.publication_date)
            print(item.offer_url)
    else:
        break