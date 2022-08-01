{
    'name': "Hospital Management",
    'version': '1.0.0',
    'author': "Adham Mohamed",
    'category': 'Hospital',
    'description': """Hospital Management System""",
    'sequence': -100,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml'
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
