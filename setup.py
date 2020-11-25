import setuptools

setuptools.setup(
    name="setup_test",
    packages=setuptools.find_packages(),
    # install_requires=['setuptools-git'],
    # install_requires=['setuptools-scm'],
    include_package_data=True,
    package_data={'tmp': ['tmp/ref/*']},
    python_requires='>=3.6',
)
