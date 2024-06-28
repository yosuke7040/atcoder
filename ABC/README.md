# 使い方

※ ABCディレクトリ直下でVSCodeを開いてください。

- 新規ディレクトリ作成

344をコンテスト名にしてください。

```bash
./make-dir.sh 344
```

- テストケース実行

対象のpythonファイルを開いて、command + shift + Bを押してください。

- 単純なテストしたい時

input.txtにテストケースを記載
対象のpythonファイルを開いて、F5を押してください。


- python仮想環境

環境zy

```bash
python3 -m venv venv-atcoder
source venv-atcoder/bin/activate

# pypy
curl -LO https://downloads.python.org/pypy/pypy3.10-v7.3.16-macos_arm64.tar.bz2
tar xf pypy3.10-v7.3.16-macos_arm64.tar.bz2
rm -rf pypy3.10-v7.3.16-macos_arm64.tar.bz2

pip3 install online-judge-tools
pip3 install atcoder-tools
 ```
