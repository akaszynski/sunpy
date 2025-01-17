.. _dev_guide:
{% if not is_development %}
.. _newcomers:
.. _remote_data:
{% endif %}

*****************
Developer's Guide
*****************

{% if is_development %}

This article describes the guidelines to be followed by developers working on sunpy.
If you are thinking of contributing to sunpy please read the following carefully.

We currently recommend the :ref:`newcomers` as the place to start.
This goes over the basics and has links to useful tutorials on git.

.. toctree::
   :maxdepth: 2

   contents/newcomers
   contents/code_standards
   contents/documentation
   contents/example_gallery
   contents/tests
   contents/pr_review_procedure
   contents/api
   contents/dependencies
   contents/units_quantities
   contents/new_objects
   contents/extending_fido
   contents/maintainer_workflow
   contents/logger
   contents/remote_data
   contents/config
   contents/funding

{%else%}

Please go `here <https://docs.sunpy.org/en/latest/dev_guide/index.html>`__ for our up to date developer's guide.

{%endif%}
