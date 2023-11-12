

from setuptools import setup, find_packages

name = 'FastOMA'
__version__ = None
with open('{:s}/__init__.py'.format(name), 'rt') as fp:
    for line in fp:
        if line.startswith('__version__'):
            exec(line.rstrip())

# TODO
requirements = ['biopython', 'ete3', 'omamer>=2.0.0', 'nextflow', 'pyparsing' , 'DendroPy', 'future', 'lxml','pyham']

desc = 'FastOM - a package to infer orthology information '

setup(
    name=name,
    version=__version__,
    author='',
    email='',
    url='https://github.com/DessimozLab/gethog3',
    description=desc,
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6",
    license='MIT',
    entry_points={
        'console_scripts': [
            "check-fastoma-input=FastOMA.check_fastoma_input:check_fastoma_input",
            "infer-roothogs=FastOMA.infer_roothogs:infer_roothogs",
            "batch-roothogs=FastOMA.batch_roothogs:batch_roothogs",
            "infer-subhogs=FastOMA.infer_subhogs:infer_subhogs",
            "collect-subhogs=FastOMA.collect_subhogs:collect_subhogs",
        ]
    },
)
