import requests
import bs4
import schedule
import time
from twilio.rest import Client

def get_info():
    account_sid = "***********f" #For Security Reasons this can not be shown
    auth_token="***********"#For Security Reasons this can not be shown
    res = requests.get('https://covid19.ca.gov/state-dashboard/')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    cases = soup.select('strong')
    client = Client(account_sid, auth_token)
    cases_today = cases[1].getText()
    Vaccines = cases[6].getText()
    client.messages.create(
        from_="+19795965535",
        to="+15109469095",
        body=("California's New Cases  " + cases_today + "\nCurrent Vaccinations: " + Vaccines),
    )

schedule.every().day.at('10:00').do(get_info)

while 1:
    schedule.run_pending()
    time.sleep(1)
