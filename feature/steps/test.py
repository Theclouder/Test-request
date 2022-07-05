import json
import requests
from behave import *

@when('I request the JSON')
def get_JSON(context):
    r = requests.get('https://api.github.com/events')
    #r = requests.get('https://httpbin.org')
    '''
    This is for getting a string with all the values and keys from JSON:
    array = r.text
    
    This is for getting a list of dictionaries from JSON:
    array = r,json()

    or

    array = json.loads(r.text)
    '''
    #print(type(json.loads(r.json())))
    x = r.json()
    check = 0
    # X is a list of dict
    for i in x:
        for j in i.keys():
            if j == "id":
                print(i[j])
                check = 1
    print(check)
    if (check == 1):
        assert True
    else:
        assert False

@then('I print the JSON')
def print_JSON(context):
    #print(context.text)
    assert True