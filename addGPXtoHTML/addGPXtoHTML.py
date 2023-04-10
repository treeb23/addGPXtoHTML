import pandas as pd
import leafmap
import gpxdf

def filepath(): # ファイルパスの設定
    global f_path
    f_path=".."
    try:
        from google.colab import drive # Google Driveをcolabにマウント
        drive.mount('/content/drive')
        f_path="/content/drive/MyDrive/lab"
    except ModuleNotFoundError as e:
        print(e)
    print(f"[ファイルパスf_pathを'{f_path}'に設定]")


def leafmap_view(latitude=35,longitude=140,zoom=4):#mapを表示
    m = leafmap.Map(center=(latitude, longitude), zoom=zoom)
    return m

def addgpxtohtml(gpx_filename="abc",outhtml_filename="abc",mode='w'):
    if mode=='w':
        df = gpxdf.read_gpx(f'{f_path}/data/gpx/{gpx_filename}.gpx')
        try:
            df2 = pd.read_csv(f"{f_path}/data/gpx/gpxdf.csv")
            u = df2['trackname'].unique()
            print(f'すでに追加されたトラック一覧:{u}')
            df2=df2.append(df, ignore_index=True)
            gpxdf.to_html_map(df2, f'{f_path}/data/gpx/{outhtml_filename}.html',zoom_start=11)
            df2.to_csv(f"{f_path}/data/gpx/gpxdf.csv",index=False)
            print(f"data/gpx/{outhtml_filename}.htmlを作成。data/gpx/gpxdf.csvを更新")
        except:
            df.to_csv(f"{f_path}/data/gpx/gpxdf.csv",index=False)
            print(f"data/gpx/gpxdf.csvを作成")
    else:
        df = pd.read_csv(f"{f_path}/data/gpx/gpxdf.csv")
        u = df['trackname'].unique()
        print(f'すでに追加されたトラック一覧:{u[0:-1]}')
