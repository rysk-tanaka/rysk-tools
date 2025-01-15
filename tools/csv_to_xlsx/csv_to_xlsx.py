import pandas as pd
import argparse

def convert_csv_to_xlsx(input_file, output_file=None):
    # 出力ファイル名が指定されていない場合、入力ファイル名の拡張子をxlsxに変更
    if output_file is None:
        output_file = input_file.rsplit('.', 1)[0] + '.xlsx'

    # CSVファイルを読み込む
    df = pd.read_csv(input_file, encoding='utf-8')

    # Excelファイルとして保存
    df.to_excel(output_file, index=False)
    print(f"Converted {input_file} to {output_file}")

def main():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description='Convert CSV file to Excel file')
    parser.add_argument('input_file', help='Input CSV file path')
    parser.add_argument('-o', '--output', help='Output Excel file path (optional)')

    # 引数を解析
    args = parser.parse_args()

    # 変換実行
    convert_csv_to_xlsx(args.input_file, args.output)

if __name__ == '__main__':
    main()
