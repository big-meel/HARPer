# Harvest Auto Report Printer (HARPer)

MVP

- cli tool that connects to Harvest API and generates report
- Commit to db to store state and keep track of previous report date
- Cron job that automatically generates report

Expansion

- Frontend that shows preview of current invoice and option to print
- Web, Mobile frontend
- Message server to allow different interfaces to communicate


## Setting up Harvest API

Requirements: 

- Account ID
- Personal Access Token 

The Harvest V2 API is a REST API that allows you to interact with your 
Harvest account programmatically. You can track time, log expenses, create projects, and more.

Requires OAuth or Personal Access Tokens

Example of a GET request

```
curl https://api.harvestapp.com/v2/tasks?page=2&per_page=10 \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Harvest-Account-Id: $ACCOUNT_ID" \
  -H "User-Agent: MyApp (yourname@example.com)"
```

Harvest also requires that each request include a User-Agent header with both:

The name of your application

A link to your application or email address
We use this information to get in touch if you’re doing something wrong (so we can warn you before you’re blocked) or something awesome (so we can congratulate you). Here are examples of acceptable User-Agent headers:

- User-Agent: Trello (http://trello.com/contact)
- User-Agent: John's Harvest Integration (john@example.com)

If you don’t include a User-Agent header, you’ll get a 400 Bad Request response.

```
  curl -X POST https://api.harvestapp.com/v2/tasks \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Harvest-Account-Id: $ACCOUNT_ID" \
  -H "User-Agent: MyApp (yourname@example.com)" \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"My New Task\"}"
```

## What we care about

Time Reports https://help.getharvest.com/api-v2/reports-api/reports/time-reports/

Time reports show the hours and billable information for each client, project, 
task, or user, where tracked time is present for a given timeframe.

The response contains an object with a results property that contains an array of 
up to per_page results. Each entry in the array is a separate result object. If no 
more results are available, the resulting array will be empty. 
Several additional pagination properties are included in the response to simplify paginating your results.

Note: Each time report request requires both the from and to parameters to be supplied 
in the URL’s query string. The timeframe supplied cannot exceed 1 year (365 days).

GET /v2/reports/time/tasks
