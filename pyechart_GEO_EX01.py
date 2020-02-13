import pandas as pd
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType
def insert_loc():
    g=Geo()
    data_pair=[]
    g.add_schema(maptype='china')
    airport_df = pd.read_excel('CN_airport_info.xlsx', usecols='B,D,E,F,S')
    for i in range(len(airport_df)):
        g.add_coordinate(airport_df.iloc[i,1], float(airport_df.iloc[i,3]), float(airport_df.iloc[i,2]))
        data_pair.append((airport_df.iloc[i,1],int(airport_df.iloc[i,4])))
    g.add('', data_pair, type_=GeoType.EFFECT_SCATTER, symbol_size=7)
    g.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    g.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=False),
        title_opts=opts.TitleOpts(title="全国机场分布图"),
    )
    return g
g=insert_loc()
g.render('airport_info.html')