# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Report Dispatch By Company',
    'summary': """
        This addon define the company as criteria for report substitution.
        """,
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/multi-company',
    'depends': ['report_dispatch_base'],
    'data': [
        'data/ir_actions_report_dispatch_criteria.xml',
        'views/ir_actions_report.xml',
    ],
}
