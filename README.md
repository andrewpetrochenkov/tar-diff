<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/v/tar-diff.svg?maxAge=3600)](https://pypi.org/project/tar-diff/)
[![](https://img.shields.io/npm/v/tar-diff.svg?maxAge=3600)](https://www.npmjs.com/package/tar-diff)
[![Travis](https://api.travis-ci.org/looking-for-a-job/tar-diff.svg?branch=master)](https://travis-ci.org/looking-for-a-job/tar-diff/)

#### Installation
```bash
$ [sudo] npm i -g tar-diff
```
```bash
$ [sudo] pip install tar-diff
```

#### Features
file/url arguments supported

#### CLI
```bash
usage: tar-diff archive1 archive2
```

#### Examples
```bash
$ diff="$(tar-diff archive1.tar.gz archive2.tar.gz)"
```

complicated example. bump python project version
```bash
$ dist_dir="$(mktemp -d)"
$ python setup.py sdist --dist-dir="$dist_dir" &> /dev/null
$ sdist="$(find "$dist_dir" -type f)"
$ url="$(python -m pypi_get.urls <name> | grep tar.gz)"
$ diff="$(tar-diff "$sdist" "$url")"
$ [[ -n "$diff" ]] && bumpversion
```

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>