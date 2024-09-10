import re
from datetime import datetime

import pandas as pd


def convert_date_str(date_str: str) -> str:
    """日付を表す文字列から、SFAの日付形式の文字列に変換します

    Args:
        prev_datetime_string (str): 移行元の日付を表す文字列

    Raises:
        ValueError: サポートされていない日付形式が入力された場合
    Returns:
        str: SFAの日付形式の文字列

    Notes:
        正しいのはこれ
            - 2020/03/18
    """
    date_str = str(date_str)

    if date_str == "":
        return ""

    # yyyy-mm-dd hh:mm:ss を yyyy/mm/dd に変換
    if re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", date_str):
        return date_str[:10].replace("-", "/")

    # 日付形式の正規表現パターン
    date_patterns = [
        # ISO 8601形式
        (r"^\d{4}-\d{2}-\d{2}$", "%Y-%m-%d"),
        (r"^\d{8}$", "%Y%m%d"),
        # スラッシュ区切り
        (r"^\d{4}/\d{2}/\d{2}$", "%Y/%m/%d"),
        (r"^\d{2}/\d{2}/\d{4}$", "%m/%d/%Y"),
        (r"^\d{2}/\d{2}/\d{2}$", "%m/%d/%y"),
        (r"^\d{2}/\d{2}/\d{2}$", "%d/%m/%y"),
        # ドット区切り
        (r"^\d{4}\.\d{2}\.\d{2}$", "%Y.%m.%d"),
        (r"^\d{2}\.\d{2}\.\d{4}$", "%d.%m.%Y"),
        # ハイフン区切り
        (r"^\d{2}-\d{2}-\d{4}$", "%d-%m-%Y"),
        (r"^\d{2}-\d{2}-\d{2}$", "%d-%m-%y"),
        (r"^\d{2}-\d{2}-\d{4}$", "%m-%d-%Y"),
        (r"^\d{2}-\d{2}-\d{2}$", "%m-%d-%y"),
        # テキスト形式
        (r"^\d{2} [A-Za-z]{3} \d{4}$", "%d %b %Y"),
        (r"^[A-Za-z]{3} \d{2}, \d{4}$", "%b %d, %Y"),
        (r"^\d{2} [A-Za-z]+ \d{4}$", "%d %B %Y"),
        (r"^[A-Za-z]+ \d{2}, \d{4}$", "%B %d, %Y"),
        # 日本語形式
        (r"^\d{4}年\d{2}月\d{2}日$", "%Y年%m月%d日"),
        (r"^\d{4}年\d{1}月\d{1}日$", "%Y年%m月%d日"),
        (r"^\d{2}年\d{2}月\d{2}日$", "%y年%m月%d日"),
        # 日付と曜日
        (r"^\d{4}-\d{2}-\d{2} \([A-Za-z]{3}\)$", "%Y-%m-%d (%a)"),
        (r"^\d{2}/\d{2}/\d{4} \([A-Za-z]{3}\)$", "%d/%m/%Y (%a)"),
    ]

    for pattern, date_format in date_patterns:
        if re.match(pattern, date_str):
            try:
                parsed_date = datetime.strptime(date_str, date_format)
                return parsed_date.strftime("%Y/%m/%d")
            except ValueError:
                continue

    raise ValueError(f"Unsupported date format: {date_str}")


