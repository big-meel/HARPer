import os, sys
import json
import urllib.request

class TimeEntryReport:

  def __init__(self, start_date, end_date, account_id, access_token, api_url):
    self.start_date = start_date
    self.end_date = end_date
    self.account_id = account_id
    self.access_token = access_token
    self.api_url = api_url

  def entries(self):
    response_body = self.__send_request().read().decode("utf-8")
    json_response = json.loads(response_body)

    return json.dumps(json_response, indent=4)

  def __headers(self):
    return {
      "User-Agent": "My Harvest Report (jameel@onegreatstudio.com)",
      "Authorization": "Bearer " + self.access_token,
      "Harvest-Account-Id": "" + self.account_id
    }
  
  def __generate_query(self):
    return "from=" + self.start_date + "&" + "to=" + self.end_date

  def __send_request(self):
    complete_url = self.api_url + "/time_entries?" + self.__generate_query()

    # Create request
    request_obj = urllib.request.Request(url=complete_url, headers=self.__headers())
    # Initiate request with a timeout of 5 and capture response
    return urllib.request.urlopen(request_obj, timeout=5)




