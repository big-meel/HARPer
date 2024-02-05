import os
import json
import urllib.request
from dotenv import load_dotenv
load_dotenv()

# Move these to env variables and access with os.environ.get(HARVEST_ACCOUNT_ID)
ACCOUNT_ID = os.getenv('HARVEST_ACCOUNT_ID')
ACCESS_TOKEN = os.getenv('HARVEST_ACCESS_TOKEN')
API_URL = os.getenv('HARVEST_API_V2_URL')

# Update these dates to be dynamic
from_date = "20231220"
to_date = "20240123"
queries = "from=" + from_date + "&" + "to=" + to_date

# Fetches time entries
url = API_URL + "/time_entries?" + queries 

headers = {
  "User-Agent": "My Harvest Report (jameel@onegreatstudio.com)",
  "Authorization": "Bearer " + ACCESS_TOKEN,
  "Harvest-Account-Id": "" + ACCOUNT_ID
}

# Create request
request = urllib.request.Request(url=url, headers=headers)

# Initiate request with a timeout of 5 and capture response
response = urllib.request.urlopen(request, timeout=5)

# Read the response and convert to json
response_body = response.read().decode("utf-8")
json_response = json.loads(response_body)

print(json.dumps(json_response, sort_keys=True, indent=4))

# DONE: Move constants to env variables 
# TODO: Set up git and github repo to better keep track of features
# TODO: Capture json response and clean up unneccessary data (Oppoetunity for pandas perhaps)
# TODO: Make into proper cli tool
# TODO: Look into generating pdf with python files (html python templates)
# TODO: Generate PDF and store in tmp directory
# TODO: Keep track of dates
# TODO: Cron job