def convert_datetime_str(datetime_str: str) -> str:
    """日時を表す文字列から、SFAの日時形式の文字列に変換します

    Args:
        datetime_str (str): 移行元の日時を表す文字列

    Raises:
        ValueError: サポートされていない日時形式が入力された場合
    Returns:
        str: SFAの日時形式の文字列

    Notes:
        正しいのはこれ
            - 2020/03/18 17:08:10
    """
    datetime_str = str(datetime_str)

    if datetime_str == "":
        return ""

    # 日時形式の正規表現パターン
    datetime_patterns = [
        # ISO 8601形式
        (r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", "%Y-%m-%dT%H:%M:%S%z"),
        (r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$", "%Y-%m-%dT%H:%M:%S"),
        (r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", "%Y-%m-%d %H:%M:%S"),
        (r"^\d{8}T\d{6}$", "%Y%m%dT%H%M%S"),
        (r"^\d{8} \d{6}$", "%Y%m%d %H%M%S"),
        # スラッシュ区切り
        (r"^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}$", "%Y/%m/%d %H:%M:%S"),
        (r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$", "%m/%d/%Y %H:%M:%S"),
        (r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$", "%d/%m/%Y %H:%M:%S"),
        # ドット区切り
        (r"^\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}$", "%Y.%m.%d %H:%M:%S"),
        (r"^\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}$", "%d.%m.%Y %H:%M:%S"),
        # ハイフン区切り
        (r"^\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}$", "%d-%m-%Y %H:%M:%S"),
        (r"^\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}$", "%m-%d-%Y %H:%M:%S"),
        # テキスト形式
        (r"^\d{2} [A-Za-z]{3} \d{4} \d{2}:\d{2}:\d{2}$", "%d %b %Y %H:%M:%S"),
        (r"^[A-Za-z]{3} \d{2}, \d{4} \d{2}:\d{2}:\d{2}$", "%b %d, %Y %H:%M:%S"),
        (r"^\d{2} [A-Za-z]+ \d{4} \d{2}:\d{2}:\d{2}$", "%d %B %Y %H:%M:%S"),
        (r"^[A-Za-z]+ \d{2}, \d{4} \d{2}:\d{2}:\d{2}$", "%B %d, %Y %H:%M:%S"),
        # 日本語形式
        (r"^\d{4}年\d{2}月\d{2}日 \d{2}時\d{2}分\d{2}秒$", "%Y年%m月%d日 %H時%M分%S秒"),
        (r"^\d{4}年\d{1}月\d{1}日 \d{2}時\d{2}分\d{2}秒$", "%Y年%m月%d日 %H時%M分%S秒"),
    ]

    for pattern, datetime_format in datetime_patterns:
        if re.match(pattern, datetime_str):
            try:
                parsed_datetime = datetime.strptime(datetime_str, datetime_format)
                return parsed_datetime.strftime("%Y/%m/%d %H:%M:%S")
            except ValueError:
                continue

    raise ValueError(f"Unsupported datetime format: {datetime_str}")


def get_df(file_path: str, encoding: str | None = None) -> pd.DataFrame:
    """ファイルを読み込み、DataFrameを返す

    Args:
        file_path (str): 読み取るファイルのパス
        encoding (str | None, optional): エンコーディング. Defaults to None.

    Raises:
        ValueError: サポートされていないファイル形式(csv, tsv, xlsxのみ対応している)

    Returns:
        pd.DataFrame: 読み取ったDataFrame

    Examples:
        >>> get_df("prev_files/data.csv")
        >>> get_df("middle_files/marimo.xlsx")
    """
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path, encoding=encoding, dtype=str).fillna("")
    if file_path.endswith(".xlsx"):
        return pd.read_excel(file_path, dtype=str).fillna("")
    if file_path.endswith(".tsv"):
        return pd.read_csv(file_path, sep="\t", dtype=str).fillna("")
    raise ValueError("Unsupported file format")


def split_csv(file_path: str, chunksize: int = 100_000) -> None:
    """csvファイルを読み込み、10万件ずつに分割して保存します

    Args:
        file_name (str): ファイル名
        chunksize (int): 分割数. Defaults to 100_000.

    Examples:
        >>> split_csv("sfa_files/hogehoge.csv")

    Notes:
        converted_csv_filesディレクトリにあるファイルを指定してください

    Raises:
        ValueError: サポートされていないファイル形式(csvのみ対応している)
    """
    if not file_path.endswith(".csv"):
        raise ValueError("Unsupported file format")

    df = pd.read_csv(file_path, dtype=str).fillna("").astype(str)
    for i, size in enumerate(range(0, len(df), chunksize)):
        now_df = df.iloc[size : size + chunksize]
        file_no = str(i + 1).zfill(2)
        now_df.to_csv(f"{file_path[:-4]}_{file_no}.csv", index=False, quoting=1)
