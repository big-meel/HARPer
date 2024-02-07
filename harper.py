import os, sys
import json
import urllib.request
import argparse
from dotenv import load_dotenv
load_dotenv()

ACCOUNT_ID = os.getenv('HARVEST_ACCOUNT_ID')
ACCESS_TOKEN = os.getenv('HARVEST_ACCESS_TOKEN')
API_URL = os.getenv('HARVEST_API_V2_URL')

# Initialize parser
parser = argparse.ArgumentParser(
  prog='HARPer',
  description='Fetches time entries from harvest API'
)

parser.add_argument('-s', '--start_date', help='The stating date of the time entries requested `yyyymmdd`')
parser.add_argument('-e', '--end_date', help='The ending date of the time entries requested `yyyymmdd`')

args = parser.parse_args()

if not args.start_date:
  sys.stderr.write("A starting date is required for this command `--start_date \<yyyy-mm-dd\>`\n")
  sys.exit()

if not args.end_date:
  sys.stderr.write("An End date is required for this command `--end_date \<yyyy-mm-dd\>`\n")
  sys.exit()

queries = "from=" + args.start_date + "&" + "to=" + args.end_date

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

print(json.dumps(json_response, indent=4))
# print(type(json_response))

# TODO: Split core functionality from CLI components (Core to be used in A Lambda function) with OOP?
# TODO: Add to Lambda function


# Create separate service that takes the JSON and creates PDF
# TODO: Look into generating pdf with python files (html python templates)
# TODO: Generate PDF and store in tmp directory