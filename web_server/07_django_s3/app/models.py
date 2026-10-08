from django.db import models  # Django 모델 기능
from django import forms      # Django 폼 기능

class UploadedFile(models.Model):
    # 업로드 파일을 uploads/ 경로 기준으로 저장하는 파일 필드
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)  # 파일 업로드 시간 자동 저장

    # 문자열로 파일 객체 확인시 이름 반환
    def __str__(self):
        return self.file.name

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile  # 폼 생성시 기반 모델 : UploadedFile
        fields = ['file']     # 폼에 포함할 필드