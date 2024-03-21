from config.create import *
from schemas.api import home_api

if __name__ == '__main__':
    app = create_app()
    
    # 注册蓝图
    app.register_blueprint(home_api, url_prefix='/api')

    app.run()
    