from setuptools import setup

filepath = "uitable/README.md"

setup(
    name="uitable",
    version="0.2",
    description="display data by table format",
    long_description=open(filepath).read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yxxhero/uitable",
    author="yxxhero",
    author_email="aiopsclub@163.com",
    license="MIT",
    packages=["uitable"],
    zip_safe=False,
)
