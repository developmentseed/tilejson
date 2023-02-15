# tilejson

<p align="center">
  <img max-width="800" src="https://user-images.githubusercontent.com/10407788/218823077-5c1567c9-79f0-4147-af92-0fe901986dff.gif"/>
  <p align="center">Create simple map viewer from TileJSON URL.</p>
</p>

<p align="center">
  <a href="https://github.com/developmentseed/tilejson/actions?query=workflow%3ACI" target="_blank">
      <img src="https://github.com/developmentseed/tilejson/workflows/CI/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/developmentseed/tilejson" target="_blank">
      <img src="https://codecov.io/gh/developmentseed/tilejson/branch/main/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/tilejson" target="_blank">
      <img src="https://img.shields.io/pypi/v/tilejson?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/developmentseed/tilejson/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/developmentseed/tilejson.svg" alt="Downloads">
  </a>
</p>


## Install

You can install tilejson using pip

```bash
$ pip install tilejson
```

Build from source

```bash
$ git clone https://github.com/developmentseed/tilejson.git
$ cd tilejson
$ pip install -e .
```

## CLI

```bash
$ tilejson --help
Usage: tilejson [OPTIONS] URL

  tilejson cli.

Options:
  --no-geo           Create Map viewer for non-geo image.
  -o, --output PATH  Output file name.
  --help             Show this message and exit.
```

## How it works

The `tilejson` CLI will create simple map viewer (using [MapLibre](https://maplibre.org/projects/)) with a reference to the input tilejson URL.

By default the HTML code will be saved in a system temporary directory but user can pass an `--output` option to store the HTML file in a custom place.

Once the HTML document is created, `click` will [*launch*](https://click.palletsprojects.com/en/8.1.x/api/#click.launch) the page, opening it with the user's default browser.

## Contribution & Development

See [CONTRIBUTING.md](https://github.com/developmentseed/tilejson/blob/main/CONTRIBUTING.md)

## Authors

Created by [Development Seed](<http://developmentseed.org>)

## Changes

See [CHANGES.md](https://github.com/developmentseed/tilejson/blob/main/CHANGES.md).

## License

See [LICENSE.txt](https://github.com/developmentseed/tilejson/blob/main/LICENSE)
