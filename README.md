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
cd /[プロジェクトを作成したいディレクトリ]　
scrapy startproject [プロジェクト名]　##任意のプロジェクト名
cd /[プロジェクト名]
```
　※パスの調整は各自でしてください。
#### 3.spider（取得するサイトや内容を記述する.pyファイル）の作成
##### ターミナル上
```
scrapy genspider [spiderのファイル名] [httpsなしのスクレイピング対象のURL]　##spiderは任意の名前
```
とします。今回は以下のとおりでは行いましょう。
```
scrapy genspider [spiderのファイル名] [httpsなしのスクレイピング対象のURL]　##spiderは任意の名前
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
　メモしていたxpathを使ってコードを記述していく。
　※今回はこのレポジトリ内の　にあるclassより下をコピーして自分の[spider名].pyのファイル内に貼り付けてください。
xpathで記述していますがCSSの場合は、
```
response.css['cssコード']
```
でも可能です。


#### 6.プロジェクト名のディレクトリにいることを確認


#### 7.スクレイピングを開始
##### ターミナル上
```
scrapy crawl [spider名] -o [出力したいファイル名].json
```
とします。今回は以下のとおりでは行いましょう。
```
scrapy crawl [spider名] -o [出力したいファイル名].json
```
※出力ファイルはjson,csv,xmlに設定できますので拡張子部分を修正してください。

### 完了

#### その他
-スクレイピングをしすぎるとサーバに負荷がかかって迷惑になるかもしれないため◎ページ目までを取得するコードにしています。
-次ページ設定コードのコメントアウトを解除すると全ページ分のデータが取得できます。
-スクロールはサーバに負荷がかかることがあるためサイトによっては禁止されています。
-スクロールの練習をするときは[Books to Scrape(練習サイト)](https://books.toscrape.com/index.html)で練習しましょう。

#### 参考
[xpathの記述方法](https://ai-inter1.com/xpath/)

[robots.txtとは？](https://wacul-ai.com/blog/seo/internal-seo/seo-robots-txt/)

[Books to Scrape(練習サイト)](https://books.toscrape.com/index.html)
