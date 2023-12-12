# from odoo import models, fields, api, tools
#
#
# class BuildingDetails(models.Model):
#     _name = 'building.building'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#     _description = 'view product Master here'
#     _rec_name = 'bld_name'
#
#     # street1 = fields.Char()
#     # street2 = fields.Char()
#     # country = fields.Many2one('res.country', required=True)
#     # city = fields.Char(required=True)
#     # state = fields.Many2one('res.country.state', required=True)
#     # zip = fields.Char()
#     @api.model
#     def get_default_company_address(self):
#         """
#         Fetch the company's address from Odoo's settings and set it as the default value.
#         """
#         company = self.env.company
#
#         return {
#             'country': company.country_id.id,
#             'street1': company.street,
#             'street2': company.street2,
#             'city': company.city,
#             'state': company.state_id.id,
#             'zip': company.zip,
#         }
#     image = fields.Binary()
#     bld_name = fields.Char(string='Name', required=True)
#     bld_code = fields.Char(string="Building Code")
#     upld_image = fields.Binary()
#     comment = fields.Text()
#     attachment = fields.Binary(string='Attachment', attachment=True)
#     floor_plan = fields.Binary(string='Floor Plan', attachment=True)
#     street1 = fields.Char(default=get_default_company_address)
#     street2 = fields.Char(default=get_default_company_address)
#     country = fields.Many2one('res.country', required=True, default=get_default_company_address)
#     city = fields.Char(required=True, default=get_default_company_address)
#     state = fields.Many2one('res.country.state', required=True, default=get_default_company_address)
#     zip = fields.Char(default=get_default_company_address)


from odoo import models, fields, api

class BuildingDetails(models.Model):
    _name = 'building.building'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'view product Master here'
    _rec_name = 'bld_name'

    image = fields.Binary()
    bld_name = fields.Char(string='Name', required=True)
    bld_code = fields.Char(string="Building Code")
    upld_image = fields.Binary()
    product_template_image_ids = fields.Many2many('product.image', string='')
    comment = fields.Text()
    # attachment = fields.Binary(string='Attachment', attachment=True)
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')
    floor_plan = fields.Binary(string='Floor Plan', attachment=True)
    street1 = fields.Char()
    street2 = fields.Char()
    # country = fields.Many2one('res.country', required=True)
    country = fields.Many2one('res.country', required=True, default=lambda self: self._default_country())
    city = fields.Char(required=True)
    state = fields.Many2one('res.country.state', required=True, default=lambda self: self._default_state())
    zip = fields.Char()
    # latitude = fields.Float(string='Latitude')
    # longitude = fields.Float(string='Longitude')
    # gmap = fields.Html(compute='_compute_gmap', string='Map', store=False)

    # def _compute_gmap(self):
    #     for record in self:
    #         record.gmap = """
    #                 <iframe width="600" height="450" frameborder="0" style="border:0"
    #                     src="https://maps.google.com/maps?q=%s,%s&hl=es;z=14&amp;output=embed">
    #                 </iframe>
    #             """ % (record.latitude, record.longitude)

    # latitude = fields.Float(string="Latitude")
    # longitude = fields.Float(string="Longitude")

    # def open_google_maps(self):
    #     # Customize the URL as needed
    #     google_maps_url = 'https://www.google.com/maps'
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': google_maps_url,
    #         'target': 'new',
    #     }

    @api.model
    def _default_country(self):
        country_id = self.env['res.country'].search([('name', '=', 'India')], limit=1)
        return country_id

    @api.model
    def _default_state(self):
        state_id = self.env['res.country.state'].search([('name', '=', 'Kerala'), ('country_id.name', '=', 'India')],limit=1)
        return state_id
