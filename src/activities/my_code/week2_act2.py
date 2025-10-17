import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


def get_data_paths():
    """
    获取 CSV 和 Excel 数据文件的路径。

    该函数通过当前脚本的位置自动定位项目根目录，并构建
    activities/data 目录下数据文件的完整路径。

    Returns:
        tuple[Path, Path]:
            包含两个元素的元组 (csv_path, excel_path)，
            分别为 CSV 文件路径和 Excel 文件路径。
            如果发生错误，则返回 (None, None)。
    """
    try:
        project_root = Path(__file__).parent.parent.parent
        csv_path = project_root / "activities" / "data" / "paralympics_raw.csv"
        excel_path = project_root / "activities" / "data" / "paralympics_all_raw.xlsx"
        return csv_path, excel_path
    except Exception as e:
        print(f"获取数据路径时出错: {e}")
        return None, None


def read_csv_file(file_path):
    """
    读取 CSV 文件为 pandas DataFrame。

    Args:
        file_path (Path or str): CSV 文件路径。

    Returns:
        pd.DataFrame | None:
            成功时返回读取到的 DataFrame；
            发生错误时返回 None。
    """
    try:
        df = pd.read_csv(file_path)
        print("CSV 文件读取成功 ✅")
        return df
    except Exception as e:
        print(f"读取 CSV 文件时出错: {e}")
        return None


def read_excel_file(file_path, sheet_name=0):
    """
    读取 Excel 文件中的指定工作表。

    Args:
        file_path (Path or str): Excel 文件路径。
        sheet_name (int | str, optional): 要读取的工作表名称或索引，默认为 0。

    Returns:
        pd.DataFrame | None:
            成功时返回读取到的 DataFrame；
            发生错误时返回 None。
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Excel 工作表 {sheet_name} 读取成功 ✅")
        return df
    except Exception as e:
        print(f"读取 Excel 文件时出错: {e}")
        return None

def identify_missing_values(df):
    try:
        print(df.isna().sum())
        df.fillna(0, inplace=True)
        print("缺失值以0填充成功")
    except Exception as e:
        print(f"处理缺失值时出错: {e}")
        return None


def describe_data(df):
    """
    打印 DataFrame 的基本信息与统计描述。

    该函数会输出：
        - 数据形状（行数、列数）
        - 前五行与后五行
        - 所有列名
        - 各列数据类型
        - DataFrame 的整体信息（info）
        - 数值型列的统计摘要（describe）

    Args:
        df (pd.DataFrame): 需要描述的 DataFrame。

    Returns:
        None
    """
    try:
        pd.set_option("display.max_columns", None)
        print("形状:", df.shape)
        print("前五行:\n", df.head())
        print("后五行:\n", df.tail())
        print("列:", df.columns.tolist())
        print("数据类型:\n", df.dtypes)
        df.info()
        print("数值型列统计描述:\n")
        print(df.describe())
        print("就这样看吧！")
    except Exception as e:
        print(f"解释文件时出错: {e}")
        return None

def plot_data(df):
    """
    绘制 DataFrame 中指定列的散点图。

    Args:
        df (pd.DataFrame): 包含数据的 DataFrame。
    """
    # Using pandas.plot directly creates the figure, axes and allows for some customisation
    # matplotlib examples typically split this into separate commands defining fig and ax then adding customisation
    ax = df.plot(title='Sample Plot', xlabel='X-axis Label', ylabel='Y-axis Label')

    # Save plot (may prefer this to showing the plot)
    plt.savefig('sample_plot.png')

    # Show the plot
    plt.show()

def create_boxplot(df):
    """
    创建 DataFrame 的箱线图。

    Args:
        df (pd.DataFrame): 包含数据的 DataFrame。
    """
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        df.boxplot(column=[col])  # how to plot seperately for each column?
        plt.show()

def year_and_participation(df):
    print('test', df)
    ar=df.plot(x='start', y='participants', title='Year vs Number of Participants')
    plt.savefig('sample_plot.png')
    plt.show()

def unique_countries(df):
    try:
        unique_countries = df['country'].unique()
        print(f"Unique countries: {unique_countries}")
        print(df['country'].value_counts())
    except Exception as e:
        print(f"计算唯一国家时出错: {e}")
        return None

if __name__ == "__main__":
    """
    主程序入口。

    该部分会：
        1. 获取数据文件路径；
        2. 读取 CSV 与 Excel 文件；
        3. 对每个 DataFrame 调用 describe_data() 打印信息。
    """
    csv_path, excel_path = get_data_paths()
    df_csv = read_csv_file(csv_path)
    df_excel = read_excel_file(excel_path)
    identify_missing_values(df_csv)
    identify_missing_values(df_excel)
    describe_data(df_csv)
    describe_data(df_excel)
    """
    plot_data(df_csv)
    plot_data(df_excel)

    # Create a histogram of the DataFrame
    df_csv.hist()

    # Show the plot
    plt.show()    
    
    # boxplot
    create_boxplot(df_csv)
    # unique countries
    year_and_participation(df_csv)
    """
    unique_countries(df_csv)