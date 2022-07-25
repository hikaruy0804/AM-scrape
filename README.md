# AM-scrape

### [HAGAKURE-PROGRAMMING-ACADEMYのissue](https://github.com/HAGAKURE-PROGRAMMING-ACADEMY/KEIJIBAN/issues/20)にあがっている[AM（アイエム）](https://github.com/HAGAKURE-PROGRAMMING-ACADEMY/KEIJIBAN/issues/20)の情報をスクレイピングします。

今回は、scrapyというスクレイピングのフレームワークを使って"博物館名、美術館名"と"詳細URL"を一覧で取得します。
scrapyを使ってデータが簡単に取れることを体感します。

#### 0.scrapyをインストール
```
pip install scrapy
```

#### 1.取得したいページやその内容をxpathやCSSでメモ。
　※実際はここがメイン作業になりますが今回は省略します。

#### 2.プロジェクトの作成

#### 3.spider（取得するサイトや内容を記述する.pyファイル）の作成

#### 4.settig.pyの設定

　完了したら保存

#### 5.spider内の[spider名].pyの設定
　※今回はレポジトリ内の　classより下をコピペしてください。

　完了したら保存

今回はXpathで記載しますが、CSSの場合は、
```
response.css['cssコード']
```
でも可能です。


#### 6.コマンドプロンプトでプロジェクト名のディレクトリにいることを確認


#### 7.スクレイピングを開始
jsonの場合 拡張子はjson,csv,xmlに設定できます。
```
scrapy crawl [museum_scrap] -o [出力したいファイル名].json
```

#### 8.その他
あまりスクレイピングをしすぎるとサーバに負荷がかかって迷惑になるかもしれないため◎ページ目までを取得するコードにしています。
次ページ設定コードのコメントアウトを解除すると全ページ分のデータが取得できます。
スクロールはサーバに負荷がかかることがあるためサイトによっては禁止されています。
スクロールの練習をするときは[Books to Scrape(練習サイト)](https://books.toscrape.com/index.html)で練習しましょう。

#### 9.参考
[xpathの記述方法](https://ai-inter1.com/xpath/)

[robots.txtとは？](https://wacul-ai.com/blog/seo/internal-seo/seo-robots-txt/)

[Books to Scrape(練習サイト)](https://books.toscrape.com/index.html)
