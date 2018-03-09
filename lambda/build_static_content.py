import json
# from CNN_Parser.Parser import get_front_page_headlines as gh
from BBC_Parser.Search import create_url
from BBC_Parser.ParseSearchResult import parse_search_result

list = parse_search_result(create_url("elon musk",3))
print(len(list))
j_list = [json.dump(i.__dict__) for i in list]
s = json.dump(j_list)
print(s)

# use json.dump(item.__dict__)

