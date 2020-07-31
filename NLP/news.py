from KoreaNewsCrawler.articlecrawler import ArticleCrawler

Crawler = ArticleCrawler()  
Crawler.set_category("정치", "사회", "오피니언")  
Crawler.set_date_range(2016, 5, 2020,7)  
Crawler.start()