from .utils import loadgpd
from .env import EnvVar

gdf_dic = {
    "abm_region_gen3_4326": loadgpd(
        EnvVar.path["GEODBPATH"], f"abm_region_gen3", epsg=4326
    ),
    "abm_departement_gen3_4326": loadgpd(
        EnvVar.path["GEODBPATH"], f"abm_departement_gen3", epsg=4326
    ),
    "abm_pays_gen3_4326": loadgpd(
        EnvVar.path["GEODBPATH"], f"abm_pays_europe_gen3", epsg=4326
    ),
}