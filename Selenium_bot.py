"""
A simple selenium test example written by python
"""
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
class Bot:
    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--lang=en")
        self.times_restarted = 0  # keep track of how many times profile page has to be refreshed
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(20)

    def tear_down(self):
        """Stop web driver"""
        self.driver.quit()

    def go_to_page(self, url):
        """Find and click top-right button"""
        try:
            self.driver.get(url)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def login(self, username, password):
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(.,'Not Now')]").click()
        notNow = self.driver.find_element_by_class_name("HoLwm")
        time.sleep(3)
        notNow.click()
        time.sleep(5)
    
    def get_image_URL(self,wordList):
        URL="https://www.instagram.com/explore/tags/"+wordList[0]
        self.go_to_page(URL)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        r = requests.get(URL, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        links_with_text = []
        for a in soup.findAll('a',href=True, attrs={'class':'v1Nh3 kIKUG _bz0w'}):
            if a.text: 
                links_with_text.append(a['href'])
            
            
