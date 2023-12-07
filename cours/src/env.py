
class EnvVar:
    path = {
        "GEODBPATH": "./data/geo.sqlite",
    }

    metro = {
        "WIDTH": 530,
        "HEIGHT": 530,
        "PROJ": "conicConformal",
        "SCALE": 2800,
        "CENTER": [-3.35, 51.4], #[-3.35, 46.2],
        "ROTATE": [0, 0, -1.5],
    }

    drom = {
        "WIDTH": 50,
        "HEIGHT": 50,
        "SCALE_GUA": 3800,
        "CENTER_GUA": [-61.89, 16.55],
        "SCALE_MTQ": 4500,
        "CENTER_MTQ": [-61.35, 14.95],
        "SCALE_GUY": 700,
        "CENTER_GUY": [-53.280, 3.5],
        "SCALE_REU": 3900,
        "CENTER_REU": [55.15, -20.77],
        "SCALE_MAY": 5200,
        "CENTER_MAY": [44.865, -12.55],
        "SCALE_NCA": 5200,
        "CENTER_NCA": [163.7, -19.2],
        "SCALE_POL": 5200,
        "CENTER_POL": [-149.95, -17.25],
        "PROJ": "mercator",
        "ROTATE": [0, 0, 0],
    }

    template = {
        "TITLE_DROM_COL": "#4d4d4d",
        "TITLE_DROM_SZE": 8,
        "LEG_LABEL_COL": "#6c757d",
        "LEG_TITLE_COL": "#6c757d",
    }

    indic = {"COLUMN_INDIC": "IND"}

    CmapDefs = {
        "YlOrRd": {
            4: ["#ffffb2", "#fecc5c", "#fd8d3c", "#e31a1c"],
            5: ["#ffffb2", "#fecc5c", "#fd8d3c", "#f03b20", "#bd0026"],
            6: ["#ffffb2", "#fed976", "#feb24c", "#fd8d3c", "#f03b20", "#bd0026"],
        },
        "Blues": {
            4: ["#eff3ff", "#bdd7e7", "#6baed6", "#2171b5"],
            5: ["#eff3ff", "#bdd7e7", "#6baed6", "#3182bd", "#08519c"],
            6: ["#eff3ff", "#c6dbef", "#9ecae1", "#6baed6", "#3182bd", "#08519c"],
        },
        "Greens": {
            4: ["#edf8e9", "#bae4b3", "#74c476", "#238b45"],
            5: ["#edf8e9", "#bae4b3", "#74c476", "#31a354", "#006d2c"],
            6: ["#edf8e9", "#c7e9c0", "#a1d99b", "#74c476", "#31a354", "#006d2c"],
        },
        "Reds": {
            4: ["#fee5d9", "#fcae91", "#fb6a4a", "#cb181d"],
            5: ["#fee5d9", "#fcae91", "#fb6a4a", "#de2d26", "#a50f15"],
            6: ["#fee5d9", "#fcbba1", "#fc9272", "#fb6a4a", "#de2d26", "#a50f15"],
        },
        "Oranges": {
            4: ["#fee5d9", "#fdbe85", "#fd8d3c", "#d94701"],
            5: ["#fee5d9", "#fdbe85", "#fd8d3c", "#e6550d", "#a63603"],
            6: ["#feedde", "#fdd0a2", "#fdae6b", "#fd8d3c", "#e6550d", "#a63603"],
        },
        "RdYlGn": {
            4: ["#1a9641", "#a6d96a", "#fdae61", "#d7191c"],
            5: ["#1a9641", "#a6d96a", "#ffffbf", "#fdae61", "#d7191c"],
            6: ["#1a9850", "#91cf60", "#d9ef8b", "#fee08b", "#fc8d59", "#d73027"],
        },
    }

    list_discret = [
        ["Intervalles egaux", "EqualInterval"],
        ["Fisher-Jenks", "FisherJenks"],
        ["Quantiles", "Quantiles"],
        ["Q6", "Percentiles"],
        ["Moyenne ecart-type", "StdMean"],
    ]


