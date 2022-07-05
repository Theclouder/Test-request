import requests

def before_all(context):
    context.r = requests.get('https://api.github.com/events')