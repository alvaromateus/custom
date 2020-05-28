# -*- coding: utf-8 -*-
{
    'name': "atendimento",

    'summary': """
        Módulo de atendimentos.""",

    'description': """
        Controle de atendimentos da Defensoria Pública do Paraná.
    """,

    'author': "Alvaro Mateus Santana",
    'website': "http://www.defensoriapublica.pr.def.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
#        'security/ir.model.access.csv',
        'views/views.xml',
	'views/assistido.xml',
	'views/membro_familia.xml',
	'views/endereco.xml',
	'views/telefone.xml',
	'views/solicitante.xml',
	'views/programa_social.xml',
	'views/atendimento.xml',
	'views/antigo.xml',
	'views/sede.xml',
	'views/defensor.xml',
	'views/diligencia.xml',
	'views/atendimento_telefonico.xml',

 #       'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
