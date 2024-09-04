from odoo.tests import common
from odoo.exceptions import ValidationError

class TestMaterial(common.TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['material.supplier'].create({'name': 'Supplier A'})
        self.material = self.env['material.material'].create({
            'material_code': 'M001',
            'material_name': 'Material 1',
            'material_type': 'fabric',
            'material_buy_price': 150,
            'related_supplier_id': self.supplier.id,
        })

    def test_material_creation(self):
        self.assertEqual(self.material.material_code, 'M001')
        self.assertEqual(self.material.material_buy_price, 150)

    def test_material_price_constraint(self):
        with self.assertRaises(ValidationError):
            self.env['material.material'].create({
                'material_code': 'M002',
                'material_name': 'Material 2',
                'material_type': 'jeans',
                'material_buy_price': 50,
                'related_supplier_id': self.supplier.id,
            })

    def test_update_material(self):
        self.material.write({'material_name': 'Updated Material'})
        self.assertEqual(self.material.material_name, 'Updated Material')

    def test_delete_material(self):
        material_id = self.material.id
        self.material.unlink()
        self.assertFalse(self.env['material.material'].browse(material_id).exists())
