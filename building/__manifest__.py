# -*- coding: utf-8 -*-
{
    'name': "building",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website_sale','mail','account','website_google_map'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/building.xml',
        'views/product.xml',
        'views/inventory.xml',
        'views/booking.xml',
        'views/room.xml',
        'report/reports.xml',
        # 'views/style_report.xml',
        # 'views/template_report.xml',
        'views/room.xml',
        'views/tenant.xml',
        'views/report.xml',
        'wizard/wizard.xml',
        'data/sequence.xml',
        # 'security/security.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}

