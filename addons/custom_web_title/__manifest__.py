# __manifest__.py

{
    'name': 'Custom Web Title',
    'version': '1.0',
    'summary': 'Customize the title of the web pages',
    'category': 'Tools',
    'author': 'Tu Nombre',
    'website': 'https://www.tuwebsite.com',
    'depends': ['web','base'],
    'data': [
        'views/web_templates.xml',
    ],
    'installable': True,
    'application': False,
}