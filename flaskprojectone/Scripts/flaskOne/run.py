# -*- coding: utf-8 -*-
from app import app             #from app 指导入 app 包里的 __iniy__.py 所以这句话的含义是导入 __.init__.py 里面的 app实例。
if __name__ == '__main__':
	 #app.debug = True            # 设置调试模式，生产模式的时候要关掉debug
	app.run(debug = True )        # 启动服务器
