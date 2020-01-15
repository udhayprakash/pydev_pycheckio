#!/usr/bin/python
"""
Purpose: https://py.checkio.org/mission/sendgrid-sendone/solve/
"""

import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = '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'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(API_KEY)


def send_email(email, name):
    message = Mail(
        from_email='from_email@example.com',
        to_emails=email,  # 'to@example.com',
        subject=SUBJECT,  # 'Sending with Twilio SendGrid is Fun',
        html_content=BODY.format(name))  # '<strong>and easy to do anywhere, even with Python</strong>')
    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')

# print(f'sg.version              :{sg.version}')
# print(f'sg.useragent            :{sg.useragent}')
# print(f'sg.host                 :{sg.host}')
# print(f'sg.impersonate_subuser  :{sg.impersonate_subuser}')
