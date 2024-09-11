# 環境構築

Poetryで筆者と環境を揃えておきます。

再現性を確保するの大事です。

```bash
# poetryをインストールする(すでに入っていたらこのコマンドは打たなくてもok)
curl -sSL https://install.python-poetry.org | python3 -

# poetry.lockをつくって、筆者と同じ環境が完成する
poetry install

# 環境に入る
poetry shell
```

ここから先は、基本的に TODO と書かれたところを埋めていけばいいようにできています。VSCodeだと左側のバーに虫眼鏡マークの検索ボタンがあって、そこから「TODO」で検索すると変更する箇所の一覧が出てくるはずです。

# prev_files

先方からいただいた実データファイルたちを、このフォルダに格納してください。

# const.py

ここにカラム名のマッピングやSFAでの型(日付型や数値型など)を記入します。

具体例も書いてあるので、それに沿って記述して下さい。

# main.py

以下のように打つと、company.csvができるようにします。

```bash
python3 main.py --company
```

この辺は好みですが、コマンド1つ打てば誰がやっても同じ結果が出るようにしておきましょう。

TODOと書かれているところを順に埋めていくと動くようになっているはずです！
