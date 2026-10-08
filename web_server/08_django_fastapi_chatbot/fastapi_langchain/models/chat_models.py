from pydantic import BaseModel, Field  # Pydantic 모델, 필드 옵션
from typing import Optional  # 선택값 타입
from datetime import datetime  # 현재 시각

# 채팅 요청 데이터 모델
class ChatRequest(BaseModel):
    message: str = Field(..., description='사용자 메시지', min_length=1, max_length=2000)  # 사용자 입력 메시지
    session_id: Optional[str] = Field(default="default", description="세션 식별자")  # 대화 세션 구분용 ID

# 채팅 응답 데이터 모델
class ChatResponse(BaseModel):
    response: str = Field(..., description='챗봇 응답 메시지')
    session_id: str = Field(..., description="세션 식별자")  # 응답이 속한 세션 ID
    timestamp: datetime = Field(default_factory=datetime.now, description='응답 생성 시각')

# 에러 응답 데이터 모델
class ErrorResponse(BaseModel):
    error: str = Field(..., description="에러 메시지")
    detail: Optional[str] = Field(None, description="상세 에러 정보")

# 서버 상태 확인 응답 모델
class HealthResponse(BaseModel):
    status: str = Field(..., description="서비스 상태")
    timestamp: datetime = Field(default_factory=datetime.now, description='확인 시간')

# 세션에 저장할 단일 대화 이력 모델
class HistoryItem(BaseModel):
    type: str = Field(..., description="메시지 유형: 'human'|'user' 또는 'ai'|'assistant'")  # 메시지 작성 주체
    content: str = Field(..., description="메시지 내용")

# 세션 이력을 설정하기 위한 요청 데이터 모델
class SetHistoryRequest(BaseModel):
    session_id: Optional[str] = Field(default="default", description="세션 식별자")
    history: list[HistoryItem] = Field(default_factory=list, description='세션에 설정할 순서 있는 대화 목록')