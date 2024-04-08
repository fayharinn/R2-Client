from setuptools import setup, find_packages

setup(
    name='r2client',
    version='0.2',
    packages=find_packages(),
    description='A lightweight framework to manage your R2 bucket.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',  # Specify the content type as Markdown
    url='https://github.com/fayharinn/R2-Client',
    author='Younes Bensitel',
    author_email='younes@fayhe.fr',
    license='MIT',
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)
