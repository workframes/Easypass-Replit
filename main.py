#import
from Easypass import Easypass
import schedule , time, keep_alive
keep_alive.keep_alive()

#variables
Easypass = Easypass("BOT_EMAIL", "BOT_PASSWORD")
driverPath = ""

#functions
def DailyFunc():
  Easypass.GetPass("LAUSD_EMAIL", "LAUSD_PASSWORD", "MMS_PHONE_NUMBER", driverPath, 1)


schedule.every().monday.at("13:40").do(DailyFunc)
schedule.every().tuesday.at("13:40").do(DailyFunc)
schedule.every().wednesday.at("13:40").do(DailyFunc)
schedule.every().thursday.at("13:40").do(DailyFunc)
schedule.every().friday.at("13:40").do(DailyFunc)

while True:
  schedule.run_pending()
  time.sleep(1)
