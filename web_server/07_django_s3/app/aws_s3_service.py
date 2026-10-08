import boto3  # AWS S3 클라이언트 생성 라이브러리
from botocore.exceptions import NoCredentialsError  # AWS 인증정보 예외 처리용 클래스
from django.conf import settings  # Django 프로젝트 settings.py
from datetime import datetime     # 현재 날짜/시간

class S3Client:
    # S3 클라이언트를 생성하고 버킷명을 초기화하는 메서드
    def __init__(self):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
            region_name = settings.AWS_S3_REGION_NAME,
        )
        self.bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    # 파일을 S3에 업로드하고 파일 URL 전체경로 반환하는 함수
    def upload(self, file):
        save_dir = 'uploads/'  # S3 버킷내 저장 폴더
        now = datetime.now()
        date_prefix = now.strftime('%Y%m%d_%H%M%S_')  # 파일명 접두어 (업로드시간)
        new_file_name = f"{date_prefix}{file.name}"   # 중복방지용
        extra_args = {'ContentType': file.content_type}  # 업로드 파일의 MIME 타입 설정
        try:
            self.s3.upload_fileobj(
                file,
                self.bucket_name,
                f'{save_dir}{new_file_name}',  # S3 전체 경로
                ExtraArgs = extra_args        # 추가 옵션
            )
            # 업로드된 파일 접근 가능한 전체 URL 반환
            return f'https://{self.bucket_name}.s3.amazonaws.com/{save_dir}{new_file_name}'
        # AWS 인증 오류시 오류메시지 출력
        except NoCredentialsError:
            print('AWS 인증정보가 없습니다!')