import scrapy
from scrapy_splash import SplashRequest

lua_script = """
function main(splash,args)
    assert(splash:go(args.url))

    local element = splash:select('body > div > div > main > section > button')
    element:mouse_click()
    
    splash:wait(splash.args.wait)  
    return splash:html()
end
"""


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["www.linkedin.com", "localhost"]

    def start_requests(self):
        yield SplashRequest(
            url="https://www.linkedin.com/jobs/search/?currentJobId=3965386759&geoId=106057199&keywords=data%20engineer&location=Brasil&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true",
            callback=self.parse,
            endpoint="execute",
            args={"wait": 2, "lua_source": lua_script},
        )

    def parse(self, response):
        vagas = response.css("div.base-card")

        for vaga in vagas:
            yield {"url": vaga.css("a.base-card__full-link").re(r"https:.*?\"")}
