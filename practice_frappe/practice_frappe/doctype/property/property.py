# Copyright (c) 2024, Raindrop Inc. and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
from frappe.model.document import Document
import frappe

# @frappe.whitelist()
class Property(Document):

	#validates
    # def validate(self):

    #     frappe.throw((f'This is an Error Message to check <b>{self.name}<b>'))
        # if(self.property_type=="Flat"):
        #     for amenity in self.amenities:
        #         if(amenity.amenity=="Outdoor Kitchen"):
        #             frappe.throw((f'For property <b>{self.name}</b> the amenity type is <b>{amenity.amenity}</b> tye again'))
    def after_insert(self):
        frappe.msgprint((f'Document {self.name} inserted successfully'));






