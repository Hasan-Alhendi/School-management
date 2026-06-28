from setuptools import setup, find_packages

setup(
    name="school_management",
    version="0.0.1",
    description="Custom ERPNext school management app",
    author="Hasan Alhendi",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
