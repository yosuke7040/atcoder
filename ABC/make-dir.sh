#!/bin/bash

set -eu

# 引数のチェック
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

# 変数の設定
number=$1
src_dir="problems/abc"
dest_dir="problems/abc$number"

# 雛形ディレクトリの存在確認
if [ ! -d "$src_dir" ]; then
    echo "Template directory $src_dir does not exist."
    exit 1
fi

# 新規ディレクトリの作成
mkdir -p "$dest_dir"

# ファイルのコピーとリネーム
for file in "$src_dir"/*; do
    base_name=$(basename "$file")
    cp "$file" "$dest_dir/${base_name/abc/abc$number}"
done

echo "Directory $dest_dir created with template files."
