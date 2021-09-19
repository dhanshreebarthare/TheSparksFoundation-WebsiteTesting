import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Sparksfoundation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='.\\chromedriver.exe')

    #1 To check the Vision Statement
    def test_sparksfoundation_vision(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/about/vision-mission-and-values/")
        time.sleep(2)
        elem = driver.find_element_by_class_name("media-body")
        self.assertIsNotNone(elem)
        self.assertEqual(elem.text, "A world of enabled and connected little minds, building future.")

    #2 To check the Top Header
    def test_TopHeader(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        time.sleep(2)
        elem = driver.find_element_by_class_name("col-md-6.navbar-brand")
        self.assertIsNotNone(elem)

    #3 To check the presence of Copyright Section
    def test_CopyRight(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        driver.execute_script("window.scrollTo(0, 2500)")
        time.sleep(2)
        elem = driver.find_element_by_class_name("copyright-wthree")
        text = elem.text
        time.sleep(2)
        self.assertIsNotNone(elem)

    #4 To check KNOW MORE button on the landing page
    def test_knowmorebtn(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        time.sleep(2)
        btn = driver.find_element_by_partial_link_text("KNOW MORE")
        time.sleep(2)
        btn.click()
        self.assertIsNotNone(btn)

    #5 To check the presence of E-mail Address
    def test_EmailAddr(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/contact-us/")
        elem = driver.find_elements_by_class_name("col-xs-10")
        text = elem[-1].text
        self.assertEqual(text, "Contact\n(for Non-Internship/GRIP Queries Only)\n+65-8402-8590, info@thesparksfoundation.sg")

    #6 To check LEARN MORE button on upcoming workshops
    def test_LearnWorkshops(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        driver.find_element_by_link_text("Programs").click()
        time.sleep(2)
        driver.find_element_by_link_text("Workshops").click()
        time.sleep(2)
        btn = driver.find_element_by_partial_link_text("LEARN MORE")
        btn.click()
        time.sleep(3)
        self.assertIsNotNone(btn)

    #7 To check Expert Mentors page
    def test_ExpertMentors(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        driver.find_element_by_link_text("About Us").click()
        time.sleep(2)
        driver.find_element_by_link_text("Expert Mentors").click()
        elem = driver.find_element_by_class_name("wthree_banner_info_grid")
        self.assertEqual(elem.text, 'Page Not Yet Ready!\nWe are still building the website. If you think it is an error, please contact us at info@thesparksfoundation.sg')

    #8 To check LEARN MORE button about AI in Education
    def test_LearnMoreBtn(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        time.sleep(2)
        driver.find_element_by_partial_link_text("LINKS").click()
        time.sleep(2)
        driver.find_element_by_partial_link_text("AI in Education").click()
        time.sleep(3)
        btn = driver.find_element_by_partial_link_text("LEARN MORE")
        time.sleep(3)
        btn.click()
        self.assertIsNotNone(btn)

    #9 To check LinkedIn group link
    def test_linkedIn(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        time.sleep(3)
        driver.find_element_by_partial_link_text("Contact Us").click()
        time.sleep(2)
        btn = driver.find_element_by_partial_link_text("JOIN TSF NETWORK HERE")
        btn.click()
        time.sleep(2)
        self.assertIsNotNone(btn)

    #10 To check if logo exists
    def test_LogoExists(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        elem = driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*')
        elem.click()
        self.assertIsNotNone(elem)

    #11 To check Internships at Internshala
    def test_Internshala(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        elem = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[3]/ul/li/a")
        elem.click()
        time.sleep(3)
        self.assertIsNotNone(elem)

    #12 To check the Submission Form
    def test_Form_submit(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org/")
        driver.find_element_by_link_text('Join Us').click()
        time.sleep(2)
        driver.find_element_by_link_text('Why Join Us').click()
        time.sleep(2)
        driver.find_element_by_name('Name').send_keys('Dhanshree')
        time.sleep(2)
        driver.find_element_by_name('Email').send_keys('sample@email.com')
        select = Select(driver.find_element_by_class_name('form-control'))
        select.select_by_visible_text('Student')
        time.sleep(3)
        submit = driver.find_element_by_class_name('button-w3layouts')
        submit.click()
        time.sleep(2)
        self.assertIsNotNone(submit)

if __name__ == "__main__":
    unittest.main()
    Sparksfoundation().driver.close()
