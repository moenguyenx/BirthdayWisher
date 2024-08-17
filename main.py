import datetime as dt
import json
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

MY_EMAIL = "your_email@gmail.com"
PASSWORD = "your_smtp_password"

with open("birthday.json", encoding='utf-8') as f:
    data = json.load(f)

# Get today's date
now = dt.datetime.now()
today = f"{now.day}-{now.month}"

# Select a random letter template
letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
happy_fr = None

# Find the friend with a birthday today
for i in data:
    if today == i["birthday"]:
        happy_fr = i
        break


if happy_fr:
    with open(letter_path, encoding='utf-8') as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", happy_fr["name"])

    # Create an email message
    msg = MIMEMultipart()
    msg["Subject"] = "Happy Birthday!!!"
    msg["From"] = MY_EMAIL
    msg["To"] = happy_fr["email"]

    # Attach the letter content
    msg.attach(MIMEText(contents, 'plain'))

    # Attach a picture
    picture_path = f"images/{random.randint(1,5)}.jpg" 
    with open(picture_path, 'rb') as f:
        picture = MIMEBase('application', 'octet-stream')
        picture.set_payload(f.read())
        encoders.encode_base64(picture)
        picture.add_header('Content-Disposition', f'attachment; filename={picture_path}')
        msg.attach(picture)

    # Send the email
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.send_message(msg)
else:
    print("No birthdays today.")







