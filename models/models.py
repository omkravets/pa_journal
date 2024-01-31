# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PaJournalRecord(models.Model):
    _name = 'pa_journal.record'
    _description = 'Record'

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

    equipment = fields.Many2one(string="Equipment",
                                comodel_name="pa_journal.equipment",
                                ondelete="restrict",
                                required=True)

    allOK = fields.Selection([("yes", _("Yes")),
                              ("no", _("No"))],
                             string="All OK",
                             required=True)

    name = fields.Char(string="Journal record name", compute="_compute_record_name")

    @api.depends("worker_id", "equipment", "record_date")
    def _compute_record_name(self):
        """
        method for calculate name of the record
        """
        for rec in self:
            rec.name = "%s - %s ( %s )" % \
                       (rec.worker_id.name, rec.equipment.name, rec.record_date)

    @api.onchange("equipment")
    def _compute_parameters_list(self):
        """
        method for fill description field
        """
        for rec in self:
            if type(rec.description) != bool:
                if len(rec.description) < 5:
                    rec.description = rec.equipment.parameters
            else:
                rec.description = rec.equipment.parameters


class PaJournalEquipment(models.Model):
    _name = 'pa_journal.equipment'
    _description = 'Equipment'

    name = fields.Char(string="Equipment name",
                       required=True)

    productionDate = fields.Date(string="Production date",
                                 required=False)

    parameters = fields.Text()

