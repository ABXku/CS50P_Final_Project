import mock
import builtins
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from project import dict_func, prompt_and_check, prompt_sold_out

# Note that "test_dict_func" might not work if the website structure is updated
def test_dict_func():
    website = "https://www.1999.co.jp/eng/"
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
    categories = driver.find_elements(by="xpath", value="//div[@class='hd_genre2']/a")
    test_dict = {
        0: "PVC Figure",
        1: "Anime Robot/SFX",
        2: "Gundam Kit/etc.",
        3: "Military Model",
        4: "Model Car Kit",
        5: "Hobby Tool",
        6: "Model Train N",
        7: "Model Train HO/Z",
        8: "Diecast Car",
        9: "Anime Goods",
        10: "Fashion Doll",
        11: "Toy",
        12: "RC Model",
        13: "Diecast Airplane",
        14: "Trading Card",
        15: "Hobby Magazine",
        16: "R18+",
    }
    assert dict_func(categories) == test_dict

    # @PVC Figure page
    categories = driver.find_elements(
        by="xpath", value="//div[@class='left_list_waku']"
    )
    test_dict = {
        0: "Azur Lane",
        1: "Original Illustration",
        2: "Hololive",
        3: "Bocchi the Rock!",
        4: "Blue Archive",
        5: "Vocaloid",
        6: "KonoSuba: God`s Blessing on this Wonderful World!",
        7: "Fate",
        8: "Hunter x Hunter",
        9: "The Legend of Zelda",
        10: "Demon Slayer: Kimetsu no Yaiba",
        11: "Jujutsu Kaisen",
        12: "Puella Magi Madoka Magica",
        13: "Genshin Impact",
        14: "Neon Genesis Evangelion",
        15: "One Piece",
        16: "My Dress-Up Darling",
        17: "Honkai: Star Rail",
        18: "Yakuza",
        19: "Berserk",
        20: "Other Original List",
        21: "Nendoroid",
        22: "Pop Up Parade",
        23: "Nendoroid Doll",
        24: "figma",
        25: "Lookup",
        26: "Orange Rouge",
        27: "Artfx J",
        28: "KDcolle (Kadokawa Collection)",
        29: "B-style",
        30: "Other Item Series List",
        31: "Alter",
        32: "Alphamax",
        33: "A+",
        34: "Bandai",
        35: "BellFine",
        36: "B`full",
        37: "Broccoli",
        38: "Chara-Ani",
        39: "Daiki Kougyo",
        40: "Di Molto Bene",
        41: "Dragon Toy",
        42: "Flare",
        43: "Freeing",
        44: "FuRyu",
        45: "Good Smile Company",
        46: "Hanabatake to Bishojo",
        47: "Kaitendo",
        48: "Kaiyodo",
        49: "Kadokawa",
        50: "Kotobukiya",
        51: "Lechery",
        52: "Max Factory",
        53: "Medicom Toy",
        54: "Medicos Entertainment",
        55: "MegaHouse",
        56: "Okayama Figure",
        57: "Orca Toys",
        58: "Orchid Seed",
        59: "Phat Company",
        60: "Plum",
        61: "Ques Q",
        62: "Q-Six",
        63: "Sen-Ti-Nel",
        64: "SkyTube",
        65: "Square Enix",
        66: "Tomytec",
        67: "Union-Creative",
        68: "Tuberosa+",
        69: "Vertex",
        70: "Wave",
        71: "Wing",
        72: "Other (Completed)",
        73: "Other (Completed) 2",
        74: "Bishoujo Plastic Kit",
        75: "Clayz",
        76: "Other Figure Kits",
        77: "Character",
        78: "Other Shokugan",
        79: "Scale Action Figure Accessory",
        80: "Robot/SFX are here",
        81: "Fashion Doll are here",
        82: "Anime Goods are here",
        83: "Hobby Magazine are here",
        84: "Release Date List",
        85: "Manufacturer List",
        86: "Producer List",
        87: "Item series List",
        88: "Original List",
    }
    assert dict_func(categories) == test_dict


def test_prompt_and_check():
    test_list = [2, 4, 6, 8]
    msg = "Input number"
    with mock.patch.object(builtins, "input", lambda _: "2"):
        assert prompt_and_check(msg, test_list) == 2
    with mock.patch.object(builtins, "input", lambda _: "3"):
        with pytest.raises(SystemExit):
            prompt_and_check(msg, test_list)
    with mock.patch.object(builtins, "input", lambda _: "yes"):
        with pytest.raises(SystemExit):
            prompt_and_check(msg, test_list)


def test_prompt_sold_out():
    with mock.patch.object(builtins, "input", lambda _: "y"):
        assert prompt_sold_out() == "y"
    with mock.patch.object(builtins, "input", lambda _: "n"):
        assert prompt_sold_out() == "n"
