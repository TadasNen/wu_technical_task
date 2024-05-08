from functions import launch_web, login, add_cart, checkout, contact_info, finish_buy, logout

# List of default usernames found in the website for easy access of different users. To change user navigate to
# login function below and change index number correlating to user.
username_list = ["standard_user",
                 "locked_out_user",
                 "problem_user",
                 "performance_glitch_user",
                 "error_user",
                 "visual_user",]


# List of items available for shopping. Can be taken out automatically using find_elements function of Selenium.
# However, to save time and test out specific choices of cart adding, it was left as a list. To change different
# shopping cart list, adjust the list.
#
item_id_list = ["add-to-cart-sauce-labs-backpack",
                "add-to-cart-sauce-labs-bike-light",
                "add-to-cart-sauce-labs-bolt-t-shirt",
                "add-to-cart-sauce-labs-fleece-jacket",
                "add-to-cart-sauce-labs-onesie",
                "add-to-cart-test.allthethings()-t-shirt-(red)"]

# Sequence of functions used to carry out user story as described in guidelines.
if __name__ == "__main__":
    """
    This part is used to lauch automation function is sequence.
    """
    driver = launch_web()
    login(username_list[0], driver)
    add_cart(item_id_list, driver)
    checkout(driver)
    contact_info(driver)
    finish_buy(driver)
    logout(driver)