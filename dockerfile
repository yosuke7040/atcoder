# 参考：https://qiita.com/hinamimi/items/b3dd159f956628cebdbb
# versionには注意
FROM ubuntu:20.04

# インタラクティモード避ける
ARG DEBIAN_FRONTEND=noninterractive
# タイムゾーンを日本に
ENV TZ=Asia/Tokyo

RUN apt-get update && \
    apt-get install -y zsh time tzdata tree git curl

RUN chsh -s /bin/zsh

RUN apt-get update && \
apt-get install -y python3.8 python3-pip pypy3 nodejs npm

# 一般的なコマンドで使えるように設定
# e.g. python3.8 main.py => python main.py
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 30 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 30 && \
    update-alternatives --install /usr/bin/pypy pypy /usr/bin/pypy3 30 && \
    update-alternatives --install /usr/bin/node node /usr/bin/nodejs 30

# AtCoderでも使えるPythonライブラリをインストール
RUN pip install numpy==1.18.2 && \
    pip install scipy==1.4.1 && \
    pip install scikit-learn==0.22.2.post1 && \
    pip install numba==0.48.0 && \
    pip install networkx==2.4

# コンテスト補助アプリケーションをインストール
RUN pip install online-judge-tools==11.3.0
RUN npm install -g atcoder-cli@2.1.1

# # atcoder-cliの設定
# RUN acc config-dir && \
#     acc config default-template python && \
#     acc config default-test-dirname-format test

# # # AHC用のRustのinstall
# RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
# ENV PATH $PATH:/home/root/.cargo/bin

WORKDIR /root/home