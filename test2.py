import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Crm_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_crm(self):
           user = "instructor"
           pwd = "instructor1a"
           driver = self.driver
           driver.maximize_window()
           driver.get("http://127.0.0.1:8000/admin")
           elem = driver.find_element_by_id("id_username")
           elem.send_keys(user)
           elem = driver.find_element_by_id("id_password")
           elem.send_keys(pwd)
           elem.send_keys(Keys.RETURN)
           time.sleep(3)
           assert "Posted Blog Entry"
           driver.get("http://127.0.0.1:8000")
           time.sleep(1)
           #Goes to the investment
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a").click()
           time.sleep(1)
           #Clicks add stock button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
           time.sleep(1)
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/div/select/option[2]").click()
           time.sleep(1)
           elem = driver.find_element_by_id("id_symbol")
           elem.send_keys("ALL")
           elem = driver.find_element_by_id("id_name")
           elem.send_keys("sharetest")
           elem = driver.find_element_by_id("id_shares")
           elem.send_keys("300")
           elem = driver.find_element_by_id("id_purchase_price")
           elem.send_keys("100")
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
           time.sleep(2)
           # Clicks edit button
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[7]/td[7]/a").click()
           time.sleep(2)
           elem = driver.find_element_by_id("id_name")
           # edits the address
           elem.send_keys("exmapleedittest")
           elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
           # deletes the investment
           elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[7]/td[8]/a").click()






