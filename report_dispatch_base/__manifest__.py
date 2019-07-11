# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Base Report Dispatch',
    'summary': """
        This addon give the possibility to dispatch one action report to 
        different reports based on some criteria.
        We consider one basic criteria which is the company to be able to 
        configure different report for the same object in each company.
        This module can be inherited to add new criteria.
        """,
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/multi-company',
    'depends': ['base'],
    'data': [
        'security/ir_actions_report_dispatch_criteria.xml',
        'security/ir_actions_report_substitution_criteria.xml',
        'views/ir_actions_report.xml',
    ],
}
