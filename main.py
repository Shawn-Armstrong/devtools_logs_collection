from modules.log_capturing_module import LogCapturingModule

def main():
    capturing_module = LogCapturingModule()
    capturing_module.urls_to_capture = ['http://www.wellsfargo.com/search/', 'http://www.google.com/']
    logs_by_url = capturing_module.capture_logs()
    print(logs_by_url['http://www.wellsfargo.com/search/']['console_logs'][0])
    

if __name__ == '__main__':
    main()





