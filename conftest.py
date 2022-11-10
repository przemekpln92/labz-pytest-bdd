import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def init_driver():
    web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield web_driver
    web_driver.close()


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    with open("stats.txt", 'w') as file:
        itm = session.perform_collect()
        file.write(str(session.testscollected) + " ")
        file.write(str(itm) + " ")
        file.write(str(session.testsfailed ) + " ")
        file.write(str(itm[0] ) + " ")
        file.write(str(itm[0].reportinfo() ) + " ")
        
        

def pytest_report_collectionfinish(config, start_path, startdir, items):
    with open("stats.txt", 'w') as file:
        file.write('Number of tests: ' + str(len(items)))

@pytest.hookimpl()
def pytest_report_from_serializable(config, data):
    with open("stats.txt", 'w') as file:
        for i in data.keys():
            file.write(i + " ")



    



