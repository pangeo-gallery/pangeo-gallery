from glob import glob
import os

template = """
{% set repo_data = repos[repo] %}
{% set repo_only = repo.split('/')[-1] %}

{{ repo_data.name }}
==================================================

.. raw:: html

    <pre><i class="fa fa-github fa-lg"></i> <a href="https://github.com/{{ repo_data.path }}">{{ repo_data.path }}</a></pre>

.. raw:: html

      <div class="badges">
        <img alt="License" src="https://img.shields.io/github/license/{{ repo_data.path }}?style=flat-square" />
        <a href="https://github.com/{{ repo_data.path }}"><img alt="GitHub" src="https://img.shields.io/github/last-commit/{{ repo_data.path }}/{{ repo_data.binderbot_target_branch }}?logo=github&style=flat-square" /></a>
        <a href="https://github.com/{{ repo_data.path }}/actions?query=workflow%3ABinderbot"><img alt="BinderBot" src="https://github.com/{{ repo_data.path }}/workflows/Binderbot/badge.svg?logo=github&style=flat-square" /></a>
        <a href="{{ repo_data.binder_url }}/v2/gh/{{ repo_data.binder_repo }}/{{ repo_data.binder_ref }}?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252F{{ repo_data.path | urlencode }}%26urlpath%3Dlab%252Ftree%252F{{ repo_only | urlencode }}"><img alt="Launch Binder" src="https://mybinder.org/badge_logo.svg?style=flat-square" /></a>
      </div>

Thumbnail Image
---------------

.. image:: thumbnail.png
   :alt: Thumbnail

Description
-----------

{{ repo_data.description }}

Notebooks
---------

.. toctree::
   :glob:
   :maxdepth: 1
   :titlesonly:

   **
"""

def write_template(dirname):
    with open(os.path.join(dirname, 'index.rst'), mode='w') as f:

        f.write(f"{{% set repo = '{dirname}' %}}")
        f.write(template)


def main():
    for path in glob('repos/*/*'):
        write_template(path)

if __name__ == "__main__":
    # execute only if run as a script
    main()
