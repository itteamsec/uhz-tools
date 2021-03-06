from flask import Flask
import settings
from ext import db
from tools.fileupload.views import file
from tools.message.views import tools

app = Flask(__name__, template_folder='../templates', static_folder='../static')


def create_app():
    # 导入配置文件
    app.config.from_object(settings.Production)
    db.init_app(app=app)
    # 注册蓝图
    app.register_blueprint(tools)
    app.register_blueprint(file)
    return app
