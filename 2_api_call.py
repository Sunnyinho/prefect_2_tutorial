import requests
from prefect import flow, task

# @flow
# def call_api(url):
#     return requests.get(url).json()

# api_result = call_api("http://time.jsontest.com/")
# print(api_result)

@task
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()

@task
def parse_fact(response):
    fact = response["fact"]
    print(fact)
    return fact

@flow
def api_flow(url):
    fact_json = call_api(url)
    return fact_json

print(api_flow("https://catfact.ninja/fact"))

print("==============================================================================================================================")
print("==============================================================================================================================")
print("Flow Within Flow")

@flow
def common_flow(config: dict):
    print("I am a subgraph that shows up in lots of places!")
    intermediate_result = 42
    return intermediate_result

@flow
def mainflow():
    # do something
    # then call another flow function
    data = common_flow(config={})
    # do more things

mainflow()