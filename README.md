# TestScheduleGetter
This program gets term examination schedules of my university from PDF files.

大学の、テストの行われる日時や教室を一覧表示するプログラムです。検索したい授業名は、course N@viのページのhtmlソースを入力することで一括で取得します。
ある一個の大学にしか使えません。  

__現在、そのままでは実行できません。近日中に修正します。__  
どうしても使う必要がある場合、最初のコミットなら実行できます。

##内容
試験情報ページ<https://www.waseda.jp/fsci/students/exam/>　に、試験期間の2週間くらい前に試験情報pdfが公開されます。  
試験情報ページのhtmlから、リンクのURLを取得し、試験情報pdfファイルをダウンロードします。現在、理工学部にしか対応しておりません。  
pdfファイルはテキストファイルにxpdfの機能で変換され、そこから扱いやすく変換されます。  
ユーザーが、course N@viの科目画面のhtmlソースをコピペで標準入力に入れてくれれば、そのhtmlソースからどの科目を受講しているかを取得し、テストの日時や教室を先ほどのテキストファイルから検索して表示します。

##使い方
###前提となるもの
####Python2系
そのまま...。
####Beautiful Soup4
Pythonのパッケージで、ウェブスクレイピングが簡単にできて便利。
`$ pip install beautifulsoup4`
でインストール。
####pdftotext
pdfをプレーンテキストに直してくれる便利なもの。
pdftotextが使えればなんでもいいです。
<http://labo.utsubo.tokyo/2016/05/09/pdftotextでpdfを文字列化/>
にて、macの場合のやり方が載っています。
その他のOSの場合は、検索してください...。とりあえず、  
1. pdftotextという名前で使えるようにしてある  
2. pdftotextを日本語に対応させてある  
状態であればOKです。

###実際に使ってみよう
適当なフォルダで、  
`$ git clone https://github.com/TT375S/TestScheduleGetter.git`  
とやってクローンしてください。  
次に、ファイルのあるフォルダまで移動します。  
`$ cd TestScheduleGetter/files`  
そこで、
`$ python EXEC.py`  
とやると実行されます。  
  
するとhtmlソースの入力待ちになるので、次にcourse N@viにログインしてください。  
ログインしたら、htmlソースを表示させ、コピーしてください。(この辺は　ブラウザ名+ソース表示　で検索！)  
そこでコピーしたhtmlソースを、ターミナルに貼り付けてEnterを押せばテストの一覧が表示されます。


