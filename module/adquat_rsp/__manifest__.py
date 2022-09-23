# -*- coding: utf-8 -*-
{
    'name': "Adquat RSP",

    'summary': """
        Personalisation diverse pour rsp""",

    'description': """
        Personalisation diverse pour rsp
    """,

    'author': "Adquat",
    'website': "http://www.adquat.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'project',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'data/ir.model.access.csv',
        'views/mail_template.xml',
        'views/fdi.xml',
        'views/sav.xml',
        'views/project.xml',
    ],
    'license': 'LGPL-3',
    # only loaded in demonstration mode
    'demo': [
    ],
}