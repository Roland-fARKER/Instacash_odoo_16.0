# -*- coding: utf-8 -*-
# from odoo import http


# class Pic(http.Controller):
#     @http.route('/pic/pic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pic/pic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pic.listing', {
#             'root': '/pic/pic',
#             'objects': http.request.env['pic.pic'].search([]),
#         })

#     @http.route('/pic/pic/objects/<model("pic.pic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pic.object', {
#             'object': obj
#         })
