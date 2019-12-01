from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from http_status import HttpStatus
from models import orm, NotificationCategory, NotificationCategorySchema, Notification, NotificationSchema
from sqlalchemy.exc import SQLAlchemyError

service_blueprint = Blueprint('service', __name__)
notification_category_schema = NotificationCategorySchema()
notification_schema = NotificationSchema()
service = Api(service_blueprint)

class NotificationResource(Resource):
	def get(self, id):
		notification = Notification.query.get_or_404(id)
		dumped_notification = notification_schema.dump(notification).data
		return dumped_notification
	
	


