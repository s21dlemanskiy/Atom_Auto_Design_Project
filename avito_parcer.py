from typing import Dict, Optional, List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions as selenium_exceptions
from bs4 import BeautifulSoup
import time
import pandas as pd
import os


class Parcer(object):
    driver = None

    def __init__(self, link: str):
        self.link = link
        self.reviews_links = []

    def __enter__(self):
        # Create a new instance of the Firefox driver
        self.__class__.driver = webdriver.Firefox()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__class__.driver.quit()

    def open_link(self, link: Optional[str]=None):
        if link is None:
            link = self.link
        self.driver.get(link)
        time.sleep(3)
        return

    def get_source_code(self) -> str:
        return self.driver.page_source

    def prepare_reviews_links(self) -> None:
        # Open the webpage
        self.driver.get(link)
        time.sleep(3)

        #expand all page
        while True:
            time.sleep(3)
            try:
                expand_button = self.driver.find_element(By.CLASS_NAME, "ListingPagination__moreButton")
            except selenium_exceptions.NoSuchElementException:
                break
            if expand_button.is_enabled():
                expand_button.click()
            else:
                break
        # parce links
        reviews_link_elem = self.driver.find_elements(by=By.CLASS_NAME, value="ReviewsList__item")
        for elem in reviews_link_elem:
            innerHTML = elem.get_attribute('innerHTML')
            soup = BeautifulSoup(innerHTML, "html.parser")
            self.reviews_links += [soup.find('a').get('href')]

    def set_link(self, link: str) -> None:
        self.link = link

    def parce_reviews(self) -> List[Dict[str, Optional[str]]]:
        result = []
        for lnk in self.reviews_links:
            self.open_link(lnk)
            page_soup = BeautifulSoup(self.get_source_code(), "html.parser")
            main_text, short_structured_description, user_info = None, None, None
            try:
                main_text = page_soup.find('div', class_="ReviewContent").text
                print(len(main_text))
            except Exception as e:
                print(e)
                print("skip main_text")
            try:
                user_info = str(page_soup.find('div', class_="Review__userInfo"))
            except Exception as e:
                print(e)
                print("skip user_info")
            try:
                short_structured_description = str(page_soup.find('div', class_="ReviewProsAndCons"))
            except Exception as e:
                print(e)
                print("skip short_structured_description")
            result += [{"main_text": main_text,
                        "short_structured_description": short_structured_description,
                        "user_info": user_info,
                        "link": lnk}]
        return result

"""
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DKIA%2Cmodel%3DK5%2Cgeneration%3D22462291&catalog_filter=mark%3DKIA%2Cmodel%3DK5%2Cgeneration%3D23757960&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DKIA%2Cmodel%3DSTINGER%2Cgeneration%3D22763163&catalog_filter=mark%3DKIA%2Cmodel%3DSTINGER%2Cgeneration%3D20895791&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DTOYOTA%2Cmodel%3DCOROLLA%2Cgeneration%3D21491371&catalog_filter=mark%3DTOYOTA%2Cmodel%3DCOROLLA%2Cgeneration%3D23804209&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DTOYOTA%2Cmodel%3DCAMRY%2Cgeneration%3D22813205&catalog_filter=mark%3DTOYOTA%2Cmodel%3DCAMRY%2Cgeneration%3D23894733&catalog_filter=mark%3DTOYOTA%2Cmodel%3DCAMRY%2Cgeneration%3D21110739&catalog_filter=mark%3DTOYOTA%2Cmodel%3DCAMRY%2Cgeneration%3D21015160&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DHONGQI%2Cmodel%3DH5%2Cgeneration%3D23411269&catalog_filter=mark%3DHONGQI%2Cmodel%3DH5%2Cgeneration%3D23411044&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DSKODA%2Cmodel%3DOCTAVIA%2Cgeneration%3D21713968&catalog_filter=mark%3DSKODA%2Cmodel%3DOCTAVIA%2Cgeneration%3D20898195&body_type={body}
https://auto.ru/reviews/cars/skoda/superb/21619712/body-{body.lower()}/?sort=relevance-exp1-desc&geo_id=213
https://auto.ru/reviews/cars/moscvich/6/23558378/?sort=relevance-exp1-desc&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DVOLKSWAGEN%2Cmodel%3DPASSAT_NA%2Cgeneration%3D23424602&catalog_filter=mark%3DVOLKSWAGEN%2Cmodel%3DPASSAT_NA%2Cgeneration%3D22664781&catalog_filter=mark%3DVOLKSWAGEN%2Cmodel%3DPASSAT_NA%2Cgeneration%3D23423828&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DHONDA%2Cmodel%3DACCORD%2Cgeneration%3D23114280&catalog_filter=mark%3DHONDA%2Cmodel%3DACCORD%2Cgeneration%3D23626040&catalog_filter=mark%3DHONDA%2Cmodel%3DACCORD%2Cgeneration%3D21121524&body_type={body}
https://auto.ru/reviews/cars/changan/lamore/23614518/?sort=relevance-exp1-desc&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DAUDI%2Cmodel%3DA3%2Cgeneration%3D21837610&catalog_filter=mark%3DAUDI%2Cmodel%3DA3%2Cgeneration%3D23902398&catalog_filter=mark%3DAUDI%2Cmodel%3DA3%2Cgeneration%3D20785010&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DGEELY%2Cmodel%3DPREFACE%2Cgeneration%3D23719562&catalog_filter=mark%3DGEELY%2Cmodel%3DPREFACE%2Cgeneration%3D23249968&body_type={body}
https://auto.ru/reviews/cars/all/?sort=relevance-exp1-desc&catalog_filter=mark%3DHYUNDAI%2Cmodel%3DELANTRA%2Cgeneration%3D23718151&catalog_filter=mark%3DHYUNDAI%2Cmodel%3DELANTRA%2Cgeneration%3D22660173&catalog_filter=mark%3DHYUNDAI%2Cmodel%3DELANTRA%2Cgeneration%3D21516782&body_type={body}
https://auto.ru/reviews/cars/mazda/6/21357560/body-{body.lower()}/?sort=relevance-exp1-desc
https://auto.ru/reviews/cars/jac/j7/22588707/body-{body.lower()}/?sort=relevance-exp1-desc&geo_id=213
https://auto.ru/reviews/cars/omoda/s5/23498627/?sort=relevance-exp1-desc&body_type={body}
https://auto.ru/reviews/cars/chery/arrizo_8/23548329/?sort=relevance-exp1-desc&body_type={body}


"""

for body in ["SEDAN", "LIFTBACK"]:
    link = f"""https://auto.ru/reviews/cars/changan/uni_v/23385592/body-{body.lower()}/?sort=relevance-exp1-desc&geo_id=213"""
    # body = "SEDAN"
    mark = "Changan"
    model = "UNI-V"

    with Parcer(link) as p:
        p.prepare_reviews_links()
        # p.reviews_links = p.reviews_links[0:2]
        # p.reviews_links = ["https://auto.ru/review/cars/kia/k5/22462291/2681706442459380889/"]
        result = p.parce_reviews()
        df = pd.DataFrame(result)
        df["source_link"] = link
        df["mark"] = mark
        df["model"] = model
        df["body"] = body
        output_path = 'data.csv'
        df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))


