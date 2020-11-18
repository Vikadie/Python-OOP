from datetime import timedelta
from report_generator import generate_report
from email_sender import email_send
from report_formatter import format_report

from pprint import pprint

def main():
    report = generate_report(duration = timedelta(seconds = 2))

    formatted = format_report(report)

    print(formatted)
    email_send(formatted)

if __name__ == '__main__':
    main()