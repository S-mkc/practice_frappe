# Copyright (c) 2024, Raindrop Inc. and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
from frappe.model.document import Document
import frappe

class Property(Document):
	#validates
    def validate(self):
        frappe.throw((f'This is an Error Message to check'))

