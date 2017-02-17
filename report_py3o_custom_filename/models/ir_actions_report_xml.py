# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models
from openerp.addons.mail.models import mail_template


class IrActionsReportXml(models.Model):

    _inherit = 'ir.actions.report.xml'

    @api.multi
    def gen_report_download_filename(self, res_ids, data):
        """Override this function to change the name of the downloaded report
        """
        self.ensure_one()
        if not self.download_filename:
            return super(IrActionsReportXml, self). \
                gen_report_download_filename(res_ids, data)
        objects = self.env[self.model].browse(res_ids)
        return mail_template.mako_template_env \
            .from_string(self.download_filename) \
            .render({
                'objects': objects,
                'o': objects[0],
                'object': objects[0],
                'ext': self.py3o_filetype
            })
