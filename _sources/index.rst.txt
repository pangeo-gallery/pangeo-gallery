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
