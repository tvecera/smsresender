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
import serial
import time
from sms import Sms


class Modem:
    log = logging.getLogger('smsresender.Modem')

    config = None
    conn = None

    def __init__(self, config):
        self.config = config
        self.connect()

    def connect(self):
        self.log.debug('Try connect to modem... [%s,%s,%s]', self.config.modem.port, self.config.modem.baudrate,
                       self.config.timeout)
        self.conn = serial.Serial(port=self.config.modem.port, baudrate=self.config.modem.baudrate,
                                  timeout=self.config.timeout)

        # Init modem eg. turn off echo, sms text mode
        for command in self.config.modem.initcommands:
            self.write(command)

    def readsms(self):
        cmd = self.config.rx.readUnread
        self.conn.flushInput()
        self.conn.flushOutput()

        self.write(cmd, False)
        data = self.read()
        # Start from 1, first item isn't SMS message (b')
        smslist = data.split('+CMGL:')[1:]
        result = []
        self.log.debug('Number of SMS: %s', len(smslist))

        for item in smslist:
            result.append(Sms(item, self.config))

        return result

    def write(self, command, checkresponse=True):
        cmd = (command + self.config.RX_EOL).encode('ascii')
        self.log.debug('IN: [%s]', cmd)
        self.conn.write(cmd)
        if checkresponse:
            return self.checkresponse()

        return False

    def checkresponse(self):
        data = self.read()

        if self.config.RX_ERROR.search(data):
            self.log.error('RESPONSE: ERROR [%s]', data)
        elif self.config.RX_OK.search(data):
            self.log.debug('RESPONSE: OK')
            return True
        else:
            self.log.error('RESPONSE: EMPTY [%s]', data)

        return False

    def read(self):
        data = ''
        time.sleep(self.config.rx.waiting)
        while self.conn.in_waiting > 0:
            data += str(self.conn.read(self.conn.in_waiting))
            self.log.debug('[%s]', data)

        data = data.replace('\\r', '').replace('\\n', self.config.TXT_DELIM)

        return data
