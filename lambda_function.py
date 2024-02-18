import os
from harper_core import TimeEntryReport

def lambda_handler(event, context):
    
    report = TimeEntryReport(
            start_date = event['start_date'],
            end_date = event['end_date'],
            account_id = os.environ['HARVEST_ACCOUNT_ID'],
            access_token = os.environ["HARVEST_ACCESS_TOKEN"], 
            api_url = os.environ["HARVEST_API_V2_URL"]
        )
    
    return report.entries()
