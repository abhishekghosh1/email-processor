from flask import request
from flask_restplus import Resource

from app.main.service.email_service import remove_signature
from app.main.util.decorator import token_required
from ..util.dto import EmailDto

api = EmailDto.api
signature = EmailDto.signature


@api.route('/signature')
class Signature(Resource):
    """
        Email Signature Resource
    """

    @api.doc('Remove Signature')
    @token_required
    @api.expect(signature, validate=True)
    def delete(self):
        # get the post data
        post_data = request.json
        return remove_signature(post_data.get('message'),
                                post_data.get('sender'))
