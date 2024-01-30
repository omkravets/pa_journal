# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PaJournalRecord(models.Model):
    _name = 'pa_journal.record'
    _description = 'Record'

#    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

    record_date = fields.Datetime(string="Date and time",
                                  required=True,
                                  default=fields.Datetime.now())
    description = fields.Text()

    def _get_employee_id(self):
        """
        method for calculate of employee_id by user_id
        """
        employee_rec = self.env['hr.employee']. \
            search([('user_id', '=', self.env.uid)], limit=1)
        return employee_rec.id

    worker_id = fields.Many2one(string="Worker",
                                comodel_name="hr.employee",
                                ondelete="restrict",
                                required=True,
                                default=_get_employee_id)


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
