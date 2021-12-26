import requests
from bs4 import BeautifulSoup
import json
news_dict = {}


def get_first_news(n):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    url = 'https://sochisirius.ru/news/page/' + str(n)
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    article_cards = soup.find_all('a', class_='preview-teaser__list-item fullimage')

    for article in article_cards:
        article_title = article.find('p').text.strip()
        article_url = f'https://sochisirius.ru{article.get("href")}'

        article_id = article_url.split('/')[-1]     # https://sochisirius.ru/news/4968


        # print(f"{article_title} | {article_url}")

        news_dict[article_id] = {
            'article_title': article_title,
            'article_url': article_url
        }

    with open('news_dict.json', 'w') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)


def check_news_update():
    with open('news_dict.json') as file:
        news_dict = json.load(file)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

    url = 'https://sochisirius.ru/news/page/1'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    article_cards = soup.find_all('a', class_='preview-teaser__list-item fullimage')

    fresh_news = {}
    for article in article_cards:
        article_url = f'https://sochisirius.ru{article.get("href")}'
        article_id = article_url.split('/')[-1]

        if article_id in news_dict:
            continue
        else:
            article_title = article.find('p').text.strip()
            news_dict[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }

            fresh_news[article_id] = {
                'article_title': article_title,
                'article_url': article_url
            }
    with open('news_dict.json', 'w') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return fresh_news


def main():
    for i in range(1, 49):
        print(i)
        get_first_news(i)
    # check_news_update()


if __name__ == '__main__':
    main()