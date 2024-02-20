#!/bin/bash

problem_name=$1
dir_name=$2
contest_name=$(basename ${dir_name})

base_url=${problem_name%_*}
test_dir=test/${base_url}/${problem_name}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${test_dir} https://atcoder.jp/contests/${contest_name}/tasks/${problem_name//-/_}
fi

oj test -c "python3 problems/${contest_name}/${problem_name}.py" -d ${test_dir}
