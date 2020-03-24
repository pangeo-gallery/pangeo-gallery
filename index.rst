Pangeo Gallery
==============


.. raw:: html

    <div class="row">
       <div class="col-sm-6 col-md-4x">
       {% for repo, repo_data in repos.items() %}
        <div class="thumbnail">

.. image:: {{ repo }}/thumbnail.png
   :target: #

.. raw:: html

         <div class="caption">
          <h3>{{ repo_data.name }}</h3>
          <p> {{ repo_data.description }}
          </p>

.. image:: https://github.com/{{ repo_data.path }}/workflows/Binderbot/badge.svg
   :alt: Binderbot Build Status
   :target: https://github.com/{{ repo_data.path }}/actions?query=workflow%3ABinderbot

.. image:: https://mybinder.org/badge_logo.svg
   :alt: Launch Binder
   :target: {{ repo.binder_url }}/v2/gh/{{ repo.binder_repo }}/master/?urlpath=git-pull?repo=https://github.com/{{ repo_data.path }}

.. toctree::
   :glob:
   :maxdepth: 1

   {{ repo }}/*


.. raw:: html

         </div>
        </div>
       {% endfor %}
      </div>
    </div>
