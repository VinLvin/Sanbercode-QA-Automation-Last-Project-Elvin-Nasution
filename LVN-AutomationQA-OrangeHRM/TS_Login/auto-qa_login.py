import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        # steps
        driver = self.driver #buka web driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        driver.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        expected_url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
        self.assertEqual(expected_url,driver.current_url)

    def test_a_failed_login_invalid_credentials(self):
        # steps
        driver = self.driver #buka web driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        driver.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("asdasd") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"spanMessage").text
        self.assertIn('Invalid credentials', response_data)

    def test_a_failed_login_empty_password(self):
        # steps
        driver = self.driver #buka web driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        driver.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"spanMessage").text
        self.assertIn('Password cannot be empty', response_data)

    def test_a_failed_login_empty_username(self):
        # steps
        driver = self.driver #buka web driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        driver.find_element(By.ID,"txtUsername").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"spanMessage").text
        self.assertIn('Username cannot be empty', response_data)

   
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
