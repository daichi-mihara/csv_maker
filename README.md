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

ここから先は、基本的に TODO と書かれたところを埋めていけばいいようにできています。

# prev_files

先方からいただいた実データファイルたちを、このフォルダに格納してください。

# main.py

以下のように打つと、company.csvができるようにします。

```bash
python3 main.py --company
```

この辺は好みですが、コマンド1つ打てば誰がやっても同じ結果が出るようにしておきましょう。

長くなるので割愛しますが、TODOと書かれているところを順に埋めていくと動くようになっているはずです！
