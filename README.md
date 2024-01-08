# COVID-19 California State Dashboard Notifier
This Python script fetches COVID-19 statistics from the California state dashboard and sends updates via SMS using Twilio at 10:00 AM daily.

# Prerequisites
Python 3.x

Required Python libraries: requests, bs4 (BeautifulSoup), schedule, twilio

# Setup
Install the required libraries using pip:
pip install requests bs4 schedule twilio
Obtain a Twilio account SID, auth token, and phone numbers (sender and recipient).

Replace the placeholders in the script with your Twilio credentials and phone numbers.

# Usage
Run the script.
python covid_notifier.py

The script will fetch COVID-19 statistics from the California state dashboard and send the latest data via SMS at 10:00 AM daily.

# Important Note
Ensure the script runs continuously or schedule it to run at the desired time daily using tools like cron or task schedulers based on your operating system.
