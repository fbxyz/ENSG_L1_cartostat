import altair as alt
from .data import gdf_dic
from .env import EnvVar


def basemap_altair(alt_base, field, countries, type, scale, center, rotate=None):
    if rotate is None:
        rotate = [0, 0, 0]
    return (
        alt_base.encode()
        .transform_filter(alt.FieldOneOfPredicate(field=field, oneOf=countries))
        .project(type=type, scale=scale, center=center,rotate=rotate)
    )


def drom_maps(_base_fr, _exclude, _basemap):
    def _drom_template(alt_base, exclude, title, center, scale, rotate=None):
        if rotate is None:
            rotate = [0, 0, 0]
        return (
            alt_base.encode()
            .transform_filter(alt.FieldOneOfPredicate(field="COD_GEO", oneOf=exclude))
            .properties(
                width=50,
                height=50,
                title=alt.TitleParams(
                    title,
                    fontSize=EnvVar.template["TITLE_DROM_SZE"],
                    color=EnvVar.template["TITLE_DROM_COL"],
                ),
            )
            .project(
                type=EnvVar.drom["PROJ"], 
                center=center, 
                #scale=scale, 
                rotate=rotate
            )
        )

    gua = _drom_template(
        alt_base=_base_fr,
        exclude=_exclude["gua"],
        title=["Guadeloupe"],
        center=EnvVar.drom["CENTER_GUA"],
        scale=EnvVar.drom["SCALE_GUA"],
    )

    mtq = _drom_template(
        alt_base=_base_fr,
        exclude=_exclude["mtq"],
        title=["Martinique"],
        center=EnvVar.drom["CENTER_MTQ"],
        scale=EnvVar.drom["SCALE_MTQ"],
    )

    guy = _drom_template(
        alt_base=_base_fr,
        exclude=_exclude["guy"],
        title=["Guyane"],
        center=EnvVar.drom["CENTER_GUY"],
        scale=EnvVar.drom["SCALE_GUY"],
    )

    reu = _drom_template(
        alt_base=_base_fr,
        exclude=_exclude["reu"],
        title=["Réunion"],
        center=EnvVar.drom["CENTER_REU"],
        scale=EnvVar.drom["SCALE_REU"],
    )

    may = _drom_template(
        alt_base=_base_fr,
        exclude=_exclude["may"],
        title=["Mayotte"],
        center=EnvVar.drom["CENTER_MAY"],
        scale=EnvVar.drom["SCALE_MAY"],
    )

    nca = _drom_template(
        alt_base=_base_fr,
        exclude=_exclude["nca"],
        title=["Nouvelle-", "Calédonie"],
        center=EnvVar.drom["CENTER_NCA"],
        scale=EnvVar.drom["SCALE_NCA"],
    )

    pol = _drom_template(
        alt_base=_base_fr,
        exclude=_exclude["pol"],
        title=["Polynésie"],
        center=EnvVar.drom["CENTER_POL"],
        scale=EnvVar.drom["SCALE_POL"],
    )

    basemap_guy = basemap_altair(
        alt_base=_basemap,
        field="code_pays_iso3",
        countries=["SUR", "BRA"],
        type=EnvVar.drom["PROJ"],
        scale=EnvVar.drom["SCALE_GUA"],
        center=EnvVar.drom["CENTER_GUA"],
    )

    return alt.vconcat(
        gua, mtq, alt.layer(basemap_guy, guy), reu, may, nca, pol, spacing=10
    )


def map_altair(fr, ind, ind_class, ind_colors, ue, geo, title, legend_title):
    if geo == "REG":
        exclude = {
            "metro": ["01", "02", "03", "04", "06", "988", "987"],
            "gua": ["01"],
            "mtq": ["02"],
            "guy": ["03"],
            "reu": ["04"],
            "may": ["06"],
            "nca": ["988"],
            "pol": ["987"],
        }

    else:
        exclude = {
            "metro": ["971", "972", "973", "974", "976", "988", "987"],
            "gua": ["971"],
            "mtq": ["972"],
            "guy": ["973"],
            "reu": ["974"],
            "may": ["976"],
            "nca": ["988"],
            "pol": ["987"],
        }

    basemap = (
        alt.Chart(ue)
        .mark_geoshape(
            fill="#ebeced",
            stroke="#4d4d4d",
            strokeWidth=0.35,
        )
        .encode()
        .properties(width=EnvVar.metro["WIDTH"], height=EnvVar.metro["HEIGHT"])
    )

    basemap_ue = basemap_altair(
        alt_base=basemap,
        field="code_pays_iso3",
        countries=["BEL", "CHE", "DEU", "ESP", "GBR", "ITA", "LUX", "NLD", "AUT"],
        type=EnvVar.metro["PROJ"],
        scale=EnvVar.metro["SCALE"],
        center=EnvVar.metro["CENTER"],
        rotate=EnvVar.metro["ROTATE"],
    )

    sort = fr.sort_values(ind)
    dom = sort[ind_class].unique()
    col = list(fr[ind_colors].unique())


    base_fr = (
        alt.Chart(fr, title=title)
        .mark_geoshape(
            stroke="#4d4d4d",
            strokeWidth=0.35,
        )
        .encode(
            color=alt.Color(
                f"{ind_class}:O",
                scale=alt.Scale(domain=dom, range=col),
                legend=alt.Legend(title=f"{legend_title}"),
            ),
            tooltip=[
                alt.Tooltip("LIB_GEO:N", title="Libellé"),
                alt.Tooltip(f"{ind}:O", title=legend_title),
            ],
        )
    )

    metro = (
        base_fr.encode()
        .transform_filter(
            {"not": alt.FieldOneOfPredicate(field="COD_GEO", oneOf=exclude["metro"])}
        )
        .properties(width=EnvVar.metro["WIDTH"], height=EnvVar.metro["HEIGHT"])
        .project(
            type=EnvVar.metro["PROJ"],
            scale=EnvVar.metro["SCALE"],
            center=EnvVar.metro["CENTER"],
            rotate=EnvVar.metro["ROTATE"],
        )
    )

    row_drom = drom_maps(_base_fr=base_fr, _exclude=exclude, _basemap=basemap)

    all_maps = (
        alt.hconcat(row_drom, alt.concat(alt.layer(basemap_ue, metro)))
        .properties(center=True)

    )

    return all_maps