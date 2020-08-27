from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

timeout=20

def yt_driver():
    options = webdriver.ChromeOptions()
    options.headless = True  # if headeless parameter is set to true - the chrome browser will not appear in foreground
    options.add_argument('start-maximized')  # Start the chrome maximised
    options.add_argument('disable-infobars')  # Disable infobars
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # chrome_options.add_argument("--headless")
    #chrome_options.headless = True  # if headeless parameter is set to true - the chrome browser will not appear in foreground
    #chrome_options.add_argument('start-maximized')  # Start the chrome maximised
    #chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("disable-infobars")  # Disable infobars
    # chrome_options.add_argument('--incognito')
    #chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #chrome_options.add_experimental_option('useAutomationExtension', False)
    #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
    return driver

def getViews(driver,keyword):
    # url
    url = f"https://www.youtube.com/results?search_query=" + keyword
    # get the url
    driver.get(url)
    # wait for some time
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="video-title"]'))).click()
             # result=driver.find_element_by_xpath('//*[@id="count"]/yt-view-count-renderer/span[1]').text.strip('vues').encode('unicode-escape')
    result=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="count"]/yt-view-count-renderer/span[1]'))).text.strip(' views')


    return result

def check_isrc(driver,isrc):
    url = "https://isrcsearch.ifpi.org/#!/search?isrcCode={}&tab=lookup&showReleases=0&start=0&number=10".format(isrc)
    driver.get(url)
    time.sleep(1)
    try:
      text_isrc=driver.find_element_by_xpath('//*[@id="results"]/table/tbody/tr/td[7]').text
      print(text_isrc.lower())
      if text_isrc.lower()==isrc.lower():
        return 'yes'
    except:  # in case of failure
        pass
    return 'no'