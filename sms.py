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


class Sms:
    log = logging.getLogger('smsresender.Sms')

    id = 0
    status = None
    fromPhone = None
    fromContact = None
    date = None
    time = None
    msg = None
    original = None

    def __init__(self, rx, config):
        self.original = rx
        result = rx.split(config.TXT_DELIM)
        self.parseheader(result[0])
        self.parsemsg(result[1])
        self.log.debug('SMS: [%s, %s, %s, %s, %s]', self.id, self.status, self.fromPhone,
                       self.date + ' ' + self.time, self.msg)

    def parseheader(self, rx):
        rx = rx.replace('"', '')
        header = rx.split(',')
        self.id = int(header[0].lstrip())
        self.status = header[1]
        self.fromPhone = header[2]
        self.date = header[4]
        self.time = header[5]

    def parsemsg(self, rx):
        sms = rx.split('|')
        self.msg = sms[0].lstrip()
