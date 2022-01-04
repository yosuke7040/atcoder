#!/bin/bash

problem_name=$1
# base_url=${problem_name%_*}
base_url="math-and-algorithm"
problem_full_name="math-and-algorithm_${problem_name:0:1}"
test_dir=test/${base_url}/${problem_name}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${test_dir} https://atcoder.jp/contests/${base_url}/tasks/${problem_full_name//-/_}
fi

oj test -c "python3 problems/${problem_name}.py" -d ${test_dir}