# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api, _
from odoo.addons.base.models.ir_model import FIELD_TYPES
from odoo.exceptions import UserError


class IrActionsReportDispatchCriteria(models.Model):

    _name = 'ir.actions.report.dispatch.criteria'
    _description = 'Actions Report Dispatch Criteria'

    name = fields.Char(required=True)
    field_name = fields.Char(required=True)
    ttype = fields.Selection(
        selection=FIELD_TYPES, string='Type', required=True
    )
    model = fields.Char()

    _sql_constraints = [
        ('unique_name', 'unique(field_name)', 'This criteria exist already')
    ]

    @api.model
    def _get_criteria_list(self):
        return self._get_criteria_fields()

    @api.multi
    def _check_criteria_in_model(self, model):
        self.ensure_one()
        if (
            self.field_name in model._fields
            and model._fields[self.field_name].ttype == self.ttype
        ):
            if (
                self.ttype in ('many2one', 'many2many', 'one2many')
                and model._fields.model != self.model
            ):
                return False
            return True
        return False

    @api.constrains('ttype', 'model')
    def _check_model_for_relational_fields(self):
        for rec in self:
            if (
                rec.ttype in ('many2one', 'many2many', 'one2many')
                and not rec.model
            ):
                raise UserError(_('Model is required for relational criteria'))
        return True
