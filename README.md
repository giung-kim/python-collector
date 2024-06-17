# Python-Collector

Python-Collector는 FastAPI와 네이버 API를 이용하여 책 정보를 수집하고 데이터베이스에 저장하는 프로젝트입니다. 이 프로젝트는 책 정보를 쉽게 수집하고 관리할 수 있는 도구를 제공합니다.

## 프로젝트 개요

이 프로젝트는 다음과 같은 목표를 가지고 있습니다:

- 네이버 API를 이용하여 실시간으로 책 정보를 검색
- 검색된 책 정보를 MongoDB에 저장
- 간단한 웹 인터페이스를 제공하여 사용자에게 책 정보를 표시

## 주요 기능

- **책 정보 검색:** 사용자가 입력한 키워드를 바탕으로 네이버 API를 통해 책 정보를 검색합니다.
- **데이터 저장:** 검색된 책 정보를 MongoDB에 저장하여 지속적으로 관리할 수 있습니다.
- **웹 인터페이스:** FastAPI와 Jinja2 템플릿을 이용하여 사용자에게 책 정보를 웹 페이지로 제공합니다.

## 사용 기술

- **백엔드 프레임워크:** FastAPI
- **데이터베이스:** MongoDB
- **웹 스크래핑:** Naver Book API
- **템플릿 엔진:** Jinja2
- **기타:** Uvicorn (ASGI 서버), ODMantic (MongoDB ODM)
