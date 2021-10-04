https://qiita.com/chokoryu/items/4b31ffb89dbc8cb86971

AtCoderというディレクトリを切ってそこに環境構築しています。
コンテストの問題は{コンテスト名}_{問題名}.pyというファイル名でproblemsディレクトリに全部突っ込みます。
ファイル名の{コンテスト名}部分は、AtCoderのコンテストページのURLと同じでないと動作しないので注意して下さい。
https://atcoder.jp/contests/{コンテスト名}
ファイル名例：
　AtCoder Beginner Contest 158のA問題
　(URL:https://atcoder.jp/contests/abc158/tasks/abc158_a)
　　→abc158_a.py
　日立製作所 社会システム事業部 プログラミングコンテスト2020のC問題
　(URL:https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_c)
　　→hitachi2020_c.py


デバッグしたい.pyファイルを開いている時にF5を押せば、input.txtの内容を入力として受け取って.pyファイルを実行します。


～.pyファイル開いてる状態で、Ctrl + Shift + Bを実行でテストケースやってくれる
ファイル名には注意
cptest.shは実行権限いるよ　chmod 777 cptest.sh

login
oj login https://atcoder.jp/
oj login --check https://atcoder.jp/


docker-compose exec dev /bin/bash