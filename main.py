from modules.log_capturing_module import LogCapturingModule
from modules.record_manager import RecordManager
from modules.record import Record
from modules.report_viewer import ReportViewer

def main():
    # capturing_module = LogCapturingModule("C:\\Users\\shawn\\OneDrive\\Desktop\\Demo\\Python_Project\\my_csv.csv")
    # logs_by_url = capturing_module.capture_logs()
    # print(logs_by_url['https://www.google.com/'[0]]['network_log'])
    # record_manager = RecordManager(logs_by_url)
    # records = record_manager.get_records()
    # print(type(records[0].production_logs))

    capturing_module = LogCapturingModule()
    capturing_module.urls_to_capture = ['http://www.wellsfargo.com/search/', 'http://www.google.com/']
    logs_by_url = capturing_module.capture_logs()
    print(logs_by_url['http://www.wellsfargo.com/search/']['console_logs'][0])


if __name__ == '__main__':
    main()





