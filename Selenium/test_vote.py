import unittest
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random

from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/usernamelogin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("prof")
        elem.send_keys(Keys.RETURN)
        driver.find_element_by_class_name("btn").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_password"))
        )
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("prof")
        elem.send_keys(Keys.RETURN)
        driver.find_element_by_class_name("btn").click()
        driver.get("http://127.0.0.1:8000/professor/pedagogical/skill/156/")
        elem = driver.find_element_by_id("big30")
        driver.execute_script("window.scrollTo(0, "+ str(elem.location["y"]-200) +")")
        elem.click()

        elem = driver.find_element_by_id("profavg")
        old_avg = elem.text

        driver.find_element_by_id("questionnaire").click()
        quest = driver.find_element_by_id("questions")
        quest_list = quest.find_elements_by_class_name("lead")
        commentField = quest.find_element_by_id("comment")
        old_comment = commentField.text
        print(old_comment)
        commentField.clear()
        commentField.send_keys(str(datetime.datetime.now()))
        for e in quest_list:
            star_elem = e.find_elements_by_tag_name("li")
            if float(old_avg[:-1]) > 50.0:
                i = random.randint(0, 2)
            else:
                i = random.randint(3, 4)
            print(i)
            count = 0
            for star in star_elem:
                if count == i:
                    star.click()
                count += 1
        elem = driver.find_element_by_id("buttonSubmit")
        driver.execute_script("window.scrollTo(0, " + str(elem.location["y"]-200) + ")")
        elem.click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()

        driver.refresh()
        elem = driver.find_element_by_id("big30")
        driver.execute_script("window.scrollTo(0, " + str(elem.location["y"] - 200) + ")")
        elem.click()

        elem = driver.find_element_by_id("profavg")
        new_avg = elem.text

        driver.find_element_by_id("questionnaire").click()
        quest = driver.find_element_by_id("questions")
        commentField = quest.find_element_by_id("comment")
        new_comment = commentField.text

        print(new_comment)
        assert old_comment != new_comment

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
