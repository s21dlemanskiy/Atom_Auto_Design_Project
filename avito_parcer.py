from typing import Dict, Optional, List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions as selenium_exceptions
from bs4 import BeautifulSoup
import json
import time
import pandas as pd
import os

class ParcerInterface(object):
    driver = None

    def __init__(self, link: str):
        self.link = link

    def __enter__(self):
        # Create a new instance of the Firefox driver
        self.__class__.driver = webdriver.Firefox()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__class__.driver.quit()

    def open_link(self, link: Optional[str]=None, wait=None):
        if link is None:
            link = self.link
        self.__class__.driver.get(link)
        if wait is not None:
            time.sleep(wait)
        return

    def get_source_code(self) -> str:
        return self.__class__.driver.page_source



class ParcerAvtoru(ParcerInterface):
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
    def prepare_reviews_links(self) -> None:
        self.reviews_links = []
        # Open the webpage
        self.driver.get(self.link)
        time.sleep(3)

        # expand all page
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
            self.open_link(lnk, wait=3)
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


# for body in ["SEDAN", "LIFTBACK"]:
#     link = f"""https://auto.ru/reviews/cars/changan/uni_v/23385592/body-{body.lower()}/?sort=relevance-exp1-desc&geo_id=213"""
#     # body = "SEDAN"
#     mark = "Changan"
#     model = "UNI-V"
#
#     with ParcerAvtoru(link) as p:
#         p.prepare_reviews_links()
#         # p.reviews_links = p.reviews_links[0:2]
#         # p.reviews_links = ["https://auto.ru/review/cars/kia/k5/22462291/2681706442459380889/"]
#         result = p.parce_reviews()
#         df = pd.DataFrame(result)
#         df["source_link"] = link
#         df["mark"] = mark
#         df["model"] = model
#         df["body"] = body
#         output_path = 'data.csv'
#         df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))


class ParcerDrom(ParcerInterface):
    link_base = "https://www.drom.ru/reviews/{body}/{mark}/{model}/?year1={start_year}"
    cars = [['Kia', 'K5'],
             ['Kia', 'Stinger'],
             ['Toyota', 'Corolla'],
             ['Toyota', 'Camry'],
             ['Skoda', 'Octavia'],
             ['Skoda', 'Superb'],
             ['Volkswagen', 'Passat (North America and China)'],
             ['Honda', 'Accord'],
             ['Audi', 'A3'],
             ['Hyundai', 'Elantra'],
             ['Mazda', '6'],
             ['JAC', 'J7'],
             ['OMODA', 'S5'],
             ['Chery', 'Arrizo 8'],
             ['Changan', 'UNI-V']]
    # cars = [['Kia', 'K5']]
    def get_status(self):
        try:
            logs = self.__class__.driver.get_log('performance')
            for log in logs:
                if log['message']:
                    d = json.loads(log['message'])
                    try:
                        content_type = 'text/html' in d['message']['params']['response']['headers']['content-type']
                        response_received = d['message']['method'] == 'Network.responseReceived'
                        if content_type and response_received:
                            return d['message']['params']['response']['status']
                    except:
                        pass
        except:
            return 404

    def prepare_reviews_links(self, mark, model, body) -> None:
        self.reviews_links = []
        link = self.link_base.format(mark=mark.lower(), model=model.lower(), body=body, start_year=2018)
        print(f"prepare_reviews_links: link:{link}")
        self.open_link(link=link, wait=6)
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        reviews_selector = "body > div.b-wrapper > div.b-content.b-media-cont.b-media-cont_margin_huge >" \
                        " div.b-left-side > div > div.b-flex.b-flex_w_2-col-reviews.bm-reviews-2col >" \
                        " div:nth-child(1) >" \
                        " div.top-cars.b-random-group.b-random-group_margin_r-b-size-s-s.b-visited"
        try:
            reviews = soup.select_one(reviews_selector).find_all("a",
                                            attrs={
                                                "class":"b-info-block__cont b-info-block__cont_state_reviews"
                                            })
        except AttributeError as e:
            # if no results
            if self.get_status() == 404:
                print(f"car {mark} {model} {body}: there is no page ")
            else:
                print(f"car {mark} {model} {body}: has no reviews")
            return
        for elem in reviews:
            self.reviews_links += [elem.get('href')]

    def parce_review(self, link):
        print(f"parce_review: link:{link}")
        result = {  "main_text": None,
                    "car_characteristics": None,
                    "car_score": None,
                    "source_link": link}
        self.open_link(link, wait=3)
        review_selector = "#review_text > div:nth-child(1) > div"
        page_source = self.get_source_code()
        soup = BeautifulSoup(page_source, "html.parser")
        review_text = soup.find("div", attrs={'id':"review_text"})
        review_text = review_text.find("div", attrs={"itemprop":"reviewBody"})
        result["main_text"] = review_text.getText()
        css_characteristics_selector = "body > div.b-wrapper > div.b-content.b-media-cont.b-media-cont_margin_huge > " \
                       "div.b-left-side > div > div.b-flex.b-flex_align_left." \
                       "b-flex_w_2-spring.b-random-group.b-random-group_margin_r-size-s.b-media-cont.bm-flex-toCol" \
                       " > div:nth-child(2) > div:nth-child(1) > div"
        car_characteristics = soup.select(css_characteristics_selector)
        result["car_characteristics"] = str(car_characteristics)
        css_score_selector = "body > div.b-wrapper > div.b-content.b-media-cont.b-media-cont_margin_huge " \
                        "> div.b-left-side > div > div.b-flex.b-flex_align_left." \
                        "b-flex_w_2-spring.b-random-group.b-random-group_margin_r-size-s.b-media-cont.bm-flex-toCol" \
                        " > div:nth-child(2) > div:nth-child(2) > div"
        car_score = soup.select(css_score_selector)
        result["car_score"] = str(car_score)
        return result

    def parce_all_reviews(self, result_file="data2.csv"):
        results = []
        for mark, model in self.__class__.cars:
            for body in ["sedan", "hatchback"]:
                self.prepare_reviews_links(mark, model, body)
            #     for review_link in self.reviews_links:
            #         result = self.parce_review(review_link)
            #         result["mark"] = mark
            #         result["model"] = model
            #         result["body"] = body
            #         results.append(result)
            # if len(results) > 0:
            #     df = pd.DataFrame(results)
            #     df.to_csv(result_file, mode='a', header=not os.path.exists(result_file))
            #     results= []



