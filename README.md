# AM-scrape

### [HAGAKURE-PROGRAMMING-ACADEMYのissue](https://github.com/HAGAKURE-PROGRAMMING-ACADEMY/KEIJIBAN/issues/20)にあがっている[AM（アイエム）](https://github.com/HAGAKURE-PROGRAMMING-ACADEMY/KEIJIBAN/issues/20)の情報をスクレイピングします。

今回はscrapyというスクレイピングのフレームワークを使って"博物館名、美術館名"と"詳細URL"を一覧で取得します。
scrapyを使ってデータが簡単に取れることを体感します。
コマンドプロンプト（ターミナル）でscrapyのコマンドを実行して起動するためVSCODEやPYCHARMで作業をいます。

#### 0.scrapyをインストール
```
pip install scrapy
```

#### 1.取得したいページやその内容をxpathやCSSでメモ。
　※実際はここがメイン作業になりますが今回は省略します。

#### 2.プロジェクトの作成
'''
cd /[プロジェクトを作成したいディレクトリ]　
scrapy startproject [プロジェクト名]　##任意のプロジェクト名
cd /[プロジェクト名]
'''

#### 3.spider（取得するサイトや内容を記述する.pyファイル）の作成
'''
scrapy genspider [spiderのファイル名] [httpsなしのスクレイピング対象のURL]　##spiderは任意の名前
'''

#### 4.settig.pyの設定
'''
ROBOTSTXT_OBEY = True #スクレイピング可能か確認（デフォルトで設定済み）
DOWNLOAD_DELAY = 3　#スクレイピング間隔（秒）（コード内の上のあたりにコメントアウトされているので解除）
FEED_EXPORT_ENCODING = 'utf-8'　#文字コードを指定utf-16が良い場合も（最後の行に追加）
'''
　完了したら保存

#### 5.spider内の[spider名].pyの設定
　※今回はこのレポジトリ内の　にある　classより下をコピーして自分のspider.pyのファイル内に貼り付けてください。
　完了したら保存
今回はXpathで記載しますが、CSSの場合は、
```
response.css['cssコード']
```
でも可能です。


#### 6.コマンドプロンプトでプロジェクト名のディレクトリにいることを確認


#### 7.スクレイピングを開始
```
scrapy crawl [museum_scrap] -o [出力したいファイル名].json
```
※ファイルはjson,csv,xmlに設定できますので拡張子部分を修正してください。

### 完了

#### その他
あまりスクレイピングをしすぎるとサーバに負荷がかかって迷惑になるかもしれないため◎ページ目までを取得するコードにしています。
次ページ設定コードのコメントアウトを解除すると全ページ分のデータが取得できます。
スクロールはサーバに負荷がかかることがあるためサイトによっては禁止されています。
スクロールの練習をするときは[Books to Scrape(練習サイト)](https://books.toscrape.com/index.html)で練習しましょう。

#### 参考
[xpathの記述方法](https://ai-inter1.com/xpath/)

[robots.txtとは？](https://wacul-ai.com/blog/seo/internal-seo/seo-robots-txt/)

[Books to Scrape(練習サイト)](https://books.toscrape.com/index.html)
