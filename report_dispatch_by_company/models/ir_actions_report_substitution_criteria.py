# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ActionsReportSubstitutionCriteria(models.Model):

    _inherit = 'ir.actions.report.substitution.criteria'

    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.user.company_id,
        ondelete='cascade',
    )
