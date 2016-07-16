# -*- coding: utf-8 -*-
'''
    :codeauthor: Iggy
    :copyright: © 2016 by the SaltStack Community
    :license: Apache 2.0, see LICENSE for more details.

    Load grains from the metadata service in the Vultr cloud provider
        https://www.vultr.com/metadata
        https://vultr.com
        https://discuss.vultr.com/discussion/582/cloud-init-user-data-testing

    This service appears to currently be in flux. If this doesn't work, please
    contact iggy in the #salt irc channel.
'''

import logging
import requests

LOG = logging.getLogger(__name__)

MD_BASE_URI = "http://169.254.169.254/v1"
__virtualname__ = "vultr"


def __virtual__():
    '''
    We should only load if this is actually a vultr instance
    '''
    try:
        ret = requests.get(MD_BASE_URI + '.json')
        # check to see if we get a json response
        if ret.content.find(":") <= 0:
            return False
        return __virtualname__
    # I really don't feel like listing all the possible exceptions
    # pylint: disable=broad-except
    except Exception:
        return False


def vultr():
    '''
    Return Vultr metadata.
    '''
    vultrmd = {}
    with requests.Session() as sess:
        resp = sess.get("{0}.json".format(MD_BASE_URI))
        vultrmd = resp.json()

    return {'vultr': vultrmd}


if __name__ == '__main__':
    print vultr()
