import logging
import requests
import os
import unittest

from partial_web_file import get_partial_web_file

logging.basicConfig(level=logging.INFO)

log = logging.getLogger('FileTest')


class FileTest(unittest.TestCase):
    def test_download_partial_file(self):
        test_url = 'https://alexapps.net/files/mobile_app_boxingitimer_icon.png'
        partial_content = get_partial_web_file(test_url, start_position=1, length=3)
        log.info('length: %d', len(partial_content))
        log.info('content: %s', partial_content)
        log.info('string: %s', partial_content.decode())
        self.assertEqual(b'PNG', partial_content)
