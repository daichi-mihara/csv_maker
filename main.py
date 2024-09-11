import argparse
import pandas as pd
from utils import convert_date_str, convert_datetime_str, split_csv, get_df
from const import MAPPING_03, MAPPING_04, TYPE_DICT_03, TYPE_DICT_04


# NOTE: 関数がたくさんあってごちゃつくなら、フォルダ・ファイルに分けてしまって全然okです。
# また、この関数はあくまで一例です。必要に応じて変更してください。
def make_company_csv() -> None:
    # 先方のファイルを読み取ってDataFrameに変換
    print("🐈 データの読み込み start")
    df1 = get_df("prev_files/03_顧客連携ワーク.csv")
    df2 = get_df("prev_files/04_顧客連携ワーク.csv")

    # カラム名を変換
    print("🐈 カラム名の変換 start")
    df1 = df1.rename(columns=MAPPING_03)
    df2 = df2.rename(columns=MAPPING_04)

    # 日付変換
    print("🐈 日付・日時変換 start")
    for item in TYPE_DICT_03["date"]:
        df1[item] = df1[item].apply(convert_date_str)
    for item in TYPE_DICT_04["date"]:
        df2[item] = df2[item].apply(convert_date_str)
    # 日時変換
    for item in TYPE_DICT_03["datetime"]:
        df1[item] = df1[item].apply(convert_datetime_str)
    for item in TYPE_DICT_04["datetime"]:
        df2[item] = df2[item].apply(convert_datetime_str)

    # マージしてCSVに出力
    print("🐈 merge start")
    result_df = pd.merge(df1, df2, on="item_038", how="outer").fillna("")

    # role_idを追加
    print("🐈 role_id追加 start")
    result_df["role_id"] = "initial_role"

    # unique_keyを追加
    print("🐈 unique_key追加 start")
    result_df["unique_key"] = result_df["item_038"] + "_" + result_df["item_041"]

    # ファイル出力
    print("🐈 ファイル出力 start")
    result_df.to_csv("sfa_files/company.csv", index=False, quoting=1)

    # 45000件ずつに分割
    split_csv("sfa_files/company.csv", 45000)


def make_customer_csv() -> None:
    pass  # make_company_csvと同じ感じで作成してください


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # TODO: ここに引数を追加してください
    parser.add_argument("--company", action="store_true")
    parser.add_argument("--customer", action="store_true")

    args = parser.parse_args()

    # TODO: ここに引数に応じた処理を追加してください
    if args.company:
        make_company_csv()
    if args.customer:
        make_customer_csv()
