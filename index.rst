Pangeo Gallery
==============


{% for repo, repo_data in repos.items() %}
{{ repo_data.name }}
--------------------

{{ repo_data.description }}

.. toctree::
   :glob:
   :maxdepth: 1

   {{ repo }}/*
   
{% endfor %}
