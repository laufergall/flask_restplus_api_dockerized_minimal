""""
Includes the endpoints for namespace1
"""

from flask_restplus import Namespace, Resource

api = Namespace('namespace1',
                description='namespace description.')


@api.route('/endpoint1')
class Endpoint1(Resource):

    def get(self):
        """
        docstr GET
        """

        return 'Hello - minimal flask restplus'
