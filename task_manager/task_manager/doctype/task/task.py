# Copyright (c) 2024, Shubham Patil and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class Task(Document):
    def validate(doc):
          if not doc.description:
               frappe.throw("Description is required for the task.")
          if doc.due_date and doc.due_date < frappe.utils.today():
               frappe.throw("Due Date cannot be in the past.") 
    validate_reference_doctype = frappe.get_doc_hooks().setdefault("validate_reference_doctype", {})
    validate_reference_doctype['Task'] = {"assigned_to": ["User"]} 
    pass


