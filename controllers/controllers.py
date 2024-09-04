from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError
import json

class MaterialController(http.Controller):

    @http.route('/api/material/<int:material_id>', type='json', auth='public', methods=['GET'])
    def get_material(self, material_id):
        parameters = json.loads(request.httprequest.data)
        material_id = parameters.get('id')
        material = request.env['material.material'].browse(material_id)
        return {
            'material_code': material.material_code,
            'material_name': material.material_name,
            'material_type': material.material_type,
            'material_buy_price': material.material_buy_price,
            'related_supplier': material.related_supplier_id.name,
        }

    @http.route('/api/material', type='json', auth='public', methods=['POST'], csrf=False)
    def create_material(self, **kwargs):
        parameters = json.loads(request.httprequest.data)
        # open('/opt/odoo/logs/create_material.log', 'a+').write('\n' + str(parameters))
        new_material = request.env['material.material'].create({
            'material_code': parameters.get('material_code'),
            'material_name': parameters.get('material_name'),
            'material_type': parameters.get('material_type'),
            'material_buy_price': parameters.get('material_buy_price'),
            'related_supplier_id': parameters.get('related_supplier_id'),
        })
        return {
            'id': new_material.id,
            'message': 'Material created successfully!'
        }

    @http.route('/api/material/<int:material_id>', type='json', auth='public', methods=['PUT'])
    def update_material(self, material_id, **kwargs):

        parameters = json.loads(request.httprequest.data)
        material = request.env['material.material'].browse(material_id)
        material.write({
            'material_code': parameters.get('material_code'),
            'material_name': parameters.get('material_name'),
            'material_type': parameters.get('material_type'),
            'material_buy_price': parameters.get('material_buy_price'),
            'related_supplier_id': parameters.get('related_supplier_id'),
        })
        return {
            'message': 'Material updated successfully!'
        }

    @http.route('/api/material/<int:material_id>', type='json', auth='public', methods=['DELETE'])
    def delete_material(self, material_id):
        parameters = json.loads(request.httprequest.data)
        material_id = parameters.get('id')
        open('/opt/odoo/logs/create_material.log', 'a+').write('\n' + str(parameters))
        material = request.env['material.material'].browse(material_id)
        material.unlink()
        return {
            'message': 'Material deleted successfully!'
        }
