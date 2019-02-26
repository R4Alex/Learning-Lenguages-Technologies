# -*- coding: utf-8 -*-
from odoo import http

# class /workspace/odootycoon(http.Controller):
#     @http.route('//workspace/odootycoon//workspace/odootycoon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//workspace/odootycoon//workspace/odootycoon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/workspace/odootycoon.listing', {
#             'root': '//workspace/odootycoon//workspace/odootycoon',
#             'objects': http.request.env['/workspace/odootycoon./workspace/odootycoon'].search([]),
#         })

#     @http.route('//workspace/odootycoon//workspace/odootycoon/objects/<model("/workspace/odootycoon./workspace/odootycoon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/workspace/odootycoon.object', {
#             'object': obj
#         })