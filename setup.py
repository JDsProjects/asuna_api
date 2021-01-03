from setuptools import setup
setup(
  name = 'asuna_api',
  packages = ['asuna_api'],
  version = '0.1', 
  license='MIT', 
  description = 'An async python wrapper for the asuna api',
  author = 'JDJGIncOfficial',
  author_email = 'jdjgbot@gmail.com',
  url = 'https://github.com/JDJGInc/asuna_api',
  download_url = 'https://github.com/JDJGInc/asuna_api/archive/0.0.02.tar.gz',
  keywords = ['wrapper', 'api', 'random'],
  install_requires=['aiohttp','yarl'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
