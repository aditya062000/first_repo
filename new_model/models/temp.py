from odoo import models, api, fields

class SecondModel(models.Model):
    _name= 'second.model'
    _rec_name = 'name'
    _description = 'Second Model'

    name = fields.Char(string = "Name")
    age = fields.Integer(string = "Age")
    dob = fields.Date(string = "Date of Birth")
    address = fields.Text()
    cat_id = fields.Many2one('practice.demo', string='cat')
    bat_ids = fields.Many2many('practice.demo', string='bat')
    file = fields.Binary()






