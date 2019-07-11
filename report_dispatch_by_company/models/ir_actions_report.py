# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class IrActionReport(models.Model):

    _inherit = 'ir.actions.report'

    is_company_id_a_substitution_criteria = fields.Boolean(
        compute="_compute_is_company_id_a_substitution_criteria"
    )

    @api.multi
    def _compute_is_company_id_a_substitution_criteria(self):
        for rec in self:
            if rec.model:
                model = self.env[self.model]
                criteria = self.env[
                    'ir.actions.report.dispatch.criteria'
                ].search([('field_name', '=', 'is_company')])
                if criteria:
                    rec.is_company_id_a_substitution_criteria = \
                        criteria._check_criteria_in_model(model)
