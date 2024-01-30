# -*- coding: utf-8 -*-
# from odoo import http


# class PaJournal(http.Controller):
#     @http.route('/pa_journal/pa_journal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pa_journal/pa_journal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pa_journal.listing', {
#             'root': '/pa_journal/pa_journal',
#             'objects': http.request.env['pa_journal.pa_journal'].search([]),
#         })

#     @http.route('/pa_journal/pa_journal/objects/<model("pa_journal.pa_journal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pa_journal.object', {
#             'object': obj
#         })
