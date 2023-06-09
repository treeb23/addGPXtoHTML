# addGPXtoHTML

> ver 0.1 2023/04/11 GPXからDataFrameを作成,DataFrameを結合して一つのHTMLに複数のGPXデータを重ねたマップを記録する

https://github.com/kurama8103/gpxdf を利用している

まず必要なライブラリのインストール

`!注意 geospatial はインストールに1〜2分かかる`

```py
!pip install geospatial
!pip3 install git+https://github.com/kurama8103/gpxdf
```
インポート
```py
import pandas as pd
import leafmap
import gpxdf
```
このライブラリをインストールしてインポート
```py
!pip install git+https://github.com/treeb23/addGPXtoHTML.git
import addGPXtoHTML as agh
```
filepathを設定
```py
agh.filepath()
```

leafletマップを表示
```py
agh.leafmap_view(latitude=35,longitude=140,zoom=4)
```

data/gpx/gpxdf.csvがない場合、GPXファイルをDataFrameに変換してdata/gpx/gpxdf.csvに書き出し

data/gpx/gpxdf.csvがある場合、GPXファイルをDataFrameに変換してdata/gpx/gpxdf.csvをDataFrameに変換したものと結合し、
結合したものをHTMLに書き出す。DataFrameをdata/gpx/gpxdf.csvに書き出し(更新)

引数`mode='r'`でdata/gpx/gpxdf.csvにすでに追加されたトラック一覧を表示(他の引数は指定する必要なし)

```py
agh.addgpxtohtml(gpx_filename,outhtml_filename,mode)
```
