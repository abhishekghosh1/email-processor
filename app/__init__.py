from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.email_controller import api as signature_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Email Processor WITH JWT',
          version='1.0',
          description='a Rest webservice to process email content'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(signature_ns, path='/email')
api.add_namespace(auth_ns)