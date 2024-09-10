import argparse
import os
from pathlib import Path
import commonmarkslack


def setup_argparse():
    parser = argparse.ArgumentParser(description="Markdown を Slack 記法に変換するツール")
    parser.add_argument("input_file", type=str, help="入力 Markdown ファイルのパス")
    parser.add_argument("output_dir", type=str, help="出力ディレクトリのパス")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    return parser


def convert_markdown_to_slack(input_file, output_dir):
    # ファイルを読み込む
    with open(input_file, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # Markdown をパースし、Slack記法に変換する
    parser = commonmarkslack.Parser()
    ast = parser.parse(markdown_content)
    renderer = commonmarkslack.SlackRenderer()
    slack_content = renderer.render(ast)

    # 出力ディレクトリが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)

    # 出力ファイルパスを生成
    output_file = Path(output_dir) / "output.slack.txt"

    # 変換された内容を新しいファイルに書き込む
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(slack_content)

    print(f"変換が完了しました。出力ファイル: {output_file}")


def main():
    parser = setup_argparse()
    args = parser.parse_args()

    input_file = Path(args.input_file)
    output_dir = args.output_dir

    if not input_file.exists():
        print(f"エラー: ファイル '{input_file}' が見つかりません。")
        return

    convert_markdown_to_slack(input_file, output_dir)


if __name__ == "__main__":
    main()
