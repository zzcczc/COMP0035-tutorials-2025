import pandas as pd
from pathlib import Path

if __name__ == "__main__":
    # 定位到数据文件
    project_root = Path(__file__).parent.parent.parent
    csv_path = project_root / "activities" / "data" / "paralympics_raw.csv"
    excel_path = project_root / "activities" / "data" / "paralympics_all_raw.xlsx"
    # 1️⃣ 读取 CSV 文件
    df_csv = pd.read_csv(csv_path)
    print("CSV 文件读取成功 ✅")
    print(df_csv.head())  # 打印前 5 行数据

    # 2️⃣ 读取 Excel 文件的第一个 sheet
    df_excel_1 = pd.read_excel(excel_path, sheet_name=0)
    print("\nExcel 第一个工作表：")
    print(df_excel_1.head())

    # 3️⃣ 读取 Excel 文件的第二个 sheet
    df_excel_2 = pd.read_excel(excel_path, sheet_name=1)
    print("\nExcel 第二个工作表：")
    print(df_excel_2.head())