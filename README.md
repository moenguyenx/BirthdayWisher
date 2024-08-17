# Birthday Wisher
Executed by Moenguyenx

## Overview

The **Birthday Wisher** is a fun Python project designed to send personalized birthday emails to friends. 

The application reads birthday data from a JSON file and sends an email with a random letter template and **random cat meme** to friends celebrating their birthday.

You can have a small Linux server and set up cron job to run daily.


## Prerequisites

- Python 3.6 or higher
- An active Gmail account ([HOW TO GET SMTP Password](https://www.gmass.co/blog/gmail-smtp/))

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/birthday-wisher.git
   cd birthday-wisher
   ```

2. **Config your Email and Password in 'main.py'**

    ```bash
    MY_EMAIL = "your_email@gmail.com"
    PASSWORD = "your_smtp_password"
    ```

3. **Prepare your JSON data**

    Birthday format should be **"day(1,31)-month(1,12)"**
    ```bash
    [
        {
            "name": "Friend Name",
            "email": "friend@example.com",
            "birthday": "15-8"
        }, 
        ...list goes on
    ]
    ```

4. **Hit run haha or you can setup cronjob on Linux to run the script daily**