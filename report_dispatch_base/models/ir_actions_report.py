# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class IrActionReport(models.Model):

    _inherit = 'ir.actions.report'

    action_report_substitution_criteria_ids = fields.One2many(
        comodel_name="ir.actions.report.substitution.criteria",
        inverse_name="action_report_id",
        string="Substitution Criteria",
    )

    @api.multi
    def _get_substitution_report_domain(self, model, active_ids):
        """
        get a domain on ir.actions.report.substitution.criteria model
        :param model: action report model
        :param active_ids: records on which the report is applied
        :return: domain
        """
        self.ensure_one()
        # we get all dispatch criteria defined in the system
        criteria_list = self.env[
            'ir.actions.report.dispatch.criteria'
        ]._get_criteria_list()

        domain = [('action_report_id', '=', self.id)]
        model = self.env[model]
        records = model.browse(active_ids)

        for criteria in criteria_list:
            criteria_field = criteria.field_name
            criteria_name = criteria.name
            criteria_type = criteria.ttype
            criteria_model = criteria.model
            # We consider the substitution criteria in the domain the active
            # model has a field with the same type
            if criteria._check_criteria_in_model(model):
                criteria_value = records.mapped(criteria_field)
                if len(criteria_value) > 1:
                    raise UserError(
                        _(
                            "Report substitution: You can't mix values for "
                            "criteria %s "
                        )
                        % criteria_name
                    )
                elif len(criteria_value) == 0:
                    criteria_value = False

                if not criteria_model:
                    domain.append((criteria_field, '=', criteria_value))
                else:
                    if criteria_type == 'many2one':
                        domain.append(
                            (
                                criteria_field,
                                '=',
                                criteria_value.id
                                if criteria_value
                                else criteria_value,
                            )
                        )
                    else:
                        domain.append(
                            (
                                criteria_field,
                                'in',
                                criteria_value.ids
                                if criteria_value
                                else criteria_value,
                            )
                        )
        return domain

    @api.multi
    def _get_substitution_report(self, model, active_ids):
        domain = self._get_substitution_report_domain(model, active_ids)
        substitution_report_criteria = self.env[
            'ir.actions.report.substitution.criteria'
        ].search(domain, limit=1)
        if substitution_report_criteria:
            return substitution_report_criteria.substitution_action_report_id
        return False

    @api.noguess
    def report_action(self, docids, data=None, config=True):
        res = super(IrActionReport, self).report_action(docids, data, config)
        active_ids = res['context']['active_ids']
        if active_ids:
            substitution_report = self._get_substitution_report(
                self.model, active_ids
            )
        if substitution_report:
            res.update(
                {
                    'report_name': substitution_report.report_name,
                    'report_type': substitution_report.report_type,
                    'report_file': substitution_report.report_file,
                    'name': substitution_report.name,
                }
            )
        return res
