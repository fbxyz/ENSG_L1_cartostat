import numpy as np
import pandas as pd
import geopandas as gpd
import mapclassify as mc

from .env import EnvVar


def loadgpd(dbpath, layer, where=None, epsg=None):
    """charge un layer du geopackage. Possibilité de filtrer par where clause ("insee_reg == '76'")
    ou par bbox (minx, miny, maxx, maxy)"""
    gdf = gpd.read_file(dbpath, layer=layer)
    gdf = gdf.query(where) if where is not None else gdf
    gdf = gdf.to_crs(epsg=epsg) if epsg is not None else gdf
    return gdf


def discretisation(_gdf, method, k, cmap,_ind=EnvVar.indic['COLUMN_INDIC'],class_only=True):
    k = int(k)

    gdfna = _gdf.query(
        f"{_ind}!={_ind}"
    ).copy()
    gdf = _gdf.query(
        f"{_ind}=={_ind}"
    ).copy()

    if method == "EqualInterval":
        scheme = mc.EqualInterval(gdf[_ind], k=k)
    elif method == "Quantiles":
        scheme = mc.Quantiles(gdf[_ind], k=k)
    elif method == "FisherJenks":
        scheme = mc.FisherJenks(gdf[_ind], k=k)
    elif method == "Q6":
        scheme = mc.Percentiles(
            gdf[_ind], pct=[5, 25, 50, 75, 95, 100]
        )
        k = 6
    elif method == "StdMean":
        scheme = mc.StdMean(
            gdf[_ind], multiples=[-1.5, -0.5, 0.5, 1.5]
        )
        cmap = "RdYlGn"
    else:
        raise print(f"erreur sur carte_choro_france: parametre {method} inconnu")

    # Definir les bins et colors
    bins = np.insert(scheme.bins, 0, gdf[_ind].min())
    colors = EnvVar.CmapDefs[cmap][k]

    gdf["colors"] = pd.cut(gdf[_ind], bins=bins, include_lowest=True, labels=colors)
    gdfna["colors"] = "#FFFFFF"
    gdfna["IND_CLASS"] = "Non calculable"
    gdf["IND_CLASS"] = pd.cut(gdf[_ind], bins=bins, include_lowest=True)
    gdf["IND_CLASS"] = (
        gdf["IND_CLASS"]
        .apply(lambda x: pd.Interval(left=round(x.left, 1), right=round(x.right, 1)))
        .astype(str)
        .str.replace("(", "]", regex=False)
    )

    if class_only : 
        return pd.concat([gdf, gdfna])
    
    else :
        return  pd.concat([gdf, gdfna]), bins
    