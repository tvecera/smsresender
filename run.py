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

from params import Configuration
from modem import Modem
from mail import Mail

log = logging.getLogger('smsresender.run')


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=eval(logging.DEBUG))
    log.debug('Start...')
    config = Configuration()
    modem = Modem(config)
    sms = modem.readsms()
    mail = Mail(config)
    for item in sms:
        mail.notify(item)


if __name__ == '__main__':
    main()
