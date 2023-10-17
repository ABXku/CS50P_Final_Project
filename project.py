from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
import sys


def main():
    website = "https://www.1999.co.jp/eng/"
    #You need to change this to your own path
    path = "/Users/cindyz/Applications/chromedriver-mac-x64/chromedriver"

    # Turn on headless_mode
    options = Options()
    options.add_argument("--headless=new")

    # Default Service instance
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to a page given by the URL
    driver.get(website)

    # @Homepage
    try:
        categories = driver.find_elements(
            by="xpath", value="//div[@class='hd_genre2']/a"
        )
    except:
        sys.exit("Website Error!")
    dict = dict_func(categories)

    # Prompt user for category and return selected choice
    user_choice = prompt_and_check("Choose the category", dict)

    # @Chosen category page
    sub_categories = driver.find_element(
        by="xpath", value=f"//div[@class='hd_genre2']/a[text()='{dict[user_choice]}']"
    )
    sub_categories.click()
    product = driver.find_elements(by="xpath", value="//div[@class='left_list_waku']")
    dict = dict_func(product)

    # Prompt user for sub-category and return selected choice
    user_choice = prompt_and_check("Choose the sub-category", dict)

    # @Chosen sub-category page
    bla = driver.find_element(
        by="xpath",
        value=f"//div[@class='left_list_waku'][text()='{dict[user_choice]}']",
    )
    bla.click()

    # Sort from low price to high price
    lowest_button = driver.find_element(
        by="xpath", value="//span[@class='list_hyouji05']/a[text()='Lowest']"
    )
    lowest_button.click()

    # Exclude Sold Out
    exclude = prompt_sold_out()
    if exclude == "y":
        exclude_button = driver.find_element(
            by="xpath", value=f"//div[@class='list_hyouji02']/a"
        )
        exclude_button.click()

    names = []
    prices = []
    links = []

    # Get the range of user's budget
    min = int(input("Minimum budget(in Yen): "))
    max = int(input("Maximum budget(in Yen): "))

    # Iterate through each page and append data in lists
    i = 1
    while True:
        products = driver.find_elements(
            by="xpath", value="//div[@class='pnlItem2']/div[@class='DataArea']"
        )
        for product in products:
            name = product.find_element(by="xpath", value="./table").text
            price = product.find_element(
                by="xpath",
                value="./div[@class='ContentArea list9pt TextLeft']/div/span[@class='ListPrice']",
            ).text
            link = product.find_element(by="xpath", value=".//a").get_attribute("href")
            price_compare = int(price.split()[0].replace(",", ""))
            if min <= price_compare <= max:
                names.append(name)
                prices.append(price)
                links.append(link)
            elif price_compare < max:
                break
        try:
            i += 1
            page = driver.find_element(
                by="xpath", value=f"//span[@class='list_kensu07']/a[text()='{i}']"
            )
            page.click()
        except:
            break

    # Create two-dimensional data structure and convert it into csv file
    product_data = {"name": names, "price": prices, "link": links}
    df_product = pd.DataFrame(product_data)
    df_product.to_csv("your_toy.csv")

    # Close the driver
    driver.quit()


# Create dictionary object and print all keys and values
def dict_func(elements):
    dict = {}
    i = 0
    for element in elements:
        dict[i] = element.text
        i += 1
    for key, value in dict.items():
        print(f"{value} : [{key}]")
        print("----------------------------------------------")
    return dict


# Prompt user for choice and check the input from user
def prompt_and_check(msg, dict):
    try:
        user_choice = int(input(f"{msg} : "))
        print("**********************************************")
        if user_choice in dict:
            return user_choice
        else:
            sys.exit("Invalid Input! Please type only number")
    except ValueError:
        sys.exit("Invalid Input! Please type only number")


# Prompt user for exclude/include sold out products and check the input from user
def prompt_sold_out():
    while True:
        try:
            exclude = input("Exclude Sold Out? (y/n) : ")
            if exclude == "y" or exclude == "n":
                return exclude
            else:
                print("Only 'y' and 'n'")
        except:
            print("Only 'y' and 'n'")


if __name__ == "__main__":
    main()
