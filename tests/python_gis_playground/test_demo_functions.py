from python_gis_playground.demo_functions import plot_example_file, plot_intersection


def test_plot_file() -> None:
    plot_example_file()


# @pytest.mark.skip(reason="Doesn't work yet")
def test_find_intersection() -> None:
    plot_intersection()
