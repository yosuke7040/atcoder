#!/bin/bash

# 現在のスクリプトのディレクトリを取得
SCRIPT_DIR=$(dirname "$0")

# 仮想環境をアクティブにする
source "${SCRIPT_DIR}/venv-compe/bin/activate"
# source /Users/yyyy/src/compe/atcoder/ABC/venv-compe/bin/activate

problem_name=$1
base_url=${problem_name%_*}
test_dir=test/${base_url}/${problem_name}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${test_dir} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

# oj test -c "python3 problems/${base_url}/${problem_name}.py" -d ${test_dir}
oj test -c "/Users/yyyy/src/compe/atcoder/ABC/pypy3.10-v7.3.16-macos_arm64/bin/pypy3 problems/${base_url}/${problem_name}.py" -d ${test_dir}
