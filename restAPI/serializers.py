from rest_framework import serializers
from .models import Advisor, User_new, Booking

class AdvisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id', 'name', 'photo_url')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_new
        fields = ('id', 'name', 'email', 'password')

class BookingSerializer(serializers.ModelSerializer):
    advisor_id = serializers.SerializerMethodField('get_advisor_id')
    advisor_name = serializers.SerializerMethodField('get_advisor_name')
    advisor_photo_url = serializers.SerializerMethodField('get_advisor_url')

    def get_advisor_id(self, book):
        return book.advisor.id
    
    def get_advisor_name(self, book):
        return book.advisor.name
    
    def get_advisor_url(self, book):
        return book.advisor.photo_url
    
    class Meta:
        model = Booking
        fields = ('id', 'booking_time', 'advisor_id', 'advisor_name', 'advisor_photo_url')