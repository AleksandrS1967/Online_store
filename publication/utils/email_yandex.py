import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

password = os.getenv("COTH")


def send_message_mail(emails: list, text: str):
    login = "koroleva587@yandex.ru"

    message_text = MIMEText(f"{text}", "plain", "utf-8")
    message_text["Subject"] = Header("Важно!!!", "utf-8")
    message_text["From"] = login
    message_text["To"] = ", ".join(emails)

    smtp_ = smtplib.SMTP("smtp.yandex.ru", 587, timeout=10)

    try:
        smtp_.starttls()
        smtp_.login(login, password)
        smtp_.sendmail(message_text["From"], emails, message_text.as_string())

    except Exception as ex:
        print(ex)
    finally:
        smtp_.quit()
