import scrapy


class Toronto_spider(scrapy.Spider):
    name="toronto"
    start_urls=[
        "https://www.utoronto.ca/academics/programs-directory"
    ]
    def parse(self,response,**kwargs):
       all_courses=  response.css(".node-progam-of-study div.program-block")

       for course in all_courses:
           title=course.css("p.name::text").extract()
           degree=course.css("p.degrees::text").extract()
           options=course.css("p.options::text").extract()
           campus=course.css("p.campus::text").extract()
           
           yield {
               "title":title,
               "degree":degree[0].strip(),
               "option":options[0].strip(),
               "campus":campus[0].strip()
               }
       next_page_url= response.css("li.pager-next a::attr(href)").extract() 
       if next_page_url is not None:
            next_page_url= response.urljoin(next_page_url[0])
            yield scrapy.Request(next_page_url,callback=self.parse)