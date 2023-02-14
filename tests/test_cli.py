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
