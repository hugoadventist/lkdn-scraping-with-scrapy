import json


class JsonReader:

    # TODO: refatorar esses código para o usuário passar o caminho do arquivo json
    @staticmethod
    def read_json() -> list:
        with open(
            "/home/hugoriviere/projects/python/lkdn-scraping-with-scrapy/data/data.jsonl",
            "r",
            encoding="utf-8",
        ) as json_file:
            urls = []
            for url in json_file:
                input_url = json.loads(url)
                urls.append(input_url["url"][0])
            return urls
