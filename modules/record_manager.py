from .record import Record
import re

class RecordManager:

    def __init__(self, logs_by_url: dict):
        self.logs_by_url = logs_by_url
        self.records = []
        self._initialize_records()

    def _initialize_records(self):
        endpoints = set()
        pattern = r'https?://[^/]+(?:\:\d+)?(?P<endpoint>/[^\?#]*)'

        # Extract unique endpoints
        for url in self.logs_by_url.keys():
            match = re.match(pattern, url)
            if match:
                endpoint = match.group('endpoint')
                endpoints.add(endpoint)

        # Create Record objects for each unique endpoint
        for endpoint in endpoints:
            record = Record(endpoint=endpoint)
            self.records.append(record)

        # Assign URLs and logs to the records
        for url, logs in self.logs_by_url.items():
            match = re.search(pattern, url)
            if match:
                endpoint = match.group('endpoint')
                record = self._find_record_by_endpoint(endpoint)
            else:
                print(f"No match found for URL: {url}")
            
            if "https://www.wellsfargo.com" in url:
                record.production_url = url
                record.production_logs = logs
            else:
                record.testing_url = url
                record.testing_logs = logs

    

    def _find_record_by_endpoint(self, endpoint):
        for record in self.records:
            if record.endpoint == endpoint:
                return record
        return None
    
    def get_records(self):
        """
        Retrieve the list of records maintained by the RecordManager.

        Returns:
            list[Record]: List of Record objects.
        """
        return self.records