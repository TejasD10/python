from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def main(uname=None, password=None):
    """
    This program is intended to open the cognizant timesheet application and submit the
    time sheet
    """
    try:
        driver = webdriver.Firefox(executable_path=r'C:\Users\TDesai\git\python\Pyresources\geckodriver.exe'\
                                   , proxy=r"http://webproxy.ahm.corp:9119/ahm.pac")
        driver.get(r'https://peoplesoft.cognizant.com/')
        # get username and password fields
        # username = WebDriverWait(driver=driver, timeout=5000).until(EC.presence_of_element_located((By.ID, 'username')))
        username = WebDriverWait(driver=driver, timeout=5000).until(EC.visibility_of_element_located((By.ID
                                                                                                      , 'username')))
        pwd = WebDriverWait(driver=driver, timeout=3000).until(EC.presence_of_element_located((By.ID, 'PasswordInternal')))
        assert username is not None
        assert pwd is not None
        username.clear()
        pwd.clear()

        username.send_keys(uname)
        pwd.send_keys(password)

        # Get login button
        loginbutton = driver.find_element_by_id('Log_On1')
        loginbutton.click()
        esalink = WebDriverWait(driver=driver, timeout=100).until(EC.visibility_of_element_located(
            (By.XPATH, r"//a[@href='https://compass.esa.cognizant.com/psp/ESA89PRD/?languagecd=ENG&cmd=start']")))
        esa = esalink.get_attribute("href")
        driver.get(esa)
        timesheetelem = WebDriverWait(driver=driver, timeout=100).until(EC.visibility_of_element_located((By.LINK_TEXT, "Timesheet")))
        # driver.find_element_by_xpath(r"//a[@href='https://compass.esa.cognizant.com/psp/ESA89PRD/EMPLOYEE/ERP/c/ADMINISTER_EXPENSE_FUNCTIONS.CTS_TS_LAND_COMP.GBL?PORTALPARAM_PTCNAV=CTS_TS_LANDING_PG&EOPP.SCNode=ERP&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=ADMN_ASSOCIATE_HOMEPAGE&EOPP.SCLabel=AssociateHomepage&EOPP.SCPTcname=&FolderPath=PORTAL_ROOT_OBJECT.PORTAL_BASE_DATA.CO_NAVIGATION_COLLECTIONS.ADMN_ASSOCIATE_HOMEPAGE.ADMN_S201709121531301683857506&IsFolder=false']")
        timesheethref = timesheetelem.get_attribute('href')
        driver.get(timesheethref)

        # We now have the timesheet landing page opened, we should now be selecting the timesheet and filling it in.
        tsweeklink = WebDriverWait(driver=driver, timeout=100).until(EC.presence_of_element_located((By.ID, "CTS_TS_LAND_PER_DESCR30$0")))
        driver.get(tsweeklink.get_attribute('href'))

        assert tsweeklink is not None
        # We are now at the timesheet page, go ahead submit

    except Exception as e:
        print(e)
        raise
    finally:
        driver.close()


if __name__ == '__main__':
    main(uname='430663', password='Purvi@1090')