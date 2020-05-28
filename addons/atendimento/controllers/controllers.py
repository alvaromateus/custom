# -*- coding: utf-8 -*-
from openerp import http

# class Assistido(http.Controller):
#     @http.route('/assistido/assistido/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assistido/assistido/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('assistido.listing', {
#             'root': '/assistido/assistido',
#             'objects': http.request.env['assistido.assistido'].search([]),
#         })

#     @http.route('/assistido/assistido/objects/<model("assistido.assistido"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assistido.object', {
#             'object': obj
#         })


