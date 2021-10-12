#import
import time, email, smtplib, ssl, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from datetime import date
from os.path import basename

#variables
baseLink = "https://pap.lausd.net/en-US/"
checkDebounce = 1
screenshotWait = 0.5

#class
class Easypass():
    def __init__(self, senderEmail: str, senderPassword:str):
        self.senderEmail = senderEmail
        self.senderPassword = senderPassword
    def GetPass(self, Email: str, Password: str, Reciver: str, DriverPath: str, Debounce: int):
        #Set Time / Get Date
        startTime = time.time()
        Today = str(date.today())

        #Create Driver
        driverOptions = Options()
        driverOptions.add_argument("--headless")
        driverOptions.add_argument('--no-sandbox')  
        Driver = webdriver.Chrome( options=driverOptions)
        Driver.set_window_size(500, 1080)
        Log("Created driver", Email)

        #Get Website
        Driver.get(baseLink)

        #Sign in with Microsoft / Student Login
        studentSigninBtn = GetElement("Id", "button", "https://login.windows.net/042a40a1-b128-4ac4-8648-016ffa121487/", Driver, Email)
        studentSigninBtn.click()
        Log("Created Microsoft login session", Email)

        #Input Email
        time.sleep(checkDebounce)
        emailInput = GetElement("Id", "input", "i0116", Driver, Email)
        emailInput.send_keys(Email)
        Log("Inputted email", Email)
        
        #Procced to Password
        passwordNextBTn = GetElement("Id", "input", "idSIButton9", Driver, Email)
        passwordNextBTn.click()
        Log("Proceeding to password", Email)

        #Input Password
        time.sleep(checkDebounce)
        passwordInput = GetElement("Id", "input", "i0118", Driver, Email)
        print(Password)
        passwordInput.send_keys(Password)
        Log("Inputted password", Email)

        #Sign In
        time.sleep(checkDebounce)
        signinButton = GetElement("Id", "input", "idSIButton9", Driver, Email)
        signinButton.click()

        #Redirect
        Driver.get(baseLink + "select-person/")

        #Close Notification
        CloseNotification(Driver, Email)

        #Select User Card
        userCard = GetElement("Class", "button", "selection-card", Driver, Email)
        userCard.click()

        #Close Notification
        CloseNotification(Driver, Email)

        #Procced to form
        schoolNextBtn = GetElement("Id", "div", "RTS_FACILITY", Driver, Email)
        schoolNextBtn.click()

        #Complete form
        covidQuestion1 = GetElement("Id", "input", "anycovid19symptoms_0", Driver, Email)
        covidQuestion1.click()

        covidQuestion2 = GetElement("Id", "input", "contactwithCOVID19case_0", Driver, Email)
        covidQuestion2.click()
        Log("Completed form", Email)

        #Submit form
        formSubmit = GetElement("Id", "button", "btnProceed", Driver, Email)
        formSubmit.click()
        Log("Submitted form", Email)

        #Close Notification
        CloseNotification(Driver, Email)

        #Get Screenshot
        time.sleep(screenshotWait)
        screenshotPath = Today + Email + ".png"
        Driver.save_screenshot(screenshotPath)
        Log("Saved screenshot", Email)

        #Send Screenshot
        SendScreenshot(self.senderEmail, self.senderPassword, Reciver, screenshotPath, Email)

        #Close Driver
        Driver.close()

        #Remove Screenshot
        os.remove(screenshotPath)
        Log("Deleted Screenshot", Email)

        #Log Time
        Log("--- %s seconds ---" % (time.time() - startTime), Email)

def CheckElement(Methord: str, Type: str, Element: str, Driver, Email: str):
    if(Methord == "Class"):
        Find = Driver.find_elements_by_css_selector(Type + "[class='" + Element + "']")
        ListLen = len(Find)
        if(ListLen > 0):
            Log("Elements Exist", Email)
            return True
        else:
            Log("Does not exist", Email)
            return False
    elif(Methord == "Id"):
        Find = Driver.find_elements_by_css_selector(Type + "[id='" + Element + "']")
        ListLen = len(Find)
        if(ListLen > 0):
            Log("Elements Exist", Email)
            return True
        else:
            Log("Does not exist", Email)
            return False            
            
def GetElement(Methord: str, Type: str, Element: str, Driver, Email: str):
    if(Methord == "Class"):
        while CheckElement(Type, Methord, Element, Driver, Email) == False:
            time.sleep(checkDebounce)
        return Driver.find_element_by_class_name(Element)
    elif(Methord == "Id"):
        while CheckElement(Type, Methord, Element, Driver, Email) == False:
            time.sleep(checkDebounce)
        return Driver.find_element_by_id(Element)

def CloseNotification(Driver, Email: str):
    time.sleep(checkDebounce)
    NotificationCloseBtn = GetElement("Class", "button", "close", Driver, Email)
    NotificationCloseBtn.click()
    Log("Closed notification", Email)

def SendScreenshot(senderEmail:str, senderPassword:str, Reciver: str, filePath: str, Email: str):
    Log("Attempting to send Screenshot", Email)

    emailMessage = MIMEMultipart()
    emailMessage["Subject"] = "DAILY PASS"
    emailMessage["From"] = senderEmail
    emailMessage["To"] = Reciver
    emailMessage.attach(MIMEText("Dailypass of " + str(date.today()), "plain"))
    Log("Completed formating Message", Email)

    with open(filePath, "rb") as attachment:
        Part = MIMEBase("image", "png")
        Part.set_payload(attachment.read())

        encoders.encode_base64(Part)
        Part.add_header(
            "Content-Disposition",
            f"attachment; filename={basename(filePath)}",
        )

        emailMessage.attach(Part)

    Text = emailMessage.as_string()
    Log("Attached Screenshot", Email)

    with smtplib.SMTP_SSL(
        "smtp.gmail.com", 465, context=ssl.create_default_context()
    ) as email:
        email.login(senderEmail, senderPassword)
        email.sendmail(senderEmail, Reciver, Text)
        Log("Succesfully Sent Screenshot to" + Reciver, Email)

def Log(Message: str, Email: str):
    return print(Message + " | " + Email)
