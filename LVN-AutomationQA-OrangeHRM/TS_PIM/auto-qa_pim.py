from os import name
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class TestPim(unittest.TestCase):
    
    #Note!!! Wajib ganti username setiap melakukan sekali test
    firstname = "Kevin Test 2"
    lastname = "Nasution"
    username = "aavintest2"
    password = "admin123"

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_add_employee(self):
        #inisiasi variable
       
        driver = self.driver #buka web driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        driver.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        #Line Code Navigasi ke Menu Employee List
        b_pim = driver.find_element(By.ID, "menu_pim_viewPimModule")
        b_view_e = driver.find_element(By.ID,"menu_pim_viewEmployeeList")
     

        a = ActionChains(driver)
        a.move_to_element(b_pim).perform()
        a.click(b_view_e).perform()
        time.sleep(1)

        driver.find_element(By.ID,"btnAdd").click() # klik tombol add
        time.sleep(1)
        driver.find_element(By.ID,"firstName").send_keys(TestPim.firstname)
        time.sleep(1)
        driver.find_element(By.ID,"lastName").send_keys(TestPim.lastname)
        time.sleep(1)
        

        driver.find_element(By.ID,"btnSave").click() # klik tombol save
        time.sleep(1)

        #validasi
        response_firstname = driver.find_element(By.ID,'personal_txtEmpFirstName').get_attribute('value')
        response_lastname = driver.find_element(By.ID,'personal_txtEmpLastName').get_attribute('value')
        
        self.assertEqual(TestPim.firstname, response_firstname)
        self.assertEqual(TestPim.lastname, response_lastname)

    def test_delete_employee (self):
       
        driver = self.driver #buka web driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(2)
        driver.find_element(By.ID,"txtUsername").send_keys("admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        #Line Code Navigasi ke Menu Employee List
        b_pim = driver.find_element(By.ID, "menu_pim_viewPimModule")
        b_view_e = driver.find_element(By.ID,"menu_pim_viewEmployeeList")
     
        a = ActionChains(driver)
        a.move_to_element(b_pim).perform()
        a.click(b_view_e).perform()
        time.sleep(1)


        driver.find_element(By.ID,"empsearch_employee_name_empName").send_keys(TestPim.firstname)
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(1)
        driver.find_element(By.NAME,"chkSelectRow[]").click()
        time.sleep(1)
        driver.find_element(By.ID,"btnDelete").click()
        time.sleep(1)
        
        #Tombol OK
        driver.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(1)

        #validasi
        response_message = driver.find_element(By.TAG_NAME,'body').text
        self.assertIn('Successfully Deleted', response_message)    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()