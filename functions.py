from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx
from datetime import datetime
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



def get_default_browser():
    """
    Function made to access Windows registry to find out default browser user uses. This has an impact in this scenario
    as it is not known what is default browser used in this scenario as usually large institutions have standartized
    approach. This fuction only works on Windows OS as well, for other OS, different code is required, in addition
    to identifying OS.
    :return: str: Default browser string
    """
    register_path = r'Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice'
    with OpenKey(HKEY_CURRENT_USER, register_path) as key:
        return str(QueryValueEx(key, "ProgId")[0])

def launch_web():
    """
    Based on default browser function different types of browser are used. Most of programming was done as Firefox
    default browser. If it's either Chrome or Firefox, it will launch driver in those browsers, otherwise Edge would
    be as a default browser due to populiarity in banks. Selenium has no option for Opera.
    :return: Specific webriver for browser
    """
    default_browser = get_default_browser()
    if 'Chrome' in default_browser:
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        return webdriver.Chrome(options=chr_options)
    elif 'Firefox' in default_browser:
        return webdriver.Firefox()
    else:
        return webdriver.Edge()

def login(username, driver):
    """
    Function finds specific fields in webpage to fill out username and password information which are used to login.
    Depending on the program requirements, this step may be paused for user to select specific account to use.
    :param username: Specific username for login into the site, list can be found above.
    :param driver: Driver variable found in main.py created after launch_web function is launched
    :return: Access website, fill out username and password and clicking login button
    """
    driver.get("https://www.saucedemo.com")
    element_user = driver.find_element(By.ID, "user-name")
    element_user.send_keys(f"{username}")
    element_psw = driver.find_element(By.ID, "password")
    element_psw.send_keys("secret_sauce")
    element_login_button = driver.find_element(By.ID, "login-button")
    element_login_button.click()


def add_cart(item_id_list, driver):
    """
    Function commands to press all 'Add to cart' buttons in website that are in the item_id_list and moves to cart
    page. Depending on requirements, this part should be left for user to input for them to select specific items.
    :param item_id_list: List of available items in list determined above.
    :param driver: Driver variable found in main.py created after launch_web function is launched
    :return: Clicks all relevant products to be added in cart. Products added ar contained in item_id_list variable
    """
    for el in item_id_list:
        element_find = driver.find_element(By.ID, el)
        element_find.click()
    driver.get("https://www.saucedemo.com/cart.html")

def checkout(driver):
    """
    Functions purpose is to move from Cart page to Checkout.
    :param driver: Driver variable found in main.py created after launch_web function is launched.
    :return: Moves to next process step webpage
    """
    element_checkout = driver.find_element(By.ID, "checkout")
    element_checkout.click()

def contact_info(driver):
    """
    This part could be either left for user to input, separate document like .xls containing relevant information
    or default values left depending on business needs. Contact info fields in this fuction are with default values.
    :param driver: Driver variable found in main.py created after launch_web function is launched.
    :return: Fills out contact information and moves to Checkout Overview page.
    """
    ele_first = driver.find_element(By.ID, "first-name")
    ele_first.send_keys("Tadas")
    ele_last = driver.find_element(By.ID, "last-name")
    ele_last.send_keys("Neniskis")
    ele_zip = driver.find_element(By.ID, "postal-code")
    ele_zip.send_keys("LT09238")
    ele_continue = driver.find_element(By.ID, "continue")
    ele_continue.click()

def finish_buy(driver):
    """
    Function creates .txt document with Payment method, Shipping Information and Total price, renames it to data and
    current date and time. Afterwards, purchase finishing button is pressed.
    :param driver: Driver variable found in main.py created after launch_web function is launched.
    :return: Completes purchase of the cart and creates .txt document with general purchase information
    """
    ele_info = driver.find_elements(By.XPATH, "//div[@class='summary_info_label']")
    ele_value = driver.find_elements(By.XPATH, "//div[@class='summary_value_label']")

    list_info = []
    list_value = []
    for ele in ele_info:
        list_info.append(ele.text)
    for ele in ele_value:
        list_value.append(ele.text)

    list = [ele for pair in zip(list_info, list_value) for ele in pair]

    ele_total = driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
    list.append(ele_total.text)

    dt = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    with open(f"data_{dt}.txt", "w") as f:
        for ele in list:
            f.write(ele + '\n')

    ele_finish = driver.find_element(By.ID, "finish")
    ele_finish.click()

def logout(driver):
    """
    Function presses side bar pop up button and presses logout button. Commented code part and imports related to it
    were used to wait for sidebar to popup so function could find logout button and press it, however it does not work
    as intended and due to time constraints implicit wait function is called instead. After logout, webpage is closed.
    :param driver: Driver variable found in main.py created after launch_web function is launched.
    :return: Logs out of the page and closes webpage
    """
    ele_bar = driver.find_element(By.ID, "react-burger-menu-btn")
    ele_bar.click()
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "logout_sidebar_link"))
    # )
    driver.implicitly_wait(1)
    ele_logout = driver.find_element(By.ID, "logout_sidebar_link")
    ele_logout.click()
    driver.quit()