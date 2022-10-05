import geopandas  # type: ignore
import matplotlib  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

matplotlib.use("TkAgg")

POLYGON_WKT = [
    "POLYGON ((35 10, 45 45, 15 40, 10 20, 35 10), (20 30, 35 35, 30 20, 20 30))"
]
POINTS = [
    "POINT (35 10)",
    "POINT (2 2)",
    "POINT (3 3)",
]
LINE = ["LINESTRING (30 10, 10 30, 40 40)"]


def plot_example_file() -> None:
    geoseries = geopandas.GeoSeries.from_wkt(POINTS)

    print(geoseries)
    geoseries.plot()

    plt.show()


def plot_intersection() -> None:
    polygon = geopandas.GeoSeries.from_wkt(POLYGON_WKT)
    line = geopandas.GeoSeries.from_wkt(LINE)
    intersection = polygon.intersection(line, align=True)
    intersection.plot()
    plt.show()
