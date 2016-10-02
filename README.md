## SmsResender

Simple Python project for backup SMS messages to mailbox. Script reads SMS messages from GPRS modem (Huawei E220) and send them to the Gmail mailbox. 

Script runs on my Raspberry Pi and it runs every minute over CRON scheduler. I tested only with my GPRS modem Huawei E220, but script should works with other GPRS modem too.
    
## Todo

There're lots of things to do (this is just a first functional version).

* ~~Backup SMS to the GMAIL mailbox~~
* ~~Contacts in simple CSV file. Convert phone numbers from SMS to theirs contacts names.~~
* Read Google Contacts and convert phone numbers from SMS to theirs contacts names
* Errors notification
* Automatic identify GPRS modem port
* Forward SMS to another mobile number
* Send notification about internet outage, problem with email
* ~~Change SMS status to unread, if error with mail, forwarding occurred~~
* Create daemon for checking new SMS messages (currently periodically runs by CRON)
* Notification templates

## Installation

* Download, checkout project from GitHub
* Edit setting file - sms.ini
* Edit contacts.csv
* 

### SMS.INI

**Modem port**

Probably you need to change modem port.
`
[modem]
port = /dev/tty.HUAWEIMobile-Pcui
`

* In Windows platform looks like: COM5 (you can find in Control Panel / Device manager)
* In macOS platform looks like: /dev/tty.HUAWEIMobile-Pcui (try ls -l /dev/tty.*)
* In Linux patform looks like: /dev/ttyUSB1 (try ls -la /dev/ttyU*)

**SMTP**

If you want to use Gmail SMTP, there are a few steps you need to do before you can send emails through Gmai. You'll need to tell Google to allow you to connect via SMTP, by allowing less secure apps to access your account - https://support.google.com/accounts/answer/6010255. Before testing, turn on debug level mode for smtplib in sms.ini (debuglevel = True). Please, consider not to use your primary google account. 

## Usage

Run `python run.py`

## History

* 1.2: Reading contacts from CSV file, solved problem with UTF in mail subject
* 1.1: Initial version with mail backup.
* 1.0: Initial version without mail backup. Script only reads SMS messages from modem.


## Credits

Author: Tomas Vecera

## License

License: GPLv3
