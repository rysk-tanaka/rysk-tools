# Markdown to Slack Converter

このツールは、Markdownファイルを読み取り、Slack記法に変換するPythonスクリプトです。

## 機能

- Markdownファイルを入力として受け取ります。
- 入力されたMarkdownをSlack記法に変換します。
- 変換された内容を指定された出力ディレクトリに保存します。

## インストール

1. このリポジトリをクローンするか、スクリプトをダウンロードします。

2. 必要なライブラリをインストールします：

   ```
   pip install -r requirements.txt
   ```

## 使用方法

コマンドラインから以下のように実行します：

```
python markdown_to_slack_converter.py <markdownファイルのパス> <出力ディレクトリ>
```

例：

```
python markdown_to_slack_converter.py example.md /path/to/output
```

### オプション

- `-h`, `--help`: ヘルプメッセージを表示します。
- `-v`, `--version`: バージョン情報を表示します。

## 出力

変換されたSlack記法のテキストは、指定された出力ディレクトリ内の`output.slack.txt`ファイルに保存されます。

## 注意事項

- 入力ファイルと出力ファイルはUTF-8エンコーディングを使用しています。
- 出力ディレクトリが存在しない場合は自動的に作成されますが、適切な権限が必要です。