"""prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/kia/k5/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/kia/k5/?year1=2018
car Kia K5 hatchback: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/kia/stinger/?year1=2018
car Kia Stinger sedan: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/kia/stinger/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/toyota/corolla/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/toyota/corolla/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/toyota/camry/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/toyota/camry/?year1=2018
car Toyota Camry hatchback: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/skoda/octavia/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/skoda/octavia/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/skoda/superb/?year1=2018
car Skoda Superb sedan: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/skoda/superb/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/volkswagen/passat (north america and china)/?year1=2018
car Volkswagen Passat (North America and China) sedan: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/volkswagen/passat (north america and china)/?year1=2018
car Volkswagen Passat (North America and China) hatchback: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/honda/accord/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/honda/accord/?year1=2018
car Honda Accord hatchback: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/audi/a3/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/audi/a3/?year1=2018
car Audi A3 hatchback: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/hyundai/elantra/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/hyundai/elantra/?year1=2018
car Hyundai Elantra hatchback: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/mazda/6/?year1=2018
car Mazda 6 sedan: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/mazda/6/?year1=2018
car Mazda 6 hatchback: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/jac/j7/?year1=2018
car JAC J7 sedan: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/jac/j7/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/omoda/s5/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/omoda/s5/?year1=2018
car OMODA S5 hatchback: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/chery/arrizo 8/?year1=2018
car Chery Arrizo 8 sedan: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/chery/arrizo 8/?year1=2018
car Chery Arrizo 8 hatchback: there is no page
prepare_reviews_links: link:https://www.drom.ru/reviews/sedan/changan/uni-v/?year1=2018
prepare_reviews_links: link:https://www.drom.ru/reviews/hatchback/changan/uni-v/?year1=2018
car Changan UNI-V hatchback: there is no page"""
# with ParcerDrom("https://www.drom.ru/") as p:
#     p.parce_all_reviews()




