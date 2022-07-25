# AM-scrape

### [HAGAKURE-PROGRAMMING-ACADEMYのissue](https://github.com/HAGAKURE-PROGRAMMING-ACADEMY/KEIJIBAN/issues/20)にあがっている[AM（アイエム）](https://github.com/HAGAKURE-PROGRAMMING-ACADEMY/KEIJIBAN/issues/20)の情報をスクレイピングします。

今回はscrapyというスクレイピングのフレームワークを使って「博物館・美術館名」と「詳細URL」を一覧で取得します。
scrapyを使ってさくっとデータを取得してみます。
ターミナル（コマンドプロンプト）でscrapyのコマンドを実行しながら.pyファイルを設定していくためVSCodeやPyCharmで作業を行います。

#### 0.scrapyをインストール
```
pip install scrapy
```

#### 1.取得したいページやその内容をxpathやCSSでテキストメモなどで記録。
　※実際はここがメイン作業になりますが今回は省略します。

#### 2.プロジェクトの作成
##### ターミナル上
```
cd /[プロジェクトを作成したいディレクトリ]　
scrapy startproject [プロジェクト名]　##任意のプロジェクト名
cd /[プロジェクト名]
```
とします。今回は以下のとおりでは行いましょう。
```
cd /project
scrapy startproject museum_info
cd /museum_info
```
※パスの調整は各自でしてください。
#### 3.spider（取得するサイトや内容を記述する.pyファイル）の作成
##### ターミナル上
```
scrapy genspider [spiderのファイル名] [httpsなしのスクレイピング対象のURL]　##spiderは任意の名前
```
とします。今回は以下のとおりでは行いましょう。
```
scrapy genspider museum_overview www.museum.or.jp/museum
```
#### 4.作成したプロジェクトフォルダ内にあるsettig.pyの設定
##### settig.py
```
#スクレイピング可能か確認（デフォルトで設定済み）
ROBOTSTXT_OBEY = True
#スクレイピング間隔（秒）（コード内の上のあたりにコメントアウトされているので解除）
DOWNLOAD_DELAY = 3
#文字コードを指定（最後の行に追加）
FEED_EXPORT_ENCODING = 'utf-8'
```

#### 5.spiderフォルダ内の[spider名].pyの設定
##### [spider名].py
[設定したspiderのファイル名].pyを開く
allowed_domainsをドメイン名のみに設定
```
allowed_domains = ['www.museum.or.jp']
```
start_urlsはスクレイピング対象のURLで最後尾’/’を削除する。
```
start_urls = ['https://www.museum.or.jp/museum']
```
今回はなぜかサブディレクトリ（/museum）が設定されませんのでご注意ください。

メモしていたxpathを使ってコードを記述していく。
 
※今回はこのレポジトリ内のmuseum_overview.pyにあるdef parse(self, response)以下のコードをコピーして自分のファイルに貼り付けてください。

museum_overview.py
```
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
```

xpathで記述していますがCSSの場合は、
```
response.css['cssコード']
```
でも可能です。


#### 6.プロジェクト名のディレクトリにいることを確認


#### 7.スクレイピングを開始 csvで出力
##### ターミナル上
```
scrapy crawl [spider名] -o [出力したいファイル名].csv
```
とします。今回は以下のとおりでは行いましょう。
```
scrapy crawl  museum_overview -o test.csv
```
※出力ファイルはjson,csv,xmlに設定できますので拡張子部分を修正してください。

### 完了でーす。プロジェクトフォルダ内にcsvファイルが出力されています。

#### その他
- スクレイピングをしすぎるとサーバに負荷がかかって迷惑になるかもしれないため数ページだけを取得するコードにしています。
- 次ページ設定コードのコメントアウトを解除すると全ページ分のデータが取得できます。
- スクロールはサーバに負荷がかかることがあるためサイトによっては禁止されています。
- スクロールの練習をするときは[Books to Scrape(練習サイト)](https://books.toscrape.com/index.html)で練習しましょう。

#### 参考
[xpathの記述方法](https://ai-inter1.com/xpath/)

[robots.txtとは？](https://wacul-ai.com/blog/seo/internal-seo/seo-robots-txt/)

[Books to Scrape(練習サイト)](https://books.toscrape.com/index.html)
