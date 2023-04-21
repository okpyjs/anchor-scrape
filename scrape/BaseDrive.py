from itertools import count
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.chrome.service import Service as CService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options as FOptions
from selenium.webdriver.firefox.service import Service as FService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Driver:
    header = """user-agent=Mozilla/5.0 (X11; Linux x86_64)
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"""

    def get(self):
        pass

    def performClick(self):
        pass

    def performSendKyes(self, pathType, path, value):
        pass

    def maximize_window(self):
        pass

    def get_cookies(self):
        pass


class ChromeDriver(Driver):
    def __init__(self, head = True) -> None:
        options = COptions()
        if not head:
            options.add_argument("--headless")
        # options.add_argument("--window-size=800,5000")
        options.add_argument("--no-sandbox")
        options.add_argument(Driver.header)
        options.add_argument("--disable-dev-shm-usage")
        options.add_extension("static/extension/extension_5_4_0_0.crx")
        self.driver = webdriver.Chrome(
            service=CService(ChromeDriverManager().install()), options=options
        )
        self.driver.maximize_window()

    def get(self, _url):
        self.driver.get(_url)

    def performClick(self, pathType, path, num=10):
        count_flag = 0
        while True:
            try:
                for i in range(num):
                    # try:
                        self.driver.execute_script(f"window.scrollTo(0,{i * 500})")
                        _btn = self.driver.find_element(pathType, path)
                        _btn.click()
                        return True
                #     except:  # noqa
                #         continue
                # return False
            except:
                time.sleep(1)
            if count_flag > num:
                return False
            count_flag += 1


    def performSendKyes(self, pathType, path, value, num=10):
        for i in range(num):
            try:
                self.driver.execute_script(f"window.scrollTo(0,{i * 300})")
                _input = self.driver.find_element(pathType, path)
                _input.send_keys(value)
                return True
            except:  # noqa
                continue
        return False

    def maximize_window(self):
        self.driver.maximize_window()

    def get_cookies(self):
        return self.driver.get_cookies()

    def getSoup(self):
        return BeautifulSoup(self.driver.page_source, features="html.parser")

    def close(self):
        self.driver.close()

    def hover(self, pathType, path, num=10):
        for i in range(num):
            try:
                act = ActionChains(self.driver)
                _btn = self.driver.find_element(pathType, path)
                act.move_to_element(_btn).perform()
                return True
            except:  # noqa
                pass
            time.sleep(1)
        return False


class FirefoxDriver(Driver):
    def __init__(self, head = True) -> None:
        options = FOptions()
        if not head:
            options.add_argument("--headless")
        # options.add_argument("--window-size=800,5000")
        options.add_argument("--no-sandbox")
        options.add_argument(Driver.header)
        # options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        # options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(
            service=FService(GeckoDriverManager().install()), options=options
        )


class BaseDrive:
    """
    return: Chrome or Firefox Driver
    input: `C` or `F`
        if input is `C`, return Chrome Driver
        if input is `F`, return Firefox Driver
    """

    def __init__(self, driverType="C") -> None:
        self.driverTpye = driverType
        if self.driverTpye == "C":
            self.driver = ChromeDriver()
        elif self.driverTpye == "F":
            self.driver = FirefoxDriver()
