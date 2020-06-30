<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/tar-diff.svg?maxAge=3600)](https://pypi.org/project/tar-diff/)
[![](https://img.shields.io/npm/v/tar-diff.svg?maxAge=3600)](https://www.npmjs.com/package/tar-diff)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/tar-diff/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/tar-diff/actions)

### Installation
```bash
$ [sudo] pip install tar-diff
```

```bash
$ [sudo] npm i -g tar-diff
```

#### Features
file/url arguments supported

#### Examples
```bash
$ diff="$(tar-diff archive1.tar.gz archive2.tar.gz)"
```

complicated example. bump python project version
```bash
$ dist_dir="$(mktemp -d)"
$ python setup.py sdist --dist-dir="$dist_dir" &> /dev/null
$ sdist="$(find "$dist_dir" -type f -name "*.tar.gz")"
$ url="$(python -m pypi_get.urls <name> | grep tar.gz)"
$ diff="$(tar-diff "$sdist" "$url")"
$ [[ -n "$diff" ]] && bumpversion
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>