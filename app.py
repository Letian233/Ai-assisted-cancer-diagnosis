from flask import Flask
from flask_cors import CORS
from blueprints.survival import survival_bp
from blueprints.ct_image import ct_image_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# 注册蓝图
app.register_blueprint(survival_bp)
app.register_blueprint(ct_image_bp)

# 主应用的根路由
@app.route('/')
def index():
    return app.send_static_file('survival.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)