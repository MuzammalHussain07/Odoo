from odoo import http
from odoo.http import request


class SAASProofController(http.Controller):


@http.route(['/saas/proof/approve/<string:token>'], type='http', auth='public', website=True)
def public_proof_approval(self, token, **kw):
Proof = request.env['project.proof'].sudo()
proof = Proof.search([('token', '=', token)], limit=1)
if not proof:
return request.render('website.404')


# If the token exists, show a very small approval page with buttons.
# Clicking the approve/reject triggers a POST to a secured route that sets the state.
return request.render('odoo_saas_demo.proof_public_page', {
'proof': proof,
})


@http.route(['/saas/proof/approve_action/<string:token>'], type='http', auth='public', methods=['POST'], website=True)
def public_proof_action(self, token, **kw):
Proof = request.env['project.proof'].sudo()
proof = Proof.search([('token', '=', token)], limit=1)
if not proof:
return request.render('website.404')
action = kw.get('action')
if action == 'approve':
proof.sudo().action_mark_approved()
message = 'Approved'
elif action == 'reject':
proof.sudo().action_mark_rejected()
message = 'Rejected'
else:
message = 'No action'
# Simple confirmation page
return request.render('odoo_saas_demo.proof_action_done', {'message': message, 'proof': proof})
