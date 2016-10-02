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


class Contacts:
    log = logging.getLogger('smsresender.Contacts')

    config = None

    def __init__(self, config):
        self.config = config

    def readcontactfromfile(self, sms):
        result = []
        with open(self.config.contacts.file, 'rb') as f:
            for row in f:
                row = row.decode('utf-8').split(';')
                # Quick fix for Windows platform, UNIX LF
                row[3] = row[3].replace('\n', '')
                if row[3] == sms.fromPhone.replace('+', ''):
                    result = row
        out = ''
        if len(result) > 0:
            out = '%s %s %s' % (result[2], result[0], result[1])
        self.log.debug('Contact for phone %s: %s', sms.fromPhone, out)

        return out
