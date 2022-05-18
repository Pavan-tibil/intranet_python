from rest_framework import serializers
from .models import *


# Serializer for Latest news Model
class LatestNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestNews
        fields = '__all__'


# Serializer for Image files Model
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFiles
        fields = '__all__'


# Serializer for Comments Model
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


# Serializer to post Comments Model
class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['section_title', 'comment_description', 'user_name']


# Serializer to get images from media files with the help of image adress which is saved in image files
class GetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFiles
        fields = ('id', 'image_type')


# Serializer for Staffdirectory Model
class StaffDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffDirectory
        fields = '__all__'


# Serializer for Refer candidates Model
class RefercandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferCandidates
        fields = '__all__'


# Serializer to post Refer candidate Model
class RefercandidatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferCandidates
        fields = '__all__'


# Serializer for New Vacancy Model
class vacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


# Serializer for Forum model
class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'


# Serializer for Award and Recognition model
class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = '__all__'
