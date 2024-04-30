from setuptools import setup

setup(
    name='plotting-house-style',
    version='0.1.0',    
    description='A python package with the plotting house style of Julia Wasala.',
    url='https://github.com/JuliaWasala/plotting-house-style',
    author='Julia Wasala',
    author_email='j.wasala@liacs.leidenuniv.nl',
    license='MIT',
    packages=['plotting_house_style'],
    install_requires=['matplotlib'                     
                      ],
    extras_require={
        "map": ["geopandas", "shapely"],
    },

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
    ],
)