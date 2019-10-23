# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': "Base report xlsx",

    'summary': "Base module to create xlsx report",
    'author': 'ACSONE SA/NV,'
              'Creu Blanca,'
              'Odoo Community Association (OCA)',
    'website': "https://github.com/oca/reporting-engine",
    'category': 'Reporting',
    'version': '11.0.1.0.6',
    'license': 'AGPL-3',
    'external_dependencies': {
        'python': [
            'xlsxwriter',
            'xlrd',
        ],
    },
    'depends': [
        'base', 'web',
    ],
    'demo': [
        'demo/report.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/header_footer.xml',
        'views/ir_report.xml',
        'views/webclient_templates.xml',
    ],
    'installable': True,
}
