# Dockerfile
FROM node:14

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일들을 도커 이미지에 복사
COPY frontend/package*.json ./

# 의존성 설치
RUN npm install

# 소스 코드를 도커 이미지에 복사
COPY frontend/ .

# 앱 실행
CMD ["npm", "run", "serve"]
