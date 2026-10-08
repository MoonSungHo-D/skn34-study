from django.shortcuts import render, redirect # 템플릿 응답, 페이지 이동 처리
from django.contrib import messages  # 사용자 알림 메시지 프레임워크

from .aws_s3_service import S3Client  # S3 업로드/조회/삭제 처리 클래스
from .models import FileUploadForm  # 파일 업로드 폼

s3_client = S3Client()  # S3 제어 클라이언트 객체 생성

# 업로드된 파일을 S3에 저장하고 결과를 화면에 반환하는 View
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)  # 데이터와 파일을 함께 폼에 바인딩

        if form.is_valid():
            model = form.save(commit=False)  # 모델 객체만 생성
            print(model.file)  # 파일 정보 확인
            obj_url = s3_client.upload(form.files['file'])  # 폼에 전송된 파일을 S3 업로드 & URL 반환
            print(obj_url)     # 파일 URL 확인
            model.file = obj_url  # 모델 file 필드에 저장
            model.save()  # DB 반영

            # 성공 메시지 & 파일 링크
            messages.success(request, f"""
            🎉파일 업로드 성공!🎉
            <a href="{obj_url}">🗃️업로드한 파일🗃️</a>을 확인하세요!
            """)

            return redirect('app:upload')  # 업로드페이지로 이동
    else:
        form = FileUploadForm()  # 빈 업로드 폼 생성
    return render(request, 'app/upload.html', {'form': form})  # 업로드 페이지 렌더링
