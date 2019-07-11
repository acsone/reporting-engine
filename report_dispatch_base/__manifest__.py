# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Base Report Dispatch',
    'summary': """
        This addon give the possibility to dispatch one action report to 
        different reports based on some criteria.
        """,
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/acsone/reporting-engine',
    'depends': ['base'],
    'data': [
        'security/ir_actions_report_dispatch_criteria.xml',
        'security/ir_actions_report_substitution_criteria.xml',
        'views/ir_actions_report.xml',
    ],
}
