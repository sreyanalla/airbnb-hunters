import scrapy

#ALTER YOUR START URL WITH THE SEARCH LOCATION FROM YOUR ANALYSIS

class SinglePageSpider(scrapy.Spider):
    name = "single_page_spider"
    start_urls = ["https://www.homes.com/bronx-ny/westchester-square-academy-school/s-nx8q16jsygcwk/"]

    def parse(self, response):
        placard_containers = response.css("article.search-placard")
        for container in placard_containers:
            description = container.css(".property-name::text").get()
            price = container.css("p.price-container::text").get()
            url = container.css("a::attr(href)").get()

            yield {
                "Property Address": description.strip() if description else None,
                "Asking Price": price.strip() if price else None,
                "Website URL": response.urljoin(url) if url else None,
            }

## RUN THIS CODE IN TERMINAL WITHIN YOUR SCRAPY FOLDER: scrapy crawl single_page_spider -o output.json
## THIS WILL OUTPUT YOUR INFO INTO A JSON FILE FOR REFERENCE







