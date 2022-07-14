# -*- coding: utf-8 -*-
# from odoo import http


# class CrmPortal(http.Controller):
#     @http.route('/crm_portal/crm_portal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_portal/crm_portal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_portal.listing', {
#             'root': '/crm_portal/crm_portal',
#             'objects': http.request.env['crm_portal.crm_portal'].search([]),
#         })

#     @http.route('/crm_portal/crm_portal/objects/<model("crm_portal.crm_portal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_portal.object', {
#             'object': obj
#         })