class ParcerAvito(ParcerInterface):
    def parce_allPages(self, link=None):
        if link is None:
            link = self.link
        blank_link = link + "?reviewsPage={page_num:n}"
        all_review_data = []
        page_num = 1
        while True:
            self.open_link(blank_link.format(page_num=page_num), wait=3)
            soup = BeautifulSoup(self.get_source_code(), "html.parser")
            # проверка что reviewsPage не outofrange
            css_no_review_selector = "#app > div > div.index-root-k1Ib4.index-responsive-aOpFS." \
                                     "index-page_default-_b5bD > div > div > div.styles-root-nr_ku > div > div > h2"
            if soup.select(css_no_review_selector):
                break
            css_table_selector = "#app > div > div.index-root-k1Ib4.index-responsive-aOpFS.index-page_default-_b5bD" \
                                 " > div > div > div.styles-root-nr_ku > div > div > div.ModelReviewsList-root-GzKMx"
            table = soup.select_one(css_table_selector)
            reviews = table.find_all("div", attrs={"data-marker":"model-review"})
            for review in reviews:
                review_data = {"Преимущества": None, "Недостатки": None, "Дополнительно": None, "source_code": review}
                review = review.find("div", attrs={"class": "ReviewBody-textSections-MM3ON"})
                # plus = review.find("span", attrs={"data-marker" : "model-review/text-section/text"})
                # minus = review.find("span", attrs={"data-marker" : "model-review/text-section/title"})
                # "model-review/text-section/text"
                # print(review.getText())
                for chld in review.children:
                    title = chld.find("span", attrs={"data-marker":"model-review/text-section/title"}).getText()
                    text = chld.find("span", attrs={"data-marker":"model-review/text-section/text"}).getText()
                    review_data[title] = text
                all_review_data += [review_data]
                # direct_kids = list(review.children)
                # print(len(review.find_all("div")))
            page_num += 1
        return all_review_data



# avito_link = "https://www.avito.ru/all/avtomobili?f=ASgCAQECA0Dgtg2UypgotJkonpkouJkospgo3pcoopsx5pgowJgo4rYN1LqoKKCxKLCiKNSgKISsKMCxKPSPM8Cg3BH0nSjgnSiwmzHYnCjw3D2m_xEk4oeLA_SHiwMBRfqMFBd7ImZyb20iOjIwMTgsInRvIjpudWxsfQ"
#
# avito_link2 = "https://www.avito.ru/otzyvy_vladelcev/auto/"


