# from pathlib import Path
import scrapy
from ..services.json_load import JsonReader
import re

json_file = JsonReader()


class UrlsToLinkedinSpider(scrapy.Spider):
    name = "urls_to_linkedin"
    allowed_domains = ["www.linkedin.com", "br.linkedin.com"]

    def start_requests(self):
        urls = json_file.read_json()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-1].split("?")[0]
        # filename = f"{self.name}-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")
        yield {
            "id": re.search(r"\b\d+\b", response.url)[0],
            "title": response.css("title").xpath("string()").get(),
            "requirements:": response.css(".show-more-less-html__markup")
            .xpath("string()")
            .getall(),
        }
