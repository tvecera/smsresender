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

import smtplib
import logging


class Mail:
    log = logging.getLogger('smsresender.Mail')

    config = None

    def __init__(self, config):
        self.config = config

    def notify(self, sms):
        subject = 'SMS - %s - %s' % (sms.fromContact, sms.fromPhone)
        body = sms.msg
        email_text = """\
From: %s
To: %s
Subject: %s

%s
            """ % (self.config.mail.fromMail, self.config.mail.toMail, subject, body)

        try:
            server = smtplib.SMTP_SSL(self.config.mail.smtp, self.config.mail.port)
            server.set_debuglevel(self.config.mail.debuglevel)
            server.ehlo()
            server.login(self.config.mail.user, self.config.mail.password)
            server.sendmail(self.config.mail.fromMail, self.config.mail.toMail, email_text)
            server.close()

            self.log.debug('Email sent')
        except:
            self.log.error('Problem with sending email notification...')