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

# Only require the following data points grouped by their spent date
# spent_date (entry['spent_date'])
# client_name (entry['client']['name])
# project_name (entry['project']['name])
# task_name (entry['task']['name'])
# employee_name (entry['user']['name'])
# hours (entry['hours'])
# notes (entry['notes'])
#
# total_hours Will need to inject an algo to calculate the total hours
# Timeframe given dynamically

# print(json.dumps(json_response, indent=4))
print(type(json_response))

# DONE: Move constants to env variables 
# DONE: Set up git and github repo to better keep track of features
# DONE: Capture json response and clean up unneccessary data (Oppoetunity for pandas perhaps)
# TODO: Make into proper cli tool
# TODO: Cron job
# TODO: Add to Lambda function


# Create separate service that takes the JSON and creates PDF
# TODO: Look into generating pdf with python files (html python templates)
# TODO: Generate PDF and store in tmp directory