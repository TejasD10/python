from selenium import webdriver


def main():
    driver = webdriver.Firefox(executable_path=r'C:\Users\TDesai\git\python\Pyresources\geckodriver.exe')
    driver.get('https://rally1.rallydev.com/slm/login.op')
    assert 'CA Agile' in driver.title
    uname = driver.find_element_by_id('j_username')
    pwd = driver.find_element_by_id('j_password')
    submit = driver.find_element_by_id('login-button')
    uname.send_keys('tdesai@activehealth.net')
    pwd.send_keys('Welcome@1090')
    submit.click()
    

if __name__ == '__main__':
    main()