import time

import requests

BASE = "https://dummyjson.com/quotes"
END_POINT = "random"


def call_api(base, endpoint):
  resp = requests.get(f"{base}/{endpoint}")
  if resp.status_code != 200:
    raise requests.HTTPError(f"HTTP error occurred: {resp.status_code} - {resp.reason}")
  else:
    return resp.json()


def get_random_quote():
  resp_json = call_api(BASE, END_POINT)
  return resp_json["quote"]


while True:
  st = time.time()
  quote = get_random_quote()
  print(f"Quote: {quote}")
  et = time.time()
  time_taken = et - st
  print(f"Got quote in {time_taken:.4f} seconds")
