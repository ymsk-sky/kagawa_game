# kagawa_game
香川県ネット・ゲーム依存症対策条例（笑）に寄せられたパブリックコメント（笑）の解析を行いたい。

# docs
[ねとらぼ](https://nlab.itmedia.co.jp/nl/articles/2004/25/news026.html)で公開されているのでダウンロード。

# 環境
- macOS 10.14.6
- Python3.8

## パッケージ
### poppler

pdfファイルをpythonで操作できるようにする。

**インストール**

```
$ brew install poppler
```

### pdf2image

pdfファイルを画像(jpg, png)へ変換する。

**インストール**

```
$ pip install pdf2image
```

## 使い方

`docs`ディレクトリにDLした`pdf`ファイル群を配置する。

`pdf`を`png`画像に変換してから、OCRによってテキストへ起こす。

```
$ python convert_to_txt.py
```

画像は`imgs`配下に保存される。
