# setup.py
import setuptools

setuptools.setup(name="hkrmlcourse",
      version="0.1",
      description="Helper functions for ML course.",
      url="https://github.com/JonasEngstrom/hkrmlcourse",
      author="Jonas Engström",
      author_email="JonasEngstrom@users.noreply.github.com",
      license="MIT",
      install_requires=[
            'yfinance',
            'pandas'
      ]
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src")
      )