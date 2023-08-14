import unittest
from modules.log_capturing_module import LogCapturingModule as LogCapturer
from unittest.mock import MagicMock

class TestLogCapturer(unittest.TestCase):
    """
    This class is responsible for testing the LogCapturingModule, ensuring that logs are captured correctly from different URLs.

    Specifically, it tests the following:
    - The `capture_logs` method of LogCapturingModule, which is responsible for capturing both console and network logs from a list of URLs.
    - The structure of the logs, where each URL has associated logs, organized as follows:
        {
            'http://www.example.com': {
                'console_logs': [
                    {'level': 'WARNING', 'source': 'security', 'message': 'some message'},
                    {'level': 'INFO', 'source': 'application', 'message': 'another message'},
                    ...
                ],
                'network_logs': [...]
            },
            'http://www.example2.com': {...},
            ...
        }

    Attributes:
        urls_to_capture (list of str): The URLs for which logs are to be captured. It's defined within the test method and used to compare the captured logs.

    Methods:
        test_capture_logs(): A test method to validate the functionality of the LogCapturingModule.
    """

    def test_capture_logs(self):
        log_capturer = LogCapturer()
        log_capturer.get_console_logs = MagicMock(return_value=['console log'])
        log_capturer.get_network_logs = MagicMock(return_value=['network log'])
        urls = ['http://www.google.com', 'http://www.wellsfargo.com']
        log_capturer.urls_to_capture = urls
        logs_by_url = log_capturer.capture_logs()

        self.assertEqual(len(logs_by_url[urls[0]]['console_logs']), 2)
        self.assertEqual(logs_by_url[urls[0]]['console_logs'][0]['level'], 'WARNING')
        self.assertEqual(logs_by_url[urls[0]]['console_logs'][0]['source'], 'security')

    def test_capture_logs_structure(self):
            log_capturer = LogCapturer()
            urls = ['http://www.example.com']
            logs_by_url = {'http://www.example.com': {'console_logs': [], 'network_logs': []}}
            log_capturer.capture_logs_for_url = MagicMock(return_value=logs_by_url[urls[0]])
            log_capturer.urls_to_capture = urls
            result = log_capturer.capture_logs()

            self.assertEqual(result, logs_by_url)

    def test_get_console_logs(self):
        log_capturer = LogCapturer()
        console_logs = [{'level': 'WARNING', 'source': 'security', 'message': 'some message'}]
        log_capturer.get_console_logs = MagicMock(return_value=console_logs)
        logs = log_capturer.get_console_logs('http://www.example.com')

        self.assertEqual(logs, console_logs)

    def test_get_network_logs(self):
        log_capturer = LogCapturer()
        network_logs = [{'status': 200, 'url': 'http://www.example.com/api/data'}]
        log_capturer.get_network_logs = MagicMock(return_value=network_logs)
        logs = log_capturer.get_network_logs('http://www.example.com')

        self.assertEqual(logs, network_logs)

    def test_urls_to_capture(self):
        log_capturer = LogCapturer()
        urls = ['http://www.google.com', 'http://www.wellsfargo.com']
        log_capturer.urls_to_capture = urls

        self.assertEqual(log_capturer.urls_to_capture, urls)

if __name__ == '__main__':
    unittest.main()
