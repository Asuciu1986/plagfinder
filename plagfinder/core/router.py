# -*- coding: utf-8 -*-

import sys
import os
import telnetlib
import time
import urllib
import configparser

class Router():
    def __init__(self, window):
        self.window = window

        # Getting configuration
        conf = configparser.ConfigParser()
        conf.read(os.path.join(os.getcwd(), 'conf', 'router'))

        self.host = conf['Router']['ip']
        self.user = conf['Router']['user'] + '\n'
        self.pwrd = conf['Router']['pwrd'] + '\n'

    def internet_test(self):
        try:
            r = urllib.request.urlopen('http://216.58.208.206', timeout=1)
            return True
        except urllib.request.URLError as err:
            pass
        return False

    def restart_router(self):
        # Emit status bar message
        self.window.update_status_sign.emit("Restarting router...")

        # Connect to host using telnet protocol
        tn = telnetlib.Telnet(self.host)
        time.sleep(3)

        # Enter login when requested
        tn.read_until('Login: '.encode(sys.stdout.encoding))
        tn.write(self.user.encode(sys.stdout.encoding))
        time.sleep(2)

        # Enter password when requested
        tn.read_until('Password: '.encode(sys.stdout.encoding))
        tn.write(self.pwrd.encode(sys.stdout.encoding))
        time.sleep(2)

        # Reboot
        tn.read_until('> '.encode(sys.stdin.encoding))
        tn.write(b'reboot\n')

        # Wait until internet connection is back
        while True:
            if self.internet_test():
                break
            else:
                time.sleep(1)

        # Emit success message
        self.window.update_status_sign.emit("Reboot done")
