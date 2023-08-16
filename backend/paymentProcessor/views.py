from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import OrderSerializer, GetPaymentStatusSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
import uuid

class OrderAPIView(views.APIView):
    """
    A simple APIView for creating order entries.
    """
    serializer_class = OrderSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            data['order_meta'] = str(uuid.uuid4())  # Generate order_meta UUID
            serializer = OrderSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                order = serializer.save()

                # Get the payment_url from the serializer
                payment_url = serializer.data.get('payment_url')

                # Create the response data
                response_data = {
                    'order_id': order.order_id,
                    'order_amount': order.order_amount,
                    'payment_url': payment_url
                }

                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)


class GetPaymentStatusView(views.APIView):
    serializer_class = GetPaymentStatusSerializer

    def post(self, request):
        try:
            data = request.data
            order_id = data.get('order_id')

            # Replace this logic with actual payment status retrieval
            # Here, you would query your organization or payment gateway for the payment status
            payment_status = "Success"  # Replace with the actual status

            response_data = {
                'order_id': order_id,
                'status': payment_status
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"result": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
