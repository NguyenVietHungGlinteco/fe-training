for article in response.css('article'):
	title = article.css('h3 a::text').get() or article.css('header a::text').get() or article.css('a::text').get()
	image_url = article.css('img ::attr(src)').get()
	description = article.css('div p::text').get()
	print(dict(title=title.strip(), image_url=image_url, description=description), '\n')