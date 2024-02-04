// Copyright (c) 2024, Raindrop Inc. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Property", {
// 	refresh(frm) {
    setup: function(frm){
        // frm.add_custom_button('Hello from Frappe', () => {
        //     // frappe.set_route('Form', frm.doc.reference_type, frm.doc.reference_name);
        // })
    },
    refresh: function(frm) {
        frm.add_custom_button('send for approval', () => {
            // frappe.set_route('Form', frm.doc.reference_type, frm.doc.reference_name);
        }, "Action");
        frm.add_custom_button('Approve', () => {
            // frappe.set_route('Form', frm.doc.reference_type, frm.doc.reference_name);
        }, "Action");
        frm.add_custom_button('Reject', () => {
            // frappe.set_route('Form', frm.doc.reference_type, frm.doc.reference_name);
        }, "Action");
    }

// 	},
});
