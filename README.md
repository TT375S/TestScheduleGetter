# TestScheduleGetter
This program gets term examination schedules of my university from PDF files.

大学の、テストの行われる日時や教室を一覧表示するプログラムです。検索したい授業名は、course N@viのページのhtmlソースを入力することで一括で取得します。
ある一個の大学にしか使えません。  

__修正が終わりました。現在、普通に使えるようになりました！__

##内容
試験情報ページ<https://www.waseda.jp/fsci/students/exam/>　に、試験期間の2週間くらい前に試験情報pdfが公開されます。  
試験情報ページのhtmlから、リンクのURLを取得し、試験情報pdfファイルをダウンロードします。現在、理工学部にしか対応しておりません。  
pdfファイルはテキストファイルにxpdfの機能で変換され、そこから扱いやすく変換されます。  
ユーザーが、course N@viの科目画面のhtmlソースをコピペで標準入力に入れてくれれば、そのhtmlソースからどの科目を受講しているかを取得し、テストの日時や教室を先ほどのテキストファイルから検索して表示します。


##前提となるもの
####1. Python2系
そのまま...。
####2. Beautiful Soup4
Pythonのパッケージで、ウェブスクレイピングが簡単にできて便利。
`$ pip install beautifulsoup4`
でインストール。
####3. pdftotext
pdfをプレーンテキストに直してくれる便利なもの。
pdftotextが使えればなんでもいいです。
<http://labo.utsubo.tokyo/2016/05/09/pdftotextでpdfを文字列化/>
にて、macの場合のやり方が載っています。
その他のOSの場合は、検索してください...。とりあえず、  
1. pdftotextという名前で使えるようにしてある  
2. pdftotextを日本語に対応させてある  
状態であればOKです。

##実際に使ってみよう
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
そこでコピーしたhtmlソースを、ターミナルに貼り付けてCtrl+D(windowsではCtrl+Z)を押せばテストの一覧が表示されます。

###出力例
	-------授業名一覧です。-------
	*...テストのある授業
	-...テストのない授業

	* 回路理論Ｂ
	* コンピュータアーキテクチャＡ
	* Academic Reading 2　月５スロボッドニウ
	* 電子回路
	* 情報数学Ｂ
	* 通信理論
	* 信号処理Ｂ
	- Concept Building And Discussion 2　水５ダイヤー
	- 情報理工学実験Ａ
	* 社会調査データの分析
	* アルゴリズムとデータ構造Ｂ
	- インキュベーション推進室実施イベント
	- 学生生活について　15
	- キャリア・就職支援講座(2015年度入学者）
	- 2016年度　情報理工学科　進級学生
	- Course N@viを知ろう！ 15
	- 2016年度　コンピュータセキュリティセミナー（学部生向け）
	- 理工ITセミナー（日）
	- Science and engineering IT seminar(En)
	- 安全e-learningプログラム2016
	- ハラスメント防止
	- ダイバーシティ推進室提供講座
	- 留学ポートフォリオ
	- 防災e-learningプログラム
	- 早稲田小劇場どらま館

	-------テストスケジュール一覧--------

	２月３日（金） ３限 13：00～14：30 ２年 回路理論Ｂ 谷井 孝至 ５６－１０２
	２月１日（水） １限 9：00～10：30 ２年 コンピュータアーキテクチャＡ 笠原 博徳 ５６－１０４
	１月２４日（火） ４限 15：00～16：00 Academic Reading 2 月５スロボッドニウ スロボッドニウ アダ
	１月３１日（火） １限 9：00～10：30 ２年 電子回路 戸川 望 ５２－３０４
	１月３１日（火） ４限 15：00～16：30 ２年 情報数学Ｂ 石川 博 ５６－１０３
	２月１日（水） ３限 13：00～14：30 ２年 通信理論 前原 文明 ６３－２０２
	２月１日（水） ３限 13：00～14：30 ２年 信号処理Ｂ 畑 文雄 ６３－２０１
	１月２７日（金） ２限 11：00～12：00 社会調査データの分析 石倉 義博 ５２－１０１
	２月３日（金） １限 9：00～10：30 ２年 アルゴリズムとデータ構造Ｂ 清水 佳奈 ５２－３０４
