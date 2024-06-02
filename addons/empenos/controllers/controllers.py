# -*- coding: utf-8 -*-
# from odoo import http


# class Empenos(http.Controller):
#     @http.route('/empenos/empenos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empenos/empenos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('empenos.listing', {
#             'root': '/empenos/empenos',
#             'objects': http.request.env['empenos.empenos'].search([]),
#         })

#     @http.route('/empenos/empenos/objects/<model("empenos.empenos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empenos.object', {
#             'object': obj
#         })
