from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    @http.route('/api/materials', type='json', auth='public', methods=['GET'])
    def get_materials(self, material_type=None):
        domain = []
        if material_type:
            domain = [('material_type', '=', material_type)]
        materials = request.env['material.material'].search(domain)
        materials_list = []
        for material in materials:
            materials_list.append({
                'material_code': material.material_code,
                'material_name': material.material_name,
                'material_type': material.material_type,
                'material_buy_price': material.material_buy_price,
                'related_supplier': material.related_supplier_id.name,
            })
        return materials_list

    @http.route('/api/material/<int:material_id>', type='json', auth='public', methods=['GET'])
    def get_material(self, material_id):
        material = request.env['material.material'].browse(material_id)
        return {
            'material_code': material.material_code,
            'material_name': material.material_name,
            'material_type': material.material_type,
            'material_buy_price': material.material_buy_price,
            'related_supplier': material.related_supplier_id.name,
        }

    @http.route('/api/material', type='json', auth='public', methods=['POST'])
    def create_material(self, **kwargs):
        new_material = request.env['material.material'].create({
            'material_code': kwargs.get('material_code'),
            'material_name': kwargs.get('material_name'),
            'material_type': kwargs.get('material_type'),
            'material_buy_price': kwargs.get('material_buy_price'),
            'related_supplier_id': kwargs.get('related_supplier_id'),
        })
        return {
            'id': new_material.id,
            'message': 'Material created successfully!'
        }

    @http.route('/api/material/<int:material_id>', type='json', auth='public', methods=['PUT'])
    def update_material(self, material_id, **kwargs):
        material = request.env['material.material'].browse(material_id)
        material.write({
            'material_code': kwargs.get('material_code'),
            'material_name': kwargs.get('material_name'),
            'material_type': kwargs.get('material_type'),
            'material_buy_price': kwargs.get('material_buy_price'),
            'related_supplier_id': kwargs.get('related_supplier_id'),
        })
        return {
            'message': 'Material updated successfully!'
        }

    @http.route('/api/material/<int:material_id>', type='json', auth='public', methods=['DELETE'])
    def delete_material(self, material_id):
        material = request.env['material.material'].browse(material_id)
        material.unlink()
        return {
            'message': 'Material deleted successfully!'
        }
