import configparser
import csv
import io
import os
import urllib.parse

import requests


# Module information.
__author__ = 'Anthony Farina'
__copyright__ = 'Copyright 2021, PRTG Duplicate Device Finder'
__credits__ = ['Anthony Farina']
__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = 'Anthony Farina'
__email__ = 'farinaanthony96@gmail.com'
__status__ = 'Released'


# Global variables from the config file for easy referencing.
CONFIG = configparser.ConfigParser()
CONFIG_PATH = '/../configs/PRTG-Duplicate-Device-Finder-config.ini'
CONFIG.read(os.path.dirname(os.path.realpath(__file__)) + CONFIG_PATH)
SERVER_URL = CONFIG['PRTG Info']['server-url']
USERNAME = urllib.parse.quote_plus(CONFIG['PRTG Info']['username'])
PASSWORD = urllib.parse.quote_plus(CONFIG['PRTG Info']['password'])
PASSHASH = urllib.parse.quote_plus(CONFIG['PRTG Info']['passhash'])


# This script looks at devices in a PRTG instance and detects if a device's name or IPv4 address appears more
# than once for a probe. It then prints its results to the console.
def prtg_duplicate_device_finder() -> None:
    # Use the PRTG API to get a list of all devices.
    prtg_devices_url = SERVER_URL + '/api/table.xml?content=devices&columns=' \
                                    'name,probe,status,host' \
                                    '&sortby=probe&output=csvtable&count=50000' \
                                    '&username=' + USERNAME + '&password=' + PASSWORD
    prtg_devices_resp = requests.get(url=prtg_devices_url)
    prtg_devices_strio = io.StringIO(prtg_devices_resp.text)
    prtg_devices = csv.DictReader(prtg_devices_strio)

    # Go through the devices for each probe to find duplicate names and/or IP addresses.
    curr_probe_name = '########'
    curr_name_dict = dict()
    curr_ip_dict = dict()
    for device in prtg_devices:
        # Check if we are moving on to a new probe.
        if curr_probe_name != device['Probe']:
            # Reset the dictionaries and probe name.
            curr_name_dict = dict()
            curr_ip_dict = dict()
            curr_probe_name = device['Probe']

        # Check if this device name has been seen before for this probe.
        if curr_name_dict.get(device['Object']) is None:
            curr_name_dict[device['Object']] = device
        # We found a duplicate device name.
        else:
            duped_device = curr_name_dict[device['Object']]
            print('Duplicate device name found! Clover: ' + device['Probe'] + ' ' + device['Object'] +
                  ' | IP: ' + device['Host'] + ' is a duplicate of')
            print('                             Clover: ' + duped_device['Probe'] + ' ' + duped_device['Object'] +
                  ' | IP: ' + duped_device['Host'])

        # Check if this device IP address has been seen before for this probe.
        if curr_ip_dict.get(device['Host']) is None:
            curr_ip_dict[device['Host']] = device
        # We found a duplicate IP address.
        else:
            duped_device = curr_ip_dict[device['Host']]
            print('Duplicate IP address found! Clover: ' + device['Probe'] + ' ' + device['Object'] +
                  ' | IP: ' + device['Host'] + ' is a duplicate of')
            print('                            Clover: ' + duped_device['Probe'] + ' ' + duped_device['Object'] +
                  ' | IP: ' + duped_device['Host'])


# Runs the script. This function has no input.
if __name__ == '__main__':
    prtg_duplicate_device_finder()
