import scrapy
from bs4 import BeautifulSoup

class BlogSpider(scrapy.Spider):
    name = "narutoblog"
    start_urls=['https://naruto.fandom.com/wiki/Special:BrowseData/Jutsu?limit=250&offset=0&_cat=Jutsu']

    def parse(self,response):
        for href in response.css('.smw-columnlist-container')[0].css("a::attr(href)").extract():
            extracted_data= scrapy.Request("https://naruto.fandom.com/"+href,
                                           callback=self.parse_jutsu)
            
            yield extracted_data
        
        for next_page in response.css('a.mw-nextlink'):
            yield response.follow(next_page,self.parse)

    def parse_jutsu(self, response):
        jutsu_name=response.css("span.mw-page-title-main::text").extract()[0] # To get the name of the jutsu at the header of the page
        jutsu_name = jutsu_name.strip() # To remove any trailing whitespace

        div_selector=response.css("div.mw-parser-output")[0] # This would get the description of the Jutsu
        div_html = div_selector.extract()

        soup = BeautifulSoup(div_html).find('div')
        # Basically this loop inside the condition will look for the aside section in the html
        # and then iterate until it find the h3 with classification and 
        # extract the jutsu type in it as a key and value pair

        jutsu_type = ""
        if soup.find('aside'):
            aside= soup.find('aside')

            for cell in aside.find_all('div',{'class':'pi-data'}):
                if cell.find('h3'):
                    cell__name= cell.find('h3').text.strip()
                    if cell__name == "Classification":
                        jutsu_type = cell.find('div').text.strip()

        soup.find('aside').decompose()

        jutsu_description = soup.text.strip()
        jutsu_description = jutsu_description.split('Trivia')[0].strip()


        return dict(
            jutsu_name = jutsu_name,
            jutsu_type = jutsu_type,
            jutsu_description =  jutsu_description
        )

            
