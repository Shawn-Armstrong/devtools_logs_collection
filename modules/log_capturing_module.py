# """
# The LogCapturingModule is responsible for capturing both console and network logs 
# from a list of specified URLs using Chrome devtools. It organizes the captured logs 
# into a dictionary, with each URL as a key. The value for each URL key is itself a 
# dictionary, containing two keys: 'console_logs' and 'network_logs'. Both of these 
# keys map to a list of dictionaries, where each dictionary within the list represents 
# an individual log entry.

# The structure of the logs is as follows:
#     {
#         'http://www.example.com': {
#             'console_logs': [
#                 {'level': 'WARNING', 'source': 'security', 'message': 'some message'},
#                 {'level': 'INFO', 'source': 'application', 'message': 'another message'},
#                 ...
#             ],
#             'network_logs': [...]
#         },
#         'http://www.example2.com': {...},
#         ...
#     }

# The method `capture_logs()` is the main method for initiating log capturing for the 
# specified URLs.

# Accessing the Console Logs:
#     - logs_by_url[urls[0]]['network_log']: This accesses the 'network_log' list for 
#     the first URL. Printing will yield the entire log.
#     - logs_by_url[urls[0]]['network_log']: This accesses the first dictionary 
#     within the 'network_log'. Printing will yield the entire log entry.
#     - logs_by_url[urls[0]]['network_log'][0]: This accesses the `status_code` value
#     within the first dictionary of the 'network_log' list.

# Attributes:
#     urls_to_capture (list of str): The URLs for which logs are to be captured.

# Methods:
#     capture_logs(): Initiates log capturing for the specified URLs.
#     capture_logs_for_url(url): Captures logs for a specific URL.
#     get_console_logs(): Retrieves the console logs for a specific URL.
#     get_network_logs(): Retrieves the network logs for a specific URL.
# """

# import csv
# import re
# from selenium import webdriver

# class LogCapturingModule:

#     def __init__(self, csv_path):
#         self.driver = self.setup_driver()
#         self.urls_to_capture = self.parse_csv(csv_path)

#     def setup_driver(self):
#         options = webdriver.ChromeOptions()
#         desired_capabilities = options.to_capabilities()
#         desired_capabilities['goog:loggingPrefs'] = {'browser': 'ALL', 'performance': 'ALL'}
#         return webdriver.Chrome(desired_capabilities=desired_capabilities)

#     def parse_csv(self, csv_path):
#         urls = []
#         unique_endpoints = set()

#         # Define a regular expression pattern to extract the endpoint
#         pattern = r'https?://[^/]+(?:\:\d+)?(?P<endpoint>/[^\?#]*)'

#         with open(csv_path, 'r') as csvfile:
#             reader = csv.reader(csvfile)
#             for row in reader:
#                 url = row[0]
#                 urls.append(url)
                
#                 # Extract the endpoint from the URL
#                 match = re.match(pattern, url)
#                 if match:
#                     endpoint = match.group('endpoint')
#                     unique_endpoints.add(endpoint)

#         # Add Wells Fargo URLs for each unique endpoint
#         # for endpoint in unique_endpoints:
#         #     urls.append(f'https://www.wellsfargo.com/{endpoint}')

#         return urls


#     def capture_logs_for_url(self, url):
#         self.driver.get(url)
#         console_logs = self.driver.get_log('browser')
#         network_logs = self.driver.get_log('performance')
#         return {
#             'url': url,
#             'console_logs': console_logs,
#             'network_logs': network_logs
#         }

#     def capture_logs(self):
#         logs_by_url = {url: self.capture_logs_for_url(url) for url in self.urls_to_capture}
#         return logs_by_url

#     def close(self):
#         self.driver.quit()


from selenium import webdriver

class LogCapturingModule:

    """
    The LogCapturingModule is responsible for capturing both console and network logs 
    from a list of specified URLs using Chrome devtools. It organizes the captured logs 
    into a dictionary, with each URL as a key. The value for each URL key is itself a 
    dictionary, containing two keys: 'console_logs' and 'network_logs'. Both of these 
    keys map to a list of dictionaries, where each dictionary within the list represents 
    an individual log entry.

    The structure of the logs is as follows:
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

    The method `capture_logs()` is the main method for initiating log capturing for the 
    specified URLs.

    Accessing the Console Logs:
        - logs_by_url[urls[0]]['network_log']: This accesses the 'network_log' list for 
        the first URL. Printing will yield the entire log.
        - logs_by_url[urls[0]]['network_log'][0]: This accesses the first dictionary 
        within the 'network_log'. Printing will yield the entire log entry.
        - logs_by_url[urls[0]]['network_log'][0]: This accesses the `status_code` value
        within the first dictionary of the 'network_log' list.

    Attributes:
        urls_to_capture (list of str): The URLs for which logs are to be captured.

    Methods:
        capture_logs(): Initiates log capturing for the specified URLs.
        capture_logs_for_url(url): Captures logs for a specific URL.
        get_console_logs(): Retrieves the console logs for a specific URL.
        get_network_logs(): Retrieves the network logs for a specific URL.
    """
        
    def __init__(self):
        self.driver = self.setup_driver()
        self.urls_to_capture = [] # This is a list of URLs for which logs are to be captured.

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        desired_capabilities = options.to_capabilities()
        desired_capabilities['goog:loggingPrefs'] = {'browser': 'ALL', 'performance': 'ALL'}
        return webdriver.Chrome(desired_capabilities=desired_capabilities)

    def capture_logs_for_url(self, url):
        self.driver.get(url)
        console_logs = self.driver.get_log('browser')
        network_logs = self.driver.get_log('performance')
        return {
            'url': url,
            'console_logs': console_logs,
            'network_logs': network_logs
        }

    def capture_logs(self):
        logs_by_url = {url: self.capture_logs_for_url(url) for url in self.urls_to_capture}
        return logs_by_url

    def close(self):
        self.driver.quit()

# Example Usage
capturing_module = LogCapturingModule()
capturing_module.urls_to_capture = ['http://example.com/staging', 'http://example.com/production']
logs_by_url = capturing_module.capture_logs()
capturing_module.close()
