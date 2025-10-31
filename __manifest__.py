{
'name': 'Odoo SaaS Demo - Project Image & Proof Approval',
'version': '1.0.0',
'category': 'Project',
'summary': 'Adds project header image, public proof-approval links and simple kanban config',
'author': 'YourName',
'depends': ['project', 'website', 'mail'],
'data': [
'security/ir.model.access.csv',
'views.xml',
],
'installable': True,
'application': False,
}
