from odoo import models, fields, api
from odoo.exceptions import UserError
class BuildingRoom(models.Model):
    _name = 'building.room'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Building Room'

    name = fields.Char(string='Room Name', required=True)
    image = fields.Binary()
    sales_price = fields.Float(string='Sales Price')
    floor = fields.Integer(string='Floor')
    capacity = fields.Integer(string='Capacity')
    building_id = fields.Many2one('building.building', string='Building', required=True)
    product_ids = fields.Many2many(
        'product.template',
        'building_room_product_rel',
        'room_id',
        'product_id',
        string='Products',
        domain="[('s_field', '=', 'available'), ('room_ids', '=', False)]"
    )
    room_type = fields.Selection([
        ('office', 'Office'),
        ('conference', 'Conference Room'),
        ('meeting', 'Meeting Room'),
        ('break', 'Break Room'),
        ('other', 'Other')
    ], string='Room Type', default='office')
    facilities = fields.Text(string='Facilities')

    s_field = fields.Selection([
            ('available', 'Available'),
            ('sold', 'Sold')
        ], string='Status', default='available')

    def action_available(self):
        for x in self:
            x.s_field = 'available'

    def action_sold(self):
        for x in self:
            x.s_field = 'sold'






