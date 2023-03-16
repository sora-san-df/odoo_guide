{
    'name': "My State Module",
    'version': '1.0',
    'depends': ['base'],
    'author': "Diego Fernando M",
    'category': 'Category',
    'description': """
    Description text
    """,

    
     # add the property 'application' so my module can be considered a full app in odoo
    'application': True,
    'installable': True,

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/list_views.xml',
        'views/form_views.xml',
        'views/kanban_views.xml',
        'views/search_views.xml',
        'views/estate_property_types_views.xml',
        'views/users_views_iherited.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        
    ],

}