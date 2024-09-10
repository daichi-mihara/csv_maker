from typing import TypedDict


class TypeInfo(TypedDict):
    date: list[str]
    datetime: list[str]
    number: list[str]

# TODO: カラムのマッピング情報を定義します。
# キー: 先方のカラム名、バリュー: SFAでのカラム名
MAPPING_03 = {
    "M_CUSTOMERID": "item_038",
    "KYA_CD": "item_021",
    "M_SYURYUDEPARTMENTID": "item_057",
    "M_BTSRYUDEPARTMENTID": "item_058",
    "M_DEMANDSTATUSCLASS": "item_059",
    "M_CUSTOMERSTATUSCLASS": "item_060",
    "M_CUSTOMERZUGNCLASS": "item_061",
    "M_LPGCUSTOMERZUGNREASONCLASS": "item_062",
    "M_LPGOTHERCOMPANYCHANGEFORTX": "item_063",
    "M_GASSTOPYMD": "item_064",
    "M_GASSTOPLIFTINGYMD": "item_065",
    "M_GASSTOPREASONCLASS1": "item_066",
    "M_GASSTOPREASONCLASS2": "item_067",
    "M_GASSTOPREASONCLASS3": "item_068",
    "M_GASSTOPREASONCLASS4": "item_069",
    "M_CUSTOMERID_DISP": "item_070",
    "ENT_TS": "item_071",
    "ENT_TANCD": "item_072",
    "UPD_TS": "item_073",
    "UPD_TANCD": "item_074",
    "UPD_FNC_ID": "item_075",
    "DEL_FLG": "item_076",
}
# TODO: カラムの型情報を定義します。
# キー: SFAでのカラム名、バリュー: そのカラムの型
TYPE_DICT_03 = TypeInfo(
    date=["item_064", "item_065"],
    datetime=["item_071", "item_073"],
    number=[],
)


MAPPING_04 = {
    "KYA_CD": "item_021",
    "KYA_JNM": "company_name",
    "KYA_KNM": "item_001",
    "ZIP_NO1": "zip_cd",
    "ZIP_NO2": "zip_cd_2",
    "KEN_CD": "prefecture_div",
    "ADR_JNM": "city",
    "ADR_KNM": "item_003",
    "BLD_JNM": "address",
    "ROOM_NO": "item_004",
    "SADR_JNM": "item_193",
    "SADR_KNM": "item_194",
    "SBLD_JNM": "item_195",
    "HAN_CD": "__custom_object_index_7_id",
    "M_CUSTOMERID": "item_038",
    "M_DEMANDID": "item_041",
    "ENT_KBN": "item_196",
    "MEIBO_KBN": "item_051",
    "ENT_TS": "item_071",
    "ENT_TANCD": "item_072",
    "UPD_TS": "item_073",
    "UPD_TANCD": "item_074",
    "UPD_FNC_ID": "item_075",
    "DEL_FLG": "item_076",
}
TYPE_DICT_04 = TypeInfo(
    date=[],
    datetime=["item_071", "item_073"],
    number=[],
)
