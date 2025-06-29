import requests
import pytest
import allure
from hw_9.models.api_models import LoginResponse
from sqlalchemy import create_engine, text, MetaData, Table
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
username = os.getenv("api_username")
key = os.getenv("api_key")
base_url = os.getenv("api_url")
login_url = os.getenv("api_url_login")


@allure.title('Получить временный токен для действий пользователя')
@pytest.fixture(scope='session')
def api_token():
    response = requests.post(
        f'{base_url}{login_url}',
        data={'username': username, 'key': key}
    )
    assert response.status_code == 200, f"Некорректный код ответа, получен {response.status_code}"
    LoginResponse.model_validate(response.json())
    token = response.json()['api_token']
    yield token


@allure.title('Действия с базой данных')
@pytest.fixture(scope='session')
def db_session():
    connection_string = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()
    oc_cart = Table('oc_cart', metadata, autoload_with=engine)
    oc_session = Table('oc_session', metadata, autoload_with=engine)
    yield session, oc_cart, oc_session
    session.execute(text("TRUNCATE TABLE oc_cart;"))
    session.execute(text("TRUNCATE TABLE oc_session;"))
    session.close()
