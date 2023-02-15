"""tilejson."""

import contextlib
import tempfile

import click
from starlette.templating import Jinja2Templates

try:
    from importlib.resources import files as resources_files  # type: ignore
except ImportError:
    # Try backported to PY<39 `importlib_resources`.
    from importlib_resources import files as resources_files  # type: ignore

template_dir = str(resources_files(__package__) / "templates")  # type: ignore
templates = Jinja2Templates(directory=template_dir)


@click.command()
@click.argument("url", type=str, nargs=1, required=True)
@click.option(
    "--no-geo", is_flag=True, default=False, help="Create Map viewer for non-geo image."
)
@click.option("--output", "-o", type=click.Path(exists=False), help="Output file name.")
def tilejson(url, no_geo, output):
    """tilejson cli."""
    click.echo(url)

    if no_geo:
        tm = templates.TemplateResponse(
            name="index_nogeo.html",
            context={"tilejson_endpoint": url, "request": {}},
            media_type="text/html",
        )
    else:
        tm = templates.TemplateResponse(
            name="index.html",
            context={"tilejson_endpoint": url, "request": {}},
            media_type="text/html",
        )

    with contextlib.ExitStack() as ctx:
        if output:
            f = ctx.enter_context(open(output, "wb"))
        else:
            f = ctx.enter_context(
                tempfile.NamedTemporaryFile(suffix=".html", delete=False)
            )

        f.write(tm.body)

    click.launch(f.name)
