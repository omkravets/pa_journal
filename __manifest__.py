# -*- coding: utf-8 -*-
{
    'name': "pa_journal",

    'summary': """ Module for journal """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Oleksandr Kravets",
    'e-mail': "701@pa.ua",

    'category': 'Project Management',
    'license': "LGPL-3",
    'version': "15.0.1.0.0",

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'calendar'],

    # always loaded
    'data': [
        'security/pa_journal_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
