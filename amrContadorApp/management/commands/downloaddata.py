import datetime
import email
import imaplib
import os
from urllib.parse import urlparse

from decouple import config
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named arguments
        parser.add_argument('--mail-url', default=config('MAIL_URL'))
        parser.add_argument('--path-all-file-xlsx', default=config('PATH_All_FILE_XLSX'))

    def handle(self, *args, **options):
        mail_url = urlparse(options['mail_url'])
        mail_host = mail_url.hostname
        mail_host_port = mail_url.port
        mail_user = mail_url.username
        mail_user_pass = mail_url.password
        path_all_file_xlsx = options['path_all_file_xlsx']

        mail = imaplib.IMAP4_SSL(mail_host, mail_host_port)
        mail.login(mail_user, mail_user_pass)
        mail.select('Inbox')
        date = imapDateText(datetime.date.today())

        # type, data = mail.search(None, 'ALL')
        # type, data = mail.search(None, ('UNSEEN'), '(SENTSINCE {0})'.format(date))
        # type, data = mail.search(['SINCE', datetime.today()])
        type, data = mail.uid('search', None, '(OR UNSEEN (SINCE %s))' % date)
        mail_ids = data[0]
        id_list = mail_ids.split()

        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]  # converts byte literal to string removing b''
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(
                raw_email_string)  # downloading attachments
            for part in email_message.walk():
                # this part comes from the snipped I don't understand yet...
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                fileName = part.get_filename()
                if bool(fileName):
                    filePath = os.path.join(path_all_file_xlsx, fileName)
                    if not os.path.isfile(filePath):
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
                        subject = str(email_message).split(
                            "Subject: ", 1)[1].split("\nTo:", 1)[0]


def imapDateText(dt):
    months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    return '%02d-%s-%04d' % (dt.day, months[dt.month - 1], dt.year)