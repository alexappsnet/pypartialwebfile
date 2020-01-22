import logging
import unittest

from partial_web_file import get_file_content_from_web_zip, get_file_contents_from_web_zip

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('UnzipTest')

URL = 'https://alexapps.net/files/huge.zip'
FILE = 'a/1.txt'
EXPECTED_CONTENT = b'Hello from a/1.txt\n'


class UnzipTest(unittest.TestCase):
    def test_download_file_from_zip(self):
        content = get_file_content_from_web_zip(URL, FILE)
        log.info('Got content:\n%s', content.decode())
        self.assertEqual(EXPECTED_CONTENT, content)

    def test_download_many_files_from_zip(self):
        counter = [0]

        def on_content(path, content):
            counter[0] += 1
            log.info('Got content:\n%s', content.decode())
            self.assertTrue(FILE, path)
            self.assertEqual(EXPECTED_CONTENT, content)

        get_file_contents_from_web_zip(URL, [FILE, FILE], on_content)
        self.assertEqual(2, counter[0])