links = {('Kia', 'K5'): ['https://www.avito.ru/otzyvy_vladelcev/auto/kia/k5/iii/sedan-ASgBAgICBUTgtg3KmCjitg26qCjmtg3Ktyjqtg209DfQvA7Mk4sD',
                         'https://www.avito.ru/otzyvy_vladelcev/auto/kia/k5/ii/sedan-ASgBAgICBUTgtg3KmCjitg26qCjmtg3Ktyjqtg3a_SjQvA7Mk4sD'],
        ('Kia', 'Stinger'): ['https://www.avito.ru/otzyvy_vladelcev/auto/kia/stinger/liftback-ASgBAgICBETgtg3KmCjitg2gsSjmtg2I4q4Q0LwOzJOLAw'],
        ('Toyota', 'Corolla'): ['https://www.avito.ru/otzyvy_vladelcev/auto/toyota/corolla/xi_restayling/sedan-ASgBAgICBUTgtg20mSjitg2woijmtg3Ktyjqtg3Q~SjQvA7Mk4sD',
                                'https://www.avito.ru/otzyvy_vladelcev/auto/toyota/corolla/xii/sedan-ASgBAgICBUTgtg20mSjitg2woijmtg3Ktyjqtg2k8THQvA7Mk4sD'],
        ('Toyota', 'Camry'): ['https://www.avito.ru/otzyvy_vladelcev/auto/toyota/camry/xv70_restayling/sedan-ASgBAgICBUTgtg20mSjitg3UoCjmtg3Ktyjqtg2sr1vQvA7Mk4sD',
                              'https://www.avito.ru/otzyvy_vladelcev/auto/toyota/camry/xv70/sedan-ASgBAgICBUTgtg20mSjitg3UoCjmtg3Ktyjqtg2S~yjQvA7Mk4sD'],
        ('Skoda', 'Octavia'): ['https://www.avito.ru/otzyvy_vladelcev/auto/skoda/octavia/iv/liftback-ASgBAgICBUTgtg2emSjitg2ErCjmtg2I4q4Q6rYNoOU50LwOzJOLAw',
                               'https://www.avito.ru/otzyvy_vladelcev/auto/skoda/octavia/iii_restayling/liftback-ASgBAgICBUTgtg2emSjitg2ErCjmtg2I4q4Q6rYNqOko0LwOzJOLAw'],
        ('Skoda', 'Superb'): ['https://www.avito.ru/otzyvy_vladelcev/auto/skoda/superb/iii_restayling/liftback-ASgBAgICBUTgtg2emSjitg3AsSjmtg2I4q4Q6rYN1ok00LwOzJOLAw',
                              ],
        ('Volkswagen', 'Passat'): ['https://www.avito.ru/otzyvy_vladelcev/auto/volkswagen/passat/b8_restayling/sedan-ASgBAgICBUTgtg24mSjitg3SrCjmtg3Ktyjqtg2asTXQvA7Mk4sD'],
        ('Honda', 'Accord'): ['https://www.avito.ru/otzyvy_vladelcev/auto/honda/accord/x_restayling/sedan-ASgBAgICBUTgtg2ymCjitg30nSjmtg3Ktyjqtg2U7dsC0LwOzJOLAw',
                              'https://www.avito.ru/otzyvy_vladelcev/auto/honda/accord/x/sedan-ASgBAgICBUTgtg2ymCjitg30nSjmtg3Ktyjqtg3grTXQvA7Mk4sD'],
        ('Audi', 'A3'): ['https://www.avito.ru/otzyvy_vladelcev/auto/audi/a3/8v_restayling/sedan-ASgBAgICBUTgtg3elyjitg3gnSjmtg3Ktyjqtg3KxSjQvA7Mk4sD'],
        ('Hyundai', 'Elantra'): ['https://www.avito.ru/otzyvy_vladelcev/auto/hyundai/elantra/vii_restayling_2023_2023/sedan/benzin-ASgBAgICBkTgtg2imzHitg2wmzHmtg3Ktyjqtg221~0R7LYN3rco0LwOzJOLAw',
                                 'https://www.avito.ru/otzyvy_vladelcev/auto/hyundai/elantra/vii_2020_2022/sedan/benzin-ASgBAgICBkTgtg2imzHitg2wmzHmtg3Ktyjqtg2OgKQQ7LYN3rco0LwOzJOLAw',
                                 'https://www.avito.ru/otzyvy_vladelcev/auto/hyundai/elantra/vii_restayling_2023_2023/sedan/benzin-ASgBAgICBkTgtg2imzHitg2wmzHmtg3Ktyjqtg221~0R7LYN3rco0LwOzJOLAw'],
        ('Mazda', '6'): ['https://www.avito.ru/otzyvy_vladelcev/auto/mazda/6/gj_restayling_2/sedan-ASgBAgICBUTgtg3mmCjitg3YnCjmtg3Ktyjqtg367SjQvA7Mk4sD'],
        ('JAC', 'J7'): ['https://www.avito.ru/otzyvy_vladelcev/auto/jac/j7/i/liftback/benzin-ASgBAgICBkTgtg3AmCjitg3w3D3mtg2I4q4Q6rYN3tw97LYN3rco0LwOzJOLAw'],
        ('OMODA', 'S5'): ['https://www.avito.ru/otzyvy_vladelcev/auto/omoda/s5/i_2022_2023/sedan/benzin-ASgBAgICBkTgtg30_sMQ4rYN7oTaEea2Dcq3KOq2DfCE2hHstg3etyjQvA7Mk4sD'],
        ('Chery', 'Arrizo 8'): ['https://www.avito.ru/otzyvy_vladelcev/auto/chery/arrizo_8/i_2022_2023/sedan/benzin-ASgBAgICBkTgtg30lyjitg38sdoR5rYNyrco6rYN_rHaEey2Dd63KNC8DsyTiwM'],
        ('Changan', 'UNI-V'): ['https://www.avito.ru/otzyvy_vladelcev/auto/changan/uni-v/i_2022_2022/liftback-ASgBAgICBUTgtg3wlyjitg2E6~8Q5rYNiOKuEOq2DYrr7xDQvA7Mk4sD']}



for (mark, model), links_to_parce in links.items():
    print(mark, model)
    for lnk in links_to_parce:
        print(lnk)
        with ParcerAvito(lnk) as p:
            while True:
                try:
                    result = pd.DataFrame(p.parce_allPages())
                    break
                except Exception as e:
                    print(e)
                input("continue?")
            result["mark"] = mark
            result["model"] = model
            result["link"] = lnk
            result = result.reindex(sorted(result.columns), axis=1)
            result.to_csv("data3.csv", mode='a', header=not os.path.exists("data3.csv"))

