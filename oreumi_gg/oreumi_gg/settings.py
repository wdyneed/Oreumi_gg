"""
Django settings for oreumi_gg project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

"""
json 시크릿 설정
"""
import os, json
from django.core.exceptions import ImproperlyConfigured

# jwt 소셜로그인
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, "secrets.json")
champion_file = os.path.join(BASE_DIR, "champion.json")
# SECRET_KEY = os.path.join(BASE_DIRm, "local_secrets.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "{} 경로 확인 실패".format(setting)
        raise ImproperlyConfigured(error_msg)    
#시크릿 파일 열기 끝

SECRET_KEY = get_secret("DB_SECRET")
API_KEY = get_secret("LOL_API")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 사용 앱
    'gg_app',
    'user_app',
    'django_ckeditor_5',


    # social api
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.kakao',

    # 댓글
    
    
    #채팅
    "django.contrib.humanize",
    "channels",
    "channels_redis",
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    # allauth와 상관없는 관리자 로그인
    'django.contrib.auth.backends.ModelBackend',
    # 일반유저 allauth 인증
    'allauth.account.auth_backends.AuthenticationBackend',]

# uer 정보를 수정
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # 로그인시 username 이 아니라 email을 사용하게 하는 설정
ACCOUNT_EMAIL_REQUIRED = True  # 회원가입시 필수 이메일을 필수항목으로 만들기
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # 'mandatory' 전송하고 인증까지, 'optional' 전송만, 'none' 전송없음있다
ACCOUNT_USERNAME_REQUIRED = False  # USERNAME 을 필수항목에서 제거

ACCOUNT_UNIQUE_EMAIL = True # 중복을  허용하지 않음
ACCOUNT_LOGOUT_ON_GET = True # 로그아웃 확인 묻지 않고 즉시 로그아웃
SOCIALACCOUNT_LOGIN_ON_GET = True # 바로 소셜로그인페이지로 넘어가도록

ACCOUNT_SIGNUP_FORM_CLASS = 'user_app.forms.SignupForm'
AUTH_USER_MODEL = 'user_app.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.naver.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER") # 내 이메일주소
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD") #발급한 앱비밀번호
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[이메일 인증]' #이메일 제목앞에 붙일내용


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'oreumi_gg.urls'
BASE_DIR_TEMPLATES = Path(__file__).resolve().parent.parent


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR_TEMPLATES, "gg_app/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oreumi_gg.wsgi.application'

ASGI_APPLICATION = "oreumi_gg.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_secret("DB_NAME"),
        "USER": get_secret("DB_USER"),
        "PASSWORD": get_secret("DB_PASSWORD"),
        "HOST": get_secret("DB_HOST"),
        "PORT": get_secret("DB_PORT"),
    }
}
INTERNAL_IPS = "127.0.0.1"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


"""
##################### ckeditor top############################# 
"""
# 미디어파일 링크 pip install Pillow


CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow" 


customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload"
        ],
    },
    "comment": {
        "language": {"ui": "ko", "content": "ko"},
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
        ],
    },
    "extends": {
        "language": "ko",
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        "toolbar": [
            "heading",
            "codeBlock",
            "|",
            "outdent",
            "indent",
            "|",
            "bold",
            "italic",
            "link",
            "underline",
            "strikethrough",
            "code",
            "subscript",
            "superscript",
            "highlight",
            "|",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "insertImage",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "mediaEmbed",
            "removeFormat",
            "insertTable",
            "sourceEditing",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
                "|",
                "toggleImageCaption",
                "|"
            ],
            "styles": [
                "full",
                "side",
                "alignLeft",
                "alignRight",
                "alignCenter",
            ],
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
            "tableProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
            "tableCellProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
        },
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
        "list": {
            "properties": {
                "styles": True,
                "startIndex": True,
                "reversed": True,
            }
        },
        "htmlSupport": {
            "allow": [
                {"name": "/.*/", "attributes": True, "classes": True, "styles": True}
            ]
        },
        "mediaEmbed": {"previewsInData": "true"}
    },
}





"""
##################### ckeditor bottom ############################# 
"""
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR,'gg_app\static'))
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# 로그인 auth사용시 링크 
LOGIN_REDIRECT_URL = 'gg_app:index'
LOGOUT_REDIRECT_URL = 'gg_app:index'

# LOGIN_URL = "user_app:login"

# ACCOUNT_SESSION_REMEMBER = True  # 브라우저를 닫아도 세션기록 유
# SESSION_COOKIE_AGE = 3600  # 쿠키를 한시간만 저장  
# 지우는 명령어  python manage.py clearsessions


# py manage.py runserver 180.228.166.140:443  https로 연결 / 80은 http
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS =['http://oreumi.shop','https://oreumi.shop','http://oreumi.store','https://oreumi.store']
CSRF_COOKIE_SECURE = False

