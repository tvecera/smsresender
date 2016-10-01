## SmsResender

Simple Python project for backup SMS messages to mailbox. Script reads SMS messages from GPRS modem (Huawei E220) and send them to the Gmail mailbox. 

Script run on my Raspberry Pi and it runs every minute over CRON scheduler. 
    
## Todo

There're lots of things to do (this is just a first functional version).

~~* Backup SMS to the gmail mailbox
* Read Google Contacts and convert phone numbers from SMS to theirs contacts names.
* Errors notification
* Automatic identify GPRS modem port

## Installation

TODO: Describe the installation process

## Usage

Run `python run.py`

## History

1.0: Initial version without mail backup. Script only reads SMS messages from modem.
1.0: Initial version with mail backup.

## Credits

Author: Tomas Vecera

## License

License: GPLv3