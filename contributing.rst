Contributor Guide
=================

The site is organized into galleries, each containing one or more notebooks.
Each gallery is stored in a standalone GitHub repository.
All notebooks within a gallery should share a similar theme
(for example, *Pangeo for Physical Oceanography*) and must use the same
Conda environment.

Galleries are "built" using `binderbot <https://github.com/pangeo-gallery/binderbot>`_.
Binderbot takes all the notebooks in the gallery, executes them inside binder,
and saves the output to a dedicated branch within the repo.
Each gallery contains a configuration file called ``binder-gallery.yaml``,
which specifies the details of the binder configuration.
It also provides a basic description of the gallery contents.

Contributing to an Existing Gallery
-----------------------------------

You can contribute to an existing gallery by either modifying one of the
existing notebooks or adding a new notebook.
Since every gallery is a GitHub repository, you can contribute by
`making a pull request <https://opensource.com/article/19/7/create-pull-request-github>`_.

Creating a New Gallery
----------------------

To create a new gallery, you will need to create a new repo following the
`example gallery template <https://github.com/pangeo-gallery/example-gallery>`_.

- Click the big green button to create a new repository following the template.
- Remove the dummy content and add your content.
- Update the ``binder-gallery.yaml`` configuration file.
- Add a custom ``thumbnail.png``, a 200 x 200 px image which represents the gallery contents.

Now push your changes, e.g.::

    git push origin

At this point, a GitHub Action will execute your notebooks on the binder.
Click the "Actions" button on your repository page or navigate to ``/actions``,
and wait for the build to finish.

You also need to add your repo as a submodule to the Pangeo gallery repo, located at
https://github.com/pangeo-gallery/pangeo-gallery.

- Fork the gallery repo.
- Clone your fork.
- Create a feature branch.
- Add your repository as a submodule, e.g.::

    git submodule add -b binderbot-built \
    "https://github.com/pangeo-gallery/example-gallery.git" \
    repos/pangeo-gallery/example-gallery

- Commit and make a PR to the upstream gallery repo.

Config File Specification
-------------------------

All example galleries must contain a file called ``binder-gallery.yaml``.
An example file is shown below::

  ---
  name: Example Gallery
  description: >-
    An example gallery of notebooks used for debugging the Pangeo Gallery
    infrastructure.
  gallery_repository: pangeo-gallery/pangeo-gallery
  binder_url: "https://binder.pangeo.io"
  binder_repo: pangeo-gallery/default-binder
  binder_ref: master
  binderbot_target_branch: binderbot-built


The fields are defined as follows.

.. list-table:: binder-gallery.yaml
   :widths: 25 75
   :header-rows: 1

   * - Parameter
     - Description
   * - ``name``
     - The heading used when displaying the gallery
   * - ``description``
     - A short paragraph describing the gallery contents
   * - ``gallery_repository``
     - Location of the gallery website repo on GitHub.
       Default ``pangeo-gallery/pangeo-gallery`` should probably not be changed.
   * - ``binder_url``
     - Url for binder service in which to run the notebooks.
   * - ``binder_repo``
     - Github repository which contains the environment configuration.
       (Can be the example repo itself or an external repo.)
   * - ``binder_ref``
     - Branch, tag, or commit within ``binder_repo`` which contains the binder
       environment configuration.
   * - ``binderbot_target_branch``
     - Used by GitHub workflow to determine where to push the output of the
       binderbot built notebooks. Default (``binderbot-built``) should probably
       not be changed.
