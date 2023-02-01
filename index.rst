Pangeo Gallery
==============

Welcome to the Pangeo Gallery website. This site allows you to browse different
Pangeo use cases. The site is organized into galleries, listed below,
containing one or more notebooks.
Each gallery is hosted in a standalone GitHub repository.
If you're interested in contributing a new gallery, please see the
:doc:`contributing`.

Note that some of this content has migrated over to the 
`Project Pythia Cookbook Gallery <https://cookbooks.projectpythia.org>`_ 
which is under active develpment.

.. raw:: html

    <div class="row">
      {% for repo, repo_data in repos.items() %}
      {% set repo_only = repo.split('/')[-1] %}
       <div class="col-xs-12 col-sm-6 col-md-4">
        <div class="thumbnail">

.. image:: {{ repo }}/thumbnail.png
   :target: {{ repo }}

.. raw:: html


         <div class="caption">
          <h2>{{ repo_data.name }}</h2>
          <!-- <a class="btn btn-primary" href="https://github.com/{{ repo_data.path }}" role="button"><i class="fa fa-github fa-lg"></i> &nbsp; {{ repo_data.path }}</a> -->
          <p> {{ repo_data.description | truncate(255, False) }}
          </p>
          <div class="badges">
            <img alt="License" src="https://img.shields.io/github/license/{{ repo_data.path }}?style=flat-square" />
            <a href="https://github.com/{{ repo_data.path }}"><img alt="GitHub" src="https://img.shields.io/github/last-commit/{{ repo_data.path }}/{{ repo_data.binderbot_target_branch }}?logo=github&style=flat-square" /></a>
            <a href="https://github.com/{{ repo_data.path }}/actions?query=workflow%3ABinderbot"><img alt="BinderBot" src="https://github.com/{{ repo_data.path }}/workflows/Binderbot/badge.svg?logo=github&style=flat-square" /></a>
            <a href="{{ repo_data.binder_url }}/v2/gh/{{ repo_data.binder_repo }}/{{ repo_data.binder_ref }}?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252F{{ repo_data.path | urlencode }}%26urlpath%3Dlab%252Ftree%252F{{ repo_only | urlencode }}"><img alt="Launch Binder" src="https://mybinder.org/badge_logo.svg?style=flat-square" /></a>
          </div>
         </div>
        </div>
       </div>
      {% endfor %}
    </div>




.. toctree::
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   contributing
   {% for repo, repo_data in repos.items() %}
   {{ repo }}/index
   {% endfor %}
