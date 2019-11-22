.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
Report Py3o Multilang
=====================


This module extends the Py3o Report functionality by letting you specify a rule
to choose the appropriate template to use according to an expected language.

Usage
=====

This module add two new fields on the report definition:

* Alternate lang report file path: This should be a placeholder expression
  that provides the path to an alternate report file to use for a given
  language. The the expression can use the string '{lang}' as placeholder in the path,
  e.g. "folder/my_template_{lang}.odt". If the expression is not provided or can be resolved, the report falls back
  on the main report file path/controller.
* Language:  This should usually be a placeholder expression that provides the appropriate language,
  e.g. "${object.partner_id.lang}.". The 'object' in the expression is on instance of the model on which the
  report applies.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/143/10.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/{project_repo}/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Laurent Mignon <laurent.mignon@acsone.eu>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
