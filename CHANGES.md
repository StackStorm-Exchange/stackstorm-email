# Change Log

# 2.0.3

- Set smtp username and password as not required. 

# 2.0.2

- Add date to header in the SendEmail action so the spam score will be lower

# 2.0.1

- Fix Python 3 related issue in IMAPSensor

# 2.0.0

* Drop Python 2.7 support

# 1.1.6

- Use the correct variable for _attachment_datastore_ttl in imap_sensor.
# 1.1.5

- Add explicit support for Python 2 and 3

# 1.1.4

- Pin tld dependency to <0.11 for Python < 3.0

# 1.1.3

- Minor linting fixes

# 1.1.1

- Version bump to fix tagging issues

# 1.1.0

- Updated to flanker >= 0.9.0
- Updated send_email.py to support Unicode in subject and message fields

# 1.0.3

- Add `attachments` parameter to the send_email action. Expected a list of file paths if given, to be attached to the email.

# 1.0.2

- Add `mime` parameter to the send_email action.  If the value is `html`, the mime type of the email will be `text/html`.  Otherwise, the mime will be `text/plain`.

# 1.0.0

- Replaced 'imap_mailboxes' with 'imap_accounts' and 'smtp_accounts'. Replaced 'smtp_list_ip'
  and 'smtp_listen_port' with 'sensor_smtp_listen_ip' and 'sensor_smtp_listen_port' respectively.
  You must update any existing email.yaml file.

# 0.4.0

- Changed `email_to` data type from string to list in order to support multiple email address
  destinations.

# 0.3.0

- Updated action `runner_type` from `run-python` to `python-script`

# 0.2.0

- Rename `config.yaml` to `config.schema.yaml` and update to use schema.

# 0.1.0

- First release 
