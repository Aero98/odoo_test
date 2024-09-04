Material
<br />
id: Integer (Primary Key) <br />
material_code: String <br />
material_name: String <br />
material_type: Enum (Fabric, Jeans, Cotton) <br />
material_buy_price: Float <br />
related_supplier_id: Foreign Key (References Supplier) <br />
<br />
Supplier <br />
id: Integer (Primary Key) <br />
name: String  <br />
<br />
Relationships: <br />
A Material has one Supplier. <br />
A Supplier can have many Materials. <br />
