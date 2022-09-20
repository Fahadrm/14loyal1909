# -*- coding: utf-8 -*-
{
    'name': "schedule_activities",

    'summary': """
       schedule_activities""",

    'description': """
       schedule_activities
    """,

    'author': "Loyal It Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'calendar'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/create_button.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
