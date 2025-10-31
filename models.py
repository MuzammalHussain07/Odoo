from odoo import models, fields, api


class ProjectProject(models.Model):
_inherit = 'project.project'


header_image = fields.Binary("Project Image")
header_image_name = fields.Char('Image Filename')


class ProjectProof(models.Model):
_name = 'project.proof'
_description = 'Project Proof (for approvals)'


name = fields.Char('Title', required=True)
project_id = fields.Many2one('project.project', string='Project', ondelete='cascade')
file = fields.Binary('File')
filename = fields.Char('Filename')
state = fields.Selection([('pending','Pending'), ('approved','Approved'), ('rejected','Rejected')], default='pending')
token = fields.Char('Public Token', readonly=True)
public_url = fields.Char('Public URL', compute='_compute_public_url')


def _compute_public_url(self):
for rec in self:
if rec.token:
# host will be filled by controller; we compute the path only
rec.public_url = '/saas/proof/approve/%s' % rec.token
else:
rec.public_url = False


@api.model
def create(self, vals):
if not vals.get('token'):
vals['token'] = secrets.token_urlsafe(24)
return super().create(vals)


def action_generate_public(self):
for r in self:
if not r.token:
r.token = secrets.token_urlsafe(24)
return True


def action_mark_approved(self):
self.state = 'approved'


def action_mark_rejected(self):
self.state = 'rejected'
