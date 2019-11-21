import logging
import unittest

from partial_web_file import get_file_content_from_web_zip

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('UnzipTest')
 
 
class UnzipTest(unittest.TestCase):
    def test_download_partial_file(self):
        url = 'http://downloads.arduino.cc/libraries/github.com/adafruit/DHT_sensor_library-1.3.8.zip'
        file = 'DHT_sensor_library-1.3.8/keywords.txt'
        content = get_file_content_from_web_zip(url, file).decode()
        log.info('Got content:\n%s', content)
        self.assertTrue('KEYWORD1' in content)
        self.assertTrue('KEYWORD2' in content)
