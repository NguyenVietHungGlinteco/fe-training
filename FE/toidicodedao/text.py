for article in response.css('h3.title-news a::text').getall():
	# title = article.css('h3 a::text').get() or article.css('header a::text').get() or article.css('a::text').get()
	title = article
	print(dict(title=title))