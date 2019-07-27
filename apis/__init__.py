""""
Puts together the API namespaces
"""

from flask_restplus import Api

from .api_namespace1 import api as api_e

api = Api(version='1.0',
          default='namespace1',
          title='API title',
          description='API description.')

api.namespaces.clear()
api.add_namespace(api_e)
