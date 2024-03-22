from config.create import *
from schemas.lingyi_api import lingyi_api

if __name__ == '__main__':
    app = create_app()
    
    # 注册蓝图
    app.register_blueprint(lingyi_api, url_prefix='/lingyi')

    app.run()
    