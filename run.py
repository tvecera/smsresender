#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016  Tomas Vecera
#
# This file is part of SmsSender
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import sys

from serial import SerialException
from params import Configuration
from modem import Modem
from mail import Mail
from contacts import Contacts

log = logging.getLogger('smsresender.run')


def main():
    logging.basicConfig(filename='smsresender.log', format='%(asctime)s - %(levelname)s: %(message)s',
                        level=logging.DEBUG)
    log.debug('Start...')

    try:
        config = Configuration()
        modem = Modem(config)
        sms = modem.readsms()

        mail = Mail(config)
        contacts = Contacts(config)

        for item in sms:
            item.fromContact = contacts.readcontactfromfile(item)
            mail.notify(item)
            # Delete notified SMS
            modem.deletesms(item.id)

    except SerialException as e:
        log.error('Problem with connection to modem: %s', e.strerror)
        sys.exit('Error occurred, please check log file!!!')
    except Exception:
        sys.exit('Error occurred, please check log file!!!')


if __name__ == '__main__':
    main()
