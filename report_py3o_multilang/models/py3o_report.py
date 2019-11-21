# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import api, models

logger = logging.getLogger(__name__)


class Py3oReport(models.TransientModel):

    _inherit = "py3o.report"

    @api.multi
    def get_template_for_lang(self, model_instance):
        self.ensure_one()
        report_xml = self.ir_actions_report_xml_id
        lang = self.env["mail.template"].render_template(
            report_xml.lang, report_xml.model, model_instance.id
        )
        if lang:
            tmpl_path = report_xml.py3o_localized_template_fallback.format(
                lang=lang
            )
            tmpl_file = self._get_template_from_path(tmpl_path)
            if not tmpl_file:
                logger.debug("Template not found at %s", tmpl_path)
                lang = "_" in lang and lang.split("_")[0] or ""
                tmpl_path = report_xml.py3o_localized_template_fallback.format(
                    lang=lang
                )
                tmpl_file = self._get_template_from_path(tmpl_path)
            if not tmpl_file:
                logger.debug("Template not found at %s", tmpl_path)
            if tmpl_file:
                return tmpl_file
        return super(Py3oReport, self)._get_template_fallback(model_instance)

    @api.multi
    def _get_template_fallback(self, model_instance):
        """
        Return the template referenced in the report definition
        :return:
        """
        self.ensure_one()
        report_xml = self.ir_actions_report_xml_id
        if report_xml.lang:
            return self.get_template_for_lang(model_instance)
        return super(Py3oReport, self)._get_template_fallback()
