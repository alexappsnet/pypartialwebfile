import logging
import unittest

from partial_web_file import get_file_content_from_web_zip, get_file_contents_from_web_zip

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('UnzipTest')

URL = 'http://downloads.arduino.cc/libraries/github.com/adafruit/DHT_sensor_library-1.3.8.zip'
FILE = 'DHT_sensor_library-1.3.8/keywords.txt'


class UnzipTest(unittest.TestCase):
    def test_download_file_from_zip(self):
        content = get_file_content_from_web_zip(URL, FILE).decode()
        log.info('Got content:\n%s', content)
        self.assertTrue('KEYWORD1' in content)
        self.assertTrue('KEYWORD2' in content)

    def test_download_many_files_from_zip(self):
        counter = [0]

        def on_content(path, content):
            counter[0] += 1
            content = content.decode()
            log.info('Got content:\n%s', content)
            self.assertTrue(FILE, path)
            self.assertTrue('KEYWORD1' in content)
            self.assertTrue('KEYWORD2' in content)

        get_file_contents_from_web_zip(URL, [FILE, FILE], on_content)
        self.assertEqual(2, counter[0])
