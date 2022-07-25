import scrapy

class MuseumOverviewSpider(scrapy.Spider):
    name = 'museum_overview'
    allowed_domains = ['www.museum.or.jp'] #ホームページドメイン名に修正（サブディレクトリを削除）
    start_urls = ['https://www.museum.or.jp/museum'] #検索したいページのURL 最後尾の'/'を削除
    
    def parse(self, response):
        #最後のページ数を取得
        
        #取得要素の設定
        infos = response.xpath(' //div[@class="c-museumItem_content_row_name c-clampLines is-clampline3"]')
        for info in infos:
            title = self.get_title(info.xpath('./text()').get())
            url = self.get_url(info.xpath('./parent::a/@href').get())
            yield{
                'title':title,
                'url':url
            }
            
        #次ページへリンクテスト用

        #最後のページ数を超えるまで次のページへ移動してスクレイプ
            last_pages = response.xpath('//button[@class="v-pagination__item"]/text()')
            last_page = str(last_pages[-1])
            last_page = (int(last_page[-5:-2]))
            #print(last_page)
            i = 2
            for t in range(5): #last_page 全ページの取得をしません。
                t = i + t
                if last_page >= t:       
                    next_page = f'https://www.museum.or.jp/museum?page={t}'
                    yield response.follow(url=next_page, callback=self.parse)
        
    #/nや空白を削除      
    def get_title(self,title):
        if title:
            return title.replace('\n','').replace(' ','')
        return 0
    
    def get_url(self,url):
        if url:
            url = 'https://www.museum.or.jp/' + url
            return url
        return 0    