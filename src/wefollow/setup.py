from setuptools import setup, find_packages

version = '0.1'

long_description = """
Wefollow
"""


setup(name='wefollow',
      version=version,
      description="Wefollow",
      long_description=long_description,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        ], 
      author="Zojax Group",
      author_email="developers@zojax.com",
      url="http://zojax.com",
      license="GPL",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'webapp2',
                        'zope.interface'
                        ],
      )
