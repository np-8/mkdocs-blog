
from distutils.core import setup

setup(
    name='mkdocs-blog',
    version='0.1.0',
    author='Andy Oakley',
    author_email='ao@ao.vc',
    packages=['mkdocs_blog'],
    package_data={"": ["rss.xml"]},
    license='LICENSE.txt',
    description='Simple blogging in mkdocs',
    install_requires=['mkdocs', 'jinja2'],

    entry_points={
        'mkdocs.plugins': [
            'blog = mkdocs_blog.blog:Blog',
        ]
    }
)
