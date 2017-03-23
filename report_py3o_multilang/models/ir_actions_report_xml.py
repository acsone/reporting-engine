# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class IrActionsReportXml(models.Model):
    _inherit = 'ir.actions.report.xml'

    lang = fields.Char(
        'Language',
        help="Optional translation language (ISO code) to use to resolve the "
             "expression provided in the 'Alternate report file path field'"
             "This should usually be a placeholder expression "
             "that provides the appropriate language, e.g. "
             "${object.partner_id.lang}.",
        placeholder="${object.partner_id.lang}")

    py3o_localized_template_fallback = fields.Char(
        'Alternate localized report file path',
        help="This should be a string expression that provides the path "
             "to an alternate report file to use. The string is formatted "
             "with '{lang}' as relacement string in the path, e.g. "
             "'folder/my_template_{lang}.odt'. If the expression is not "
             "provided or can be resolved, the report falls back on the main "
             "report file path/controller.\n The expression is resolved a "
             "first time by providing the iso code as as lang e.g. fr_BE. "
             "If no file is found at the resolved path, The expression is "
             "resolved and second time by using the lang part of the ISO code "
             "e.g. 'fr'."
    )

    @api.constrains('lang', 'py3o_localized_template_fallback')
    def _check_lant_alt_report_rml(self):
        for this in self:
            if not (this.lang and this.py3o_localized_template_fallback):
                raise ValidationError(
                    _("If a value is provided for the language or for the "
                      "alternate localized report file path, you must also "
                      "provide a value for the other one"))
