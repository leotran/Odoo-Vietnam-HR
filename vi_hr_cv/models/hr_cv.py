# -*- coding: utf-8 -*-
##############################################################################
#
#    @package vi_hr_cv HR Employee Curriculum Vitae for Odoo 7-saas5
#    @copyright Copyright (C) 2014 Leo Tran (leotran.hpvn@gmail.com). All rights reserved.#
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

class hr_curriculum_vitae(osv.Model):
    _inherit = 'hr.employee'
    
    def _get_year(self, cr, uid, ids, name, arg, context=None):
        values = self.read(cr, uid, ids, ['date_of_graduation'], context)
        res = dict(map(lambda x: (x['id'], x['date_of_graduation'] and x['date_of_graduation'][0:4] or False), values))
    
    _columns = {
        'reference': fields.char('Reference', size=128),        
        'address_origin_id': fields.many2one('res.partner', 'Origin Address'),
        'date_allocate_cmnd': fields.date('Date of Allocate'),
        'place_allocate_cmnd': fields.many2one("res.country.state", 'Place of Allocate'),
        'date_allocate_passport': fields.date('Date of Allocate'),
        'place_allocate_passport': fields.many2one("res.country.state", 'Place of Allocate'),
        'date_limit_passport': fields.date('Date of Limit'),
        'family_type': fields.many2one('vi.hr.thanhphan.giadinh','Family Type'),
        'employee_type': fields.many2one('vi.hr.thanhphan.banthan','Employee Type'),
        'nationality': fields.many2one('vi.hr.dantoc','Nationality'),
        'religiousness': fields.many2one('vi.hr.tongiao','Religiousness'),
        'training_level': fields.many2one('vi.hr.trinhdo.daotao','Training Level'),
        'training_place': fields.many2one('vi.hr.noi.daotao','Place of Training'),
        'training_subject': fields.many2one('vi.hr.khoa.daotao','Subject of Training'),
        'training_speciality': fields.many2one('vi.hr.chuyennganh.daotao','Speciality of Training'),
        'date_of_graduation': fields.date('Date of Graduation'),
        'year_of_graduation': fields.function(_get_year, type='char', readonly=True, string='Year'),
        'training_ranking': fields.many2one('vi.hr.xeploai.daotao','Ranking of Training'),
        'occupation': fields.many2one('vi.hr.nghenghiep','Occupation'),
        'personal_email': fields.char('Personal Email', size=32),
        'other_email': fields.char('Other Email', size=32),
        'yahoo': fields.char('Yahoo ID', size=32),
        'skype': fields.char('Skype ID', size=32),
        'msn': fields.char('MSN ID', size=32),
        'gtalk': fields.char('Gtalk ID', size=32),
        'household': fields.many2one('res.partner','Household'),
        'contact_emergency': fields.many2one('res.partner','Contact Emergency'),
        'relation': fields.many2one('vi.hr.quanhegiadinh','Relation'),
        'party_member_ok': fields.boolean('Is Party Member'),
        'date_party_admission': fields.date("Date of Party admission"),
        'duty_party': fields.many2one('vi.hr.chucvu','Duty'),
        'place_party_admission': fields.char('Place of party admission', size=128),
        'union_member_ok': fields.boolean('Is Union Member'),
        'date_union_admission': fields.date("Date of Union Admission"),
        'duty_uinon': fields.many2one('vi.hr.chucvu','Duty'),
        'place_union_admission': fields.char('Place of union admission', size=128),
        'military_ok': fields.boolean('Is Military'),
        'date_military_admission': fields.date('Date of Military admission'),
        'military_organization': fields.char('Military Organization', size=128),
        'duty_military': fields.many2one('vi.hr.chucvu','Duty'),
        'military_level': fields.many2one('vi.hr.capbac.quannhan','Military Level'),
        'army': fields.many2one('vi.hr.binhchung','Army'),
        'date_demobilisation': fields.date('Date of Demobilisation'),
        'reason': fields.text('Reason'),
        'wounded_soldier_ok': fields.boolean('Is wounded soldier'),
        'date_revolution_admission': fields.date('Date of Revolution admission'),
        'wounded_soldier_rate': fields.many2one('vi.hr.hangthuongbinh','Wounded_soldier rate'),
        'declining_labor_rate': fields.float('Declining labor rate'),
        'regimen_ok': fields.boolean('Regimen'),
        'blood_group': fields.selection([('o','O'),('a','A'),('b','B'),('ab','AB')],'Blood group'),
        'height': fields.float('Height'),
        'weight': fields.float('Weight'),
        'health_status': fields.char('Health status', size=64),
        'warning': fields.char('Warning', size=64),
        'disease': fields.char('Disease', size=64),
        'like': fields.text('Like'),
        'strength': fields.text('Strength'),
        'weakness': fields.text('Weakness'),
        'target': fields.text('Target'),
    }