from odoo import models, fields, api



class ReportDetails(models.TransientModel):
    _name = 'building.report'
    _description = 'wizard'

    room = fields.Selection([('available','Available'),('booked','Booked')],string='Room')
    product = fields.Selection([('available','Available'),('booked','Booked')],string='Product')

    def Print_report(self):
        room_data = False
        product_data = False
        room_names = []  # List to store room names
        room_statuses = []  # List to store room statuses

        if self.room == 'available':
            room_data = self.env['building.room'].search([('s_field', '=', 'available')])

            for room in room_data:
                room_names.append(room.name)
                room_statuses.append(room.s_field)

        if self.product == 'available':
            product_data = self.env['product.template'].search([('s_field', '=', 'available')])

        building_material = self.env.ref('building.action_report_building_wizard')

        if building_material:
            report_id = building_material.id
            printer = building_material.default_print_option
            rep_name = building_material.report_name

            result = {
                'type': 'ir.actions.report',
                'id': report_id,
                'report_type': 'qweb-pdf',
                'binding_type': 'report',
                'attachment': "",
                'print_report_name': "(object._get_report_base_filename())",
                'report_file': 'report_building_wizard',
                'report_name': rep_name,
                'default_print_option': printer,
                'multi': 'false',
                'binding_view_types': 'list,form',
                'model': 'building.report',
                'xml_id': 'building.action_report_building_wizard',
                'context': {
                    'active_id': False,
                    'room_data': room_data or [],
                    'product_data': product_data or [],
                    'room_names': room_names,  # Pass room names to the report context
                    'room_statuses': room_statuses  # Pass room statuses to the report context
                },
            }

            return result
#     def Print_report(self):
#
#         store1 = {
#             'ids': self.ids,
#             'model': self._name,
#             'form': {'room': self.room,
#                      }, }
#         return self.env.ref('building.building_room_report').report_action(self, data=store1)
#
#
# class service_abs(models.AbstractModel):
#     _name = 'report.building.building_room_report_template'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         room = data['form']['room']
#         template_id = False
#
#         if room == 'available':
#             filter_condition = "building_room.s_field = 'available'"
#         elif room == 'booked':
#             filter_condition = "building_room.s_field = 'sold'"
#             template_id = 'building.building_booked_room_report_template'
#         else:
#             filter_condition = "1 = 1"
#             template_id = 'building.building_room_report_template'
#
#         qry = f"""SELECT name, room_type, s_field, floor, capacity
#                                  FROM building_room
#                                  WHERE {filter_condition}"""
#         print(qry)
#
#         docss = []
#         self.env.cr.execute(qry)
#         for d in self.env.cr.dictfetchall():
#             docss.append({
#                 'name': d['name'],
#                 'field_r': d['s_field'],
#                 'number': d['room_type'],
#                 'floor': d['floor'],
#                 'capacity': d['capacity'],
#             })
#
#         return {
#
#             'res_id': 1,
#             'res_model': 'report.report',
#             'doc_ids': data['ids'],
#             'doc_model': data['model'],
#             'room': room,
#             'data': docss,
#             'paperformat': self.env.ref('building.room_report'),
#             'template_id': template_id,
#
#
#         }

    def Cancel(self):
            return