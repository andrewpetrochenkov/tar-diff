import setuptools

setuptools.setup(
    name='tar-diff',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/tar-diff']
)
