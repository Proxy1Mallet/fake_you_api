from uuid import uuid4
from aiohttp import ClientSession

from .data import Data
from .objects import *

class FakeYou(Data):
    @classmethod
    async def create_account(cls, email: str, password: str, username: str):
        _data = {
            'email_address': email,
            'password': password,
            'password_confirmation': password,
            'username': username
        }
        return cls._session.post(url = cls._api('create_account'), headers = cls._headers, json = _data).json()

    @classmethod
    def login(cls, username_or_email: str, password: str):
        _data = {
            'username_or_email': username_or_email,
            'password': password
        }
        return cls._session.post(url = cls._api('login'), headers = cls._headers, json = _data).json()

    @classmethod
    def get_session(cls) -> GetSession:
        _req = cls._session.get(url = cls._api('session'), headers = cls._headers)
        return GetSession(data = _req.json()).get_sesion

    @classmethod
    def get_tts_list(cls):
        return cls._session.get(url = cls._api('tts/list'), headers = cls._headers).json()

    @classmethod
    def get_job(cls, job_token):
        _req = cls._session.get(url = cls._api(f'tts/job/{job_token}'), headers = cls._headers)
        return GetJob(data = _req.json()).get_job

    @classmethod
    def inference(cls, text: str, model_token: str):
        _data = {
            'inference_text': text,
            'tts_model_token': model_token,
            'uuid_idempotency_token': str(uuid4())
        }
        _req = cls._session.post(url = cls._api('tts/inference'), headers = cls._headers, json = _data)
        return Inference(data = _req.json()).inference

    @classmethod
    def save_waw(cls, url: str = None, path: str = None) -> bytes:
        if path: _url = f'https://storage.googleapis.com/vocodes-public{path}'
        if url: url = url
        req = cls._session.get(url = _url, headers = cls._headers).content
        with open(file = 'your_file.wav', mode = 'wb') as _record_file:
            _record_file.write(req)
            _record_file.close()