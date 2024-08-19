for article in response.css('article'):
	title = article.css('h3 a::text').get() or article.css('header a::text').get() or article.css('a::text').get()
	print(dict(title=title.strip()))
	

from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://vnexpress.net/',
    ]

    def parse(self, response):
        for article in response.css('article'):
            yield {
                "title" : self.get_title(article),
                "image_url" : self.get_image_url(article),
                "description" : article.css('div p::text').get(),
            }

    def get_image_url(self, article_element):
        try:
            image_url = article_element.css('img ::attr(src)').get() or article_element.css('video source ::attr(src)').get()
            if not image_url:
                return "not image_url"
            is_https_url = image_url.startswith('https://')
            if not is_https_url:
                # return "not is_https_url"
                image_url = article_element.css('img ::attr(data-src)').get()
            return image_url
        except Exception as e:
            return f"Error get url: {e}"
        
    def get_title(self, article_element):
        try:
            title_element = article_element.css('h3') \
                or article_element.css('header') or article_element.css('a')

            title = title_element.css('a::text').get() \
                or title_element.css('::text').get()
            return title.strip()
        except Exception as e:
            return f"Error get url: {e}"