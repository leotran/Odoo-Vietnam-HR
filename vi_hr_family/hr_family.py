# -*- coding: utf-8 -*-
##############################################################################
#
#    @package tvtma_hr_family HR Employee Family for OpenERP 7.0
#    @copyright Copyright (C) 2013 T.V.T Marine Automation (aka TVTMA). All rights reserved.#
#    @license http://www.gnu.org/licenses GNU Affero General Public License version 3 or later; see LICENSE.txt
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv

class hr_family(osv.osv):
    _name = 'vi.hr.family'
    _description = 'Employee Family Information'
    
    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'employee_id': fields.many2one('hr.employee', "Employee"),
        'relation': fields.many2one('vi.hr.quanhegiadinh','Relation', required=True),
        'date_of_birth': fields.date('Date of birth'),
        'year_of_birth': fields.char('Year of birth'),
        'address': fields.char('Address', size=128),
        'home_phone': fields.char('Home phone', size=32),
        'mobile': fields.char('Mobile', size=32),
        'email': fields.char('Email', size=32),
        'occupation': fields.many2one('vi.hr.nghenghiep','Occupation'),
        'work_address' : fields.char('Work address', size=128),
        'dependency_ok': fields.boolean('Is dependency'),
        'depreciation_start': fields.date('Depreciation start'),
        'depreciation_end': fields.date('Depreciation end'),
        'notes': fields.text('Notes'),
        'death': fields.boolean('Death'),
    }
    
hr_family()

class hr_employee(osv.osv):
    _inherit = 'hr.employee'
    
    _columns = {
        'vi_family_ids': fields.one2many('vi.hr.family', 'employee_id', 'Family'),
    }
    
hr_employee()