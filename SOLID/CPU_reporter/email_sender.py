import smtplib, ssl

port = 465
password = input("Give me your pass:")
gmail_username = "@gmail.com"


def email_send(report):
    with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
        server.login(gmail_username, password)
        server.sendmail(gmail_username, gmail_username, f"""\
        Subject:Report

        {report}
        This mail is send from Python!
        """)  # sendmail(sender, to, message_text)