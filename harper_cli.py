import os, sys
import argparse
from harper_core import TimeEntryReport
from dotenv import load_dotenv
load_dotenv()

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

report = TimeEntryReport(
    start_date = args.start_date, 
    end_date = args.end_date, 
    account_id = os.environ["HARVEST_ACCOUNT_ID"], 
    access_token = os.environ["HARVEST_ACCESS_TOKEN"], 
    api_url = os.environ["HARVEST_API_V2_URL"]
  )

print(report.entries())

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


# TODO: Split core functionality from CLI components (Core to be used in A Lambda function) with OOP?
#       Move core functionality along with necessary dependencies to its own module
# TODO: Add to Lambda function


# Create separate service that takes the JSON and creates PDF
# TODO: Look into generating pdf with python files (html python templates)
# TODO: Generate PDF and store in tmp directory