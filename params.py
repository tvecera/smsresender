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
import re
from configparser import ConfigParser


class Configuration:
    CONFIG_FILE = 'sms.ini'
    RX_EOL = "\r\n"
    RX_OK = re.compile(r'OK')
    RX_ERROR = re.compile(r'ERROR|(\+CM[ES] ERROR: \d+)|(COMMAND NOT SUPPORT)')

    log = logging.getLogger('smsresender.Configuration')

    modem = None
    rx = None
    timeout = None

    parser = ConfigParser()

    def __init__(self):
        self.log.debug('Read confing file... %s', self.CONFIG_FILE)
        self.parser.read(self.CONFIG_FILE)

        self.modem = Modem(self.parser)
        self.rx = Rx(self.parser)
        self.timeout = int(self.parser.get('global', 'timeout'))

        self.log.debug('timeout: %s', self.timeout)


class Modem:
    log = logging.getLogger('smsresender.Modem')

    port = None
    baudrate = None
    initcommands = list()

    def __init__(self, config):
        self.port = config.get('modem', 'port')
        self.baudrate = int(config.get('modem', 'baudrate'))

        # This is little bit ugly, but viable solution
        self.initcommands = config.get('modem', 'initcommands').split(',')

        self.log.debug('port: %s', self.port)
        self.log.debug('baudrate: %s', self.baudrate)
        self.log.debug('initcommands: %s', self.initcommands)


class Rx:
    log = logging.getLogger('smsresender.Rx')
    waiting = 0
    readAll = ''
    readUnread = ''
    readRead = ''

    def __init__(self, config):
        self.waiting = int(config.get('rx', 'waiting'))
        self.log.debug('Read waitinf: %s', self.waiting)
