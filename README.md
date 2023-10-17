# Web Scraping : Hobby Search
<p align="center">
  <img src="https://www.wattmann.co.jp/business/images/logo_hobbysearch.png" />
</p>

## Description
        After finishing all the problem sets, another thing to do in order to complete this course is to implement a final project using Python. Please check [Final Project](https://cs50.harvard.edu/python/2022/project/) out for more information about the requirements.

        Basically, this project is all about web scraping using the Selenium framework. Selenium is an open-source automation tool, and since I'm interested in automation testing, this may be a good opportunity to dive into this topic. By collecting the data from the website, we can use that data and process it in our own way. First, the program will go to the website, collect the lists of categories, and ask the user what type of thing we want to buy. Similarly, we will be prompted for sub-categories and then ask for user input again. After that, we need to tell the program whether we want to see the products that are already sold out or not, and then give them the range of budgets we have. At the end, what we have at our disposal is the CSV file containing the stuff we might be interested in, which includes the names of the products, the price, and a link to the product.

#### Video Demo: https://youtu.be/8lWi6BM7Tmk

> **Note**
        Note that this code is not going to work since you have to have your own Selenium driver on your computer, and you also have to set it to your own path. Moreover, if the website structure has changed, this code may not work as well.

## Project Structure
 - `project.py:` Main project code.
 - `test_project.py:` Unit tests for the code.

## Libraries
 - [Selenium](https://selenium-python.readthedocs.io)
 - [Pandas](https://pandas.pydata.org)
 - [Mock](https://docs.python.org/3/library/unittest.mock.html)
 - [Builtins](https://docs.python.org/3/library/builtins.html)
 - [Pytest](https://docs.pytest.org/en/7.4.x/)

## :bulb: Tip:
       If you want to do something like this, this [video](https://youtu.be/PXMJ6FS7llk?feature=shared) from FreeCodeCamp might be a very useful guideline.

## :warning: Disclaimer:
  All of the works here are for educational purposes only and are not intended to be submitted as your own code. Please check [Academic Honesty](https://cs50.harvard.edu/python/2022/honesty/) out for more detailed information.