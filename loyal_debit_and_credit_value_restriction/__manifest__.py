# -*- coding: utf-8 -*-
{
    'name': "Debit and Credit value restriction",

    'summary': """
       1.Debit and Credit value restriction
       2.stock return restriction""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Loyal It Solutions PVT Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','account','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
