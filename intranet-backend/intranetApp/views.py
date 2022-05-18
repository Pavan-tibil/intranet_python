# imported modules

import datetime
import json
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
# from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status, generics
from django.contrib.auth.models import User
from django.http import Http404
import jwt
from rest_framework.exceptions import AuthenticationFailed
from datetime import *
import datetime


# Create your views here.

# API for Login

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        # find user using email
        user = StaffDirectory.objects.filter(email=email, password=password).first()

        if user is None:
            raise AuthenticationFailed('Enter the valid email or password')

        payload = {
            "id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        # token.decode('HS256')
        # we set token via cookies
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token,
                            httponly=True)  # httponly - frontend can't access cookie, only for backend
        user = StaffDirectory.objects.filter(email=payload['email']).first()
        serializer = StaffDirectorySerializer(user)
        json_convert = json.dumps(serializer.data)

        # return JsonResponse(json_convert,safe=False)
        response.data = {
            'jwt token': token,
            'user': json.loads(json_convert)
        }
        # if email and password are correct

        return response


# API for latest_news Model

class Latestnews(APIView):

    def get(self, request):
        news = LatestNews.objects.all()

        response = LatestNewsSerializer(news, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})

    def post(self, request):
        serializer = LatestNewsSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # if anything not valid, raise exception

        serializer.save()

        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return LatestNews.objects.get(pk=pk)
        except LatestNews.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LatestNewsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "Messages": "Latest_news Update Successfully"
        }, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({
            "Messages": "Latest_news Deleted Successfully"
        })


# API to get Comments by id

class comments_by_id(APIView):
    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404

    def get(self, request, *args, pk, **kwargs):
        snippet = self.get_object(pk)
        serializer = CommentSerializer(snippet, data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            "comments": serializer.data,
        })


# API for comment model
class comments(APIView):
    def get(self, req):
        total_comments = Comments.objects.all()

        response = CommentSerializer(total_comments, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})

    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = CommentPostSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # if anything not valid, raise exception

        serializer.save()

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print(snippet.id)
        serializer = CommentSerializer(snippet, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
        return Response({
            "Messages": "Customer Update Successfully"
        }, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({
            "Messages": "staff Deleted Successfully"
        })


# API for Image files Model

class image_files(APIView):
    def get(self, req):
        all_image = ImageFiles.objects.all()

        response = ImageSerializer(all_image, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})

    def post(self, request):
        serializer = ImageSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # if anything not valid, raise exception

        serializer.save()

        return Response(serializer.data)


# API to fetch the image from the media folder on the basis of image adress

class ImageViewSet(APIView):
    queryset = ImageFiles.objects.all()
    serializer_class = ImageSerializer

    def get(self, req):
        image = ImageFiles.objects.all()

        response = GetImageSerializer(image, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # if anything not valid, raise exception

        serializer.save()

        return Response(serializer.data)


# API for Staff directory Model

class staff_directory(APIView):

    def get(self, req):
        total_staff = StaffDirectory.objects.all()

        response = StaffDirectorySerializer(total_staff, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})

    def get_object(self, pk):
        try:
            return StaffDirectory.objects.get(pk=pk)
        except StaffDirectory.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = StaffDirectorySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # if anything not valid, raise exception

        serializer.save()

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print(snippet.id)
        serializer = StaffDirectorySerializer(snippet, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
        return Response({
            "Messages": "staff Update Successfully"
        }, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({
            "Messages": "staff Deleted Successfully"
        })


# API for Refer candidates model

class referCandidates(APIView):

    def get(self, req):
        total_staff = ReferCandidates.objects.all()

        response = RefercandidateSerializer(total_staff, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})


    def get_object(self, pk):
        try:
            return ReferCandidates.objects.get(pk=pk)
        except ReferCandidates.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = RefercandidatePostSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # if anything not valid, raise exception

        serializer.save()

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RefercandidateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "Messages": "Customer Update Successfully"
        }, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({
            "Messages": "Customer Deleted Successfully"
        })


# API for New vacancy model

class vacancy(APIView):

    def get(self, req):
        total_vacancy = Vacancy.objects.all()

        response = vacancySerializer(total_vacancy, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})

    def post(self, request):
        serializer = vacancySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # if anything not valid, raise exception

        serializer.save()

        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = vacancySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "Messages": "Customer Update Successfully"
        }, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({
            "Messages": "Customer Deleted Successfully"
        })


# API for Forum model

class forum(APIView):
    def get(self, req):
        forum_details = Forum.objects.all()

        response = ForumSerializer(forum_details, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})

    def post(self, request):
        serializer = ForumSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # if anything not valid, raise exception

        serializer.save()

        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Forum.objects.get(pk=pk)
        except Forum.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ForumSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "Messages": "Customer Update Successfully"
        }, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({
            "Messages": "Customer Deleted Successfully"
        })


# API for Award and Recognition model

class awards(APIView):

    def get(self, req, year):
        print(req, year)
        awards = Awards.objects.all().filter(awarded_year=year)
        # print(awards)

        response = AwardsSerializer(awards, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})

        raise Http404

    def post(self, request, year):
        serializer = AwardsSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)  # if anything not valid, raise exception

        serializer.save()

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AwardsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "Messages": "Customer Update Successfully"
        }, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({
            "Messages": "Customer Deleted Successfully"
        })

# API for Award and Recognition model

class awardyear(APIView):

    def get(self, req):
        awards = Awards.objects.all()
        years = set()
        for i in awards:
            years.add(i.awarded_year)
        year_list = list(years)
        print(year_list)

        response = AwardsSerializer(year_list, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': year_list})

        raise Http404

class get_user_list(APIView):

    def get(self, req):
        awards = StaffDirectory.objects.all().filter(status = 1)

        response = StaffDirectorySerializer(awards, many=True)

        response_json = json.loads(json.dumps(response.data))

        return JsonResponse({'data': response_json})