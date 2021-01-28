import os
from st2common.runners.base_action import Action
from smtplib import SMTP
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail(Action):
    def run(self, email_from, email_to, subject, message,
            account, email_cc=None, mime="plain", attachments=None):

        if mime not in ['plain', 'html']:
            raise ValueError('Invalid mime provided: ' + mime)

        accounts = self.config.get('smtp_accounts', None)
        if accounts is None:
            raise ValueError('"smtp_accounts" config value is required to send email.')
        if not accounts:
            raise ValueError('at least one account is required to send email.')

        try:
            kv = {}
            for a in accounts:
                kv[a['name']] = a
            account_data = kv[account]
        except KeyError:
            raise KeyError('The account "{}" does not seem to appear in the configuration. '
                           'Available accounts are: {}'.format(account, ",".join(kv.keys())))

        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = email_from
        msg['To'] = ", ".join(email_to)
        msg.attach(MIMEText(message, mime, 'utf-8'))
        if email_cc is None:
            email_cc = []

        if email_cc:
            msg['Cc'] = ", ".join(email_cc)
            email_to += email_cc

        attachments = attachments or tuple()
        for filepath in attachments:
            filename = os.path.basename(filepath)
            with open(filepath, 'rb') as f:
                part = MIMEApplication(f.read(), Name=filename)
            part['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
            msg.attach(part)

        s = SMTP(account_data['server'], int(account_data['port']), timeout=20)
        s.ehlo()
        if account_data.get('secure', True) is True:
            s.starttls()
        if account_data.get('smtp_auth', True) is True:
            s.login(account_data['username'], account_data['password'])
        s.sendmail(email_from, email_to, msg.as_string())
        s.quit()
        return
