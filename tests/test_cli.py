"""test tilejson cli."""

from unittest.mock import patch

from click.testing import CliRunner

from tilejson.cli import tilejson


@patch("click.launch")
def test_should_launch(launch):
    """Should work as expected."""

    launch.return_value = True

    runner = CliRunner()
    result = runner.invoke(
        tilejson, ["https://host/tilejson.json?https://something.io/test.tif"]
    )
    assert not result.exception
    assert result.exit_code == 0

    with runner.isolated_filesystem():
        result = runner.invoke(
            tilejson,
            [
                "https://host/tilejson.json?https://something.io/test.tif",
                "-o",
                "index.html",
            ],
        )
        assert not result.exception
        assert result.exit_code == 0
        with open("index.html", "r") as f:
            assert (
                "https://host/tilejson.json?https://something.io/test.tif" in f.read()
            )

    with runner.isolated_filesystem():
        result = runner.invoke(
            tilejson,
            [
                "https://host/tilejson.json?https://something.io/test.tif",
                "-o",
                "index.html",
                "--no-geo",
            ],
        )
        assert not result.exception
        assert result.exit_code == 0
        with open("index.html", "r") as f:
            assert "L.CRS.Simple" in f.read()
