import scrapy


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["www.linkedin.com"]
    start_urls = [
        f"https://www.linkedin.com/jobs/search/?currentJobId=3965386759&geoId=106057199&keywords=data%20engineer&location=Brasil&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
    ]

    def parse(self, response):
        vagas = response.css("div.base-card")

        for vaga in vagas:
            yield {"url": vaga.css("a.base-card__full-link").re(r"https:.*?\"")}
