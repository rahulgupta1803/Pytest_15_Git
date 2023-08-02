from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class Test_01:
    x=10
    y=5

    # @pytest.mark.skipif(x>y,reason='Bugs in the test case')
    def test_sum_001(self):
        a=3
        b=7
        sum=a+b
        print(f'sum of a and b is {sum}')
        if sum==10:
            assert True
        else:
            assert False
    # @pytest.mark.skipif(x<y, reason='No need to run this test case')
    def test_credenceurl(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if (driver.title == "Credence"):
            print('you are at credence.in')
            driver.close()
            assert True
        else:
            print('you are at wrong url')
            driver.close()
            assert False

    # @pytest.mark.skipif(x>y, reason='it is taking too much time')
    def test_mul(self):
        a=3
        b=7
        sub=a*b
        print(f'multiplication of a from b is {sub}')
        if sub == 21:
            assert True
        else:
            assert False

    # @pytest.mark.skipif(x<y, reason='it is not important test case')
    def test_credkart_checkout(self):
        from selenium import webdriver

        import time
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        # 1 open browser
        browser = webdriver.Chrome(options=options)

        browser.maximize_window()

        # url opening
        browser.get('https://automation.credence.in/')

        # login
        browser.find_element(By.LINK_TEXT, 'Login').click()
        browser.find_element(By.XPATH, "//input[@id='email']").send_keys('Credencetest1989@test.com')
        browser.find_element(By.XPATH, "//input[@id='password']").send_keys('Credence@1234')
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # add cart for Apple macbook pro
        browser.find_element(By.XPATH, "//img[@src='https://automation.credence.in/img/macbook-pro.jpg']").click()
        browser.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        # continue shoping
        browser.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        # add cart apple ipad retina
        browser.find_element(By.XPATH, "//img[@src='https://automation.credence.in/img/ipad-retina.jpg']").click()
        browser.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        # continue shopping
        browser.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        # add cart headphones
        browser.find_element(By.XPATH, "//img[@src='https://automation.credence.in/img/headphones.jpg']").click()
        browser.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(2)
        # select quantity apple mac book pro
        product_quantity1 = Select(browser.find_element(By.XPATH, "//tbody//tr[1]//td[3]//select[@class='quantity']"))
        product_quantity1.select_by_index(3)
        time.sleep(2)
        # select quantity apple ipad retina
        product_quantity2 = Select(browser.find_element(By.XPATH, "//tbody//tr[2]//td[3]//select[@class='quantity']"))
        product_quantity2.select_by_index(2)
        time.sleep(2)
        # select quantity headphones
        product_quantity3 = Select(browser.find_element(By.XPATH, "//tbody//tr[3]//td[3]//select[@class='quantity']"))
        product_quantity3.select_by_index(4)
        time.sleep(2)
        # for check out
        browser.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        browser.find_element(By.XPATH, "//input[@id='first_name']").send_keys('Rahul')
        browser.find_element(By.XPATH, "//input[@id='last_name']").send_keys('Gupta')
        browser.find_element(By.XPATH, "//input[@id='phone']").send_keys('9548512379')
        browser.find_element(By.XPATH, "//textarea[@id='address']").send_keys('HD-169, Phase 3, Kabir nagar, Raipur, C.G')
        browser.find_element(By.XPATH, "//input[@id='zip']").send_keys('492099')
        state = Select(browser.find_element(By.XPATH, "//select[@id='state']"))
        state.select_by_index(1)

        # card details
        browser.find_element(By.XPATH, "//input[@name='owner']").send_keys('Rahul')
        browser.find_element(By.XPATH, "//input[@id='cvv']").send_keys('043')

        time.sleep(3)
        browser.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('5281')
        browser.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('0370')
        browser.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('4891')
        browser.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys('6168')
        time.sleep(3)
        year = Select(browser.find_element(By.XPATH, "//select[@id='exp_year']"))
        year.select_by_index(3)
        month = Select(browser.find_element(By.XPATH, "//select[@id='exp_month']"))
        month.select_by_index(4)

        # purchase confirmation
        browser.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
        time.sleep(6)
        try:
            browser.find_element(By.XPATH, "//h1[normalize-space()='Thank you.']")
            print("automation is completed")
            browser.close()
            assert True
        except:
            print("automation is failed")
            browser.close()
            assert False

    @pytest.mark.skip
    def test_orange_hrm_login(self):
        import time
        from selenium import webdriver
        from selenium.common import NoSuchElementException
        from selenium.webdriver.common.by import By

        from selenium.webdriver.support.select import Select

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        # login
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(5)

        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('Admin')
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')
        time.sleep(5)
        driver.find_element(By.XPATH,
                                '//div[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

        # log out
        time.sleep(6)
        driver.find_element(By.XPATH, '//div[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span').click()
        time.sleep(6)
        driver.find_element(By.XPATH,
                                '//div[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
        time.sleep(3)
        try:
             driver.find_element(By.XPATH, '//div[@id="app"]/div[1]/div/div[1]/div/div[1]/img')
             print('Automation of login and logout is successfully completed')
             driver.close()
             assert True
        except:
            print('Automation is failed')
            driver.close()
            assert False

    @pytest.mark.skip
    def test_shopclues_login_logout(self):
        import time
        from selenium import webdriver
        from selenium.webdriver.common.alert import Alert
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.shopclues.com/")

        # for login
        driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/button[1]").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Continue with Facebook']").click()
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys('rahul.ipe@gmail.com')
        driver.find_element(By.XPATH, "//input[@id='pass']").send_keys('rahul1803sarda@#$%')
        driver.find_element(By.XPATH, "//button[@id='loginbutton']").click()

        # for search item
        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/button[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys('harry potter')
        wait = WebDriverWait(driver,100)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='srch_action btn orange']"))).click()
        # driver.find_element(By.XPATH, "//a[@class='srch_action btn orange']").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@id='det_img_152622459']"))).click()
        # driver.find_element(By.XPATH, "//img[@id='det_img_152622459']").click()
        x = driver.window_handles
        driver.switch_to.window(x[1])
        driver.find_element(By.XPATH, "//button[@id='buy']").click()

        # proceed to payment
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='proceed_to_payment_button']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//label[@for='payment_option_3']").click()

        driver.close()

        driver.switch_to.window(x[0])

        # logout
        driver.find_element(By.XPATH, "//a[normalize-space()='Hi Rahul']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[normalize-space()='Sign Out']").click()

        try:
            driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")
            print('Automation is successfully completed')
            driver.close()
            assert True
        except:
            print('Automation is failed')
            driver.close()
            assert False



