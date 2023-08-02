import pytest
from selenium import webdriver


class Test_02:
    # @pytest.mark.xfail
    def test_Cred_kart_login(self):
        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        # 1 open browser
        browser = webdriver.Chrome(options=options)
        # 2 go to url
        browser.get('https://automation.credence.in/')

        # 3 click on register button
        username = 'test@credence.in'
        password='test@123'
        browser.find_element(By.LINK_TEXT,'Login').click()
        browser.find_element(By.NAME, 'email').send_keys(username)
        browser.find_element(By.ID, 'password').send_keys(password)
        browser.find_element(By.XPATH,'//button[@class="btn btn-primary"]').click()
        browser.find_element(By.LINK_TEXT,'Test User').click()
        time.sleep(3)
        browser.find_element(By.LINK_TEXT, 'Logout').click()

        try:
            browser.find_element(By.XPATH, '//h2[normalize-space()="CredKart"]')
            print('test case is passed')
            browser.close()
            assert True
        except:
            print('Test case is failed')
            browser.close()
            assert False


    def test_credkart_shopping(self):
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
        # price selection
        l = len(browser.find_elements(By.XPATH, "//tbody//tr//td[4]"))

        # Price verification
        p = []
        for x in range(1, l - 2):
            price = browser.find_element(By.XPATH, "//tbody//tr[" + str(x) + "]//td[4]").text
            product_price = (price[1:])
            p.append(float(product_price))
        print(p)

        expected_total = sum(p)
        print(f'Expected total: {expected_total}')

        v = []

        for x in range(l - 2, l + 1):
            amount = browser.find_element(By.XPATH, "//tbody//tr[" + str(x) + "]//td[4]").text
            amount1 = amount[1:].replace(",", "")
            v.append(amount1)
        print(v)

        if (expected_total == float(v[0])):
            print('subtotal is matched')
            browser.close()
            assert True
        else:
            print('subtotal is not matched')
            browser.close()
            assert False

    # @pytest.mark.skip
    def test_credenceurl(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if (driver.title == "Credence"):
            print('you are at credence.in')
            driver.close()
            assert True