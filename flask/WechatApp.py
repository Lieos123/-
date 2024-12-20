# from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
# import os
# from ultralytics import YOLO


# app = Flask(__name__)


# # 这里是首页
# #@app.route("/")
# @app.route('/', methods=['get', 'post']) 
# def index():
#     return render_template("upload.html")


# # 这里是保存用户上传的图片到文件夹中
# @app.route("/upload", methods=["POST", "GET"])
# def upload():
#     if request.method == "POST":
#         f = request.files["file"]
#         basepath = os.path.dirname(__file__)
#         upload_path = os.path.join(
#             basepath, "static/images", secure_filename(f.filename)
#         )
#         f.save(upload_path)
#         print(f)
#         names_list = []#名称列表
#         confidence_list=[]#置信度列表
#         # 下半部分用于yolov8的训练代码
#         model = YOLO("WechatApp_BJFU-master/flask/best.pt")  # 训练好的识别模型
#         results = model.predict(source=upload_path, conf=0.25)
#         for result in results:
#             classes = result.names  # 类别名称
#             confidences = result.boxes.conf  # 置信度
#             class_ids = result.boxes.cls  # 类别 ID
#             for class_id, confidence in zip(class_ids, confidences):
#                 class_name = classes[int(class_id)]  # 获取类别名称
#                 names_list.append(class_name)
#                 confidence_list.append(confidence) 
#         return render_template("upload_success.html", names=names_list,confidences=confidence_list)
#     return render_template("upload.html")


# if __name__ == "__main__":
#     app.run(port=8080)






# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename
# import os
# from ultralytics import YOLO

# app = Flask(__name__)

# # 设置上传文件夹路径
# UPLOAD_FOLDER = 'static/images'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # 上传图片到服务器并进行识别
# @app.route("/upload", methods=["POST"])
# def upload():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     if file:
#         filename = secure_filename(file.filename)
#         upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(upload_path)

#         # 使用YOLO进行图像识别
#         #model = YOLO("WechatApp_BJFU-master/flask/best.pt")  # 训练好的识别模型
#         model = YOLO("E:\Vscode(E)\WechatApp_BJFU-master/flask/best.pt")
#         results = model.predict(source=upload_path, conf=0.25)
        
#         names_list = []  # 名称列表
#         confidence_list = []  # 置信度列表
        
#         for result in results:
#             classes = result.names  # 类别名称
#             confidences = result.boxes.conf  # 置信度
#             class_ids = result.boxes.cls  # 类别 ID
            
#             for class_id, confidence in zip(class_ids, confidences):
#                 class_name = classes[int(class_id)]  # 获取类别名称
#                 names_list.append(class_name)
#                 confidence_list.append(confidence)
        
#         # 找到置信度最高的识别结果
#         if confidence_list:
#             max_conf_index = confidence_list.index(max(confidence_list))
#             highest_confidence_name = names_list[max_conf_index]
#             return jsonify({"highest_confidence_name": highest_confidence_name})
#         else:
#             return jsonify({"error": "No objects detected"}), 400

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080)

#################### 8.10   23:31

# from flask import Flask, request, jsonify
# from flask_cors import CORS # 解决跨域问题
# from werkzeug.utils import secure_filename
# import os
# from ultralytics import YOLO

# app = Flask(__name__)

# # 启用 CORS，允许所有来源访问
# CORS(app)

# # 设置上传文件夹路径
# UPLOAD_FOLDER = 'static/images'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # 上传图片到服务器并进行识别
# @app.route("/", methods=["POST"])
# def upload():
#     try:
#         # 检查是否包含文件数据
#         if 'file' not in request.files:
#             app.logger.error("No file part in the request")
#             return jsonify({"error": "No file part"}), 400

#         file = request.files['file']
#         if file.filename == '':
#             app.logger.error("No selected file")
#             return jsonify({"error": "No selected file"}), 400

#         if file:
#             filename = secure_filename(file.filename)
#             upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(upload_path)
#             app.logger.info(f"File saved to {upload_path}")

#             # 使用YOLO进行图像识别
#             model = YOLO(r"E:/Vscode(E)/WechatApp_BJFU-master/flask\best.pt")
#             results = model.predict(source=upload_path, conf=0.25)
#             app.logger.info(f"YOLO model prediction completed")

#             names_list = []  # 名称列表
#             confidence_list = []  # 置信度列表

#             for result in results:
#                 classes = result.names  # 类别名称
#                 confidences = result.boxes.conf  # 置信度
#                 class_ids = result.boxes.cls  # 类别 ID

#                 for class_id, confidence in zip(class_ids, confidences):
#                     class_name = classes[int(class_id)]  # 获取类别名称
#                     names_list.append(class_name)
#                     confidence_list.append(confidence)

#             # 找到置信度最高的识别结果
#             if confidence_list:
#                 max_conf_index = confidence_list.index(max(confidence_list))
#                 highest_confidence_name = names_list[max_conf_index]
#                 app.logger.info(f"Highest confidence object: {highest_confidence_name}")
#                 return jsonify({"highest_confidence_name": highest_confidence_name})
#             else:
#                 app.logger.warning("No objects detected in the image")
#                 return jsonify({"error": "No objects detected"}), 400

#     except Exception as e:
#         app.logger.error(f"An error occurred: {str(e)}")
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080, debug=True)

##################

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from ultralytics import YOLO

app = Flask(__name__)

# 启用 CORS，允许所有来源访问
CORS(app)

# 设置上传文件夹路径
UPLOAD_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 确保上传文件夹存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 上传图片到服务器并进行识别
@app.route("/", methods=["POST"])
def upload():
    try:
        # 检查是否包含文件数据
        if 'file' not in request.files:
            app.logger.error("No file part in the request")
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        if file.filename == '':
            app.logger.error("No selected file")
            return jsonify({"error": "No selected file"}), 400

        if file:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            app.logger.info(f"File saved to {upload_path}")

            # 使用YOLO进行图像识别
            model = YOLO(r"E:/Vscode(E)/WechatApp_BJFU-master/flask/best.pt")
            results = model.predict(source=upload_path, conf=0.25)
            app.logger.info(f"YOLO model prediction completed")

            names_list = []  # 名称列表
            confidence_list = []  # 置信度列表

            for result in results:
                classes = result.names  # 类别名称
                confidences = result.boxes.conf  # 置信度
                class_ids = result.boxes.cls  # 类别 ID

                for class_id, confidence in zip(class_ids, confidences):
                    class_name = classes[int(class_id)]  # 获取类别名称
                    names_list.append(class_name)
                    confidence_list.append(confidence)

            # 找到置信度最高的识别结果
            if confidence_list:
                max_conf_index = confidence_list.index(max(confidence_list))
                highest_confidence_name = names_list[max_conf_index]
                app.logger.info(f"Highest confidence object: {highest_confidence_name}")
                return jsonify({"highest_confidence_name": highest_confidence_name})
            else:
                app.logger.warning("No objects detected in the image")
                return jsonify({"error": "No objects detected"}), 400

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
