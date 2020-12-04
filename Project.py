
import requests
import pandas as pd
from bs4 import BeautifulSoup
import mysql.connector as mysql
import smtplib
import json
import schedule
import time

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders

from numpy import insert
from pandas import DataFrame


# list the user-agent of personal browser in oder to conduct automation
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}

# use web scraper to get current weather info
def getWeather():
    self_url = "https://www.wetter.com/deutschland/duesseldorf/DE0001855.html#"
    page = requests.get(self_url,headers = headers)
    soup = BeautifulSoup(page.content,"html.parser")

    # after analysing page source to figure out that current weather info is within the class of "forecast-navigation-grid"
    table = soup.find_all("div",class_="forecast-navigation-grid")
    for item in table:
        maxtem = item.find(class_='forecast-navigation-temperature-max').text # get maximal temperature
        mintem = item.find(class_='forecast-navigation-temperature-min').text # get minimal temperature
        rainy = item.find(class_='forecast-navigation-precipitation-probability').text # get rainy rate
        return maxtem,mintem,rainy

# accquire bundesliga score table and transfer into csv file
def getTable():
    url = "https://www.kicker.de/2-bundesliga/tabelle"
    response = requests.get(url)
    tabelle = pd.read_html(response.content, header=0)[0]
    select * from tabeblle
    where Verein = "Düsseldorf (A)  Fortuna Düsseldorf (A)"
    fortuna.to_csv("fortuna.csv")

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
def getDB():
    print("read data...")
    with open("Database.json")as r_file:
        DBMelissaZY = json.load(r_file)
    db = mysql.connect(DBMelissaZY)
    cursor = conn.cursor() ## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
    sql = """
    create table if not exists fortuna_score(
        Verein varchar(255),
        Pl. varchar(255),
        Tore Varchar(255),
        Punkte Varchar(255)
    """
    cursor.execute(sql)

    for score in scores:
        val = SELECT ("Verein","Pl.","Tore","Punkte") FROM "fortuna.csv" INTO "fortuna_score" IN "MelissaZY"
        sql = "insert into fortuna_score(Verein,Pl.,Tore,Punkte) values((%s, %s, %s, %s)"
        Verein = score[0]
        Pl.= score[1]
        Tore= score[2]
        Punkte= score[3]
        cursor.execute(sql,val)

    conn.commit()
    conn.close()



# Set the parameters required by smtplib
def sendEmail():
    print ("read data...")
    with open ("Email.json")as read_file:
        sender = json.load(read_file)

    receiver_adress = "melle.yue.zhao@gmail.com"
    subject = "Fortuna-News and weather. Today the rainfall is" +rainy, " the temperatur is from" +maxitem-mintem

    # Construct object of MIMEMultipart
    message = MIMEMultipart()
    message["subject"] = subject
    message["from"] = sender_adress
    message["to"] = receiver_adress

    # Add email contents
    mail_content = MIMEText(
        """Hi,How are you?
        Please find the attached file and link about Fortuna Düsseldorf score and News!
        https://www.kicker.de/fortuna-duesseldorf/info
        I wish you have a nice week!
    
        Best Regards""",
        "plain"
    )

    # Add HTML function
    html = MIMEText(
         """
        <html>
            <body>
                <h1>
                    Week Plan
                </h1>
                <h2>
                    Studying
                </h2>
                <h3>
                    Studying
                </h3>
                <p>
                    Studying
                </p>
            </body>
        </html>
        """,
        "html"
    )

    message.attach(mail_content)
    message.attach(html)
    # Add email attachment
    csvfile = "fortuna.csv"
    with open(csvfile) as file:
        Attachment = MIMEBase("application", "octet-steam")
        Attachment.set_payload(file.read())

    encoders.encode_base64(Attachment)
    Attachment.add_header(
        "Content-Disposition",
        f"attachment; csvfile = {csvfile}",
    )

    message.attach(Attachment)

    # Add pictures to email
    imagefile = open('Fortuna.png', 'rb')
    image = MIMEImage(imagefile.read(), _subtype="png")
    image.add_header('Content-ID', '<image1>')
    image["Content-Disposition"] = 'attachment; filename="Fortuna.png"'
    message.attach(image)

    # Send email message
    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()  # enale security
    session.login(sender["adress"], sender["password"])
    text = message.as_string()
    session.sendmail(sender["adress"], receiver_adress, text)
    session.quit()
    print('Mail Sent')

# scheduling every monday automatically to send the mail
def job():
    print("start")
    weatherandfortuna = weatherandnews_spider()
    send_email(weatherandfortuna)
    print("end")

schedule.every().monday.at("07:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
