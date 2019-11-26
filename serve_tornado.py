from abc import ABC

import numpy as np
import tensorflow as tf
import tornado.ioloop
import tornado.web
import tornado.websocket as websocket
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import time
# from tensorflow_core.python.keras.preprocessing.image import load_img, img_to_array

file_name = ""


class WebSocket(websocket.WebSocketHandler, ABC):
    def initialize(self, model):
        self.mo = model
        print('okok')

    def open(self):
        print("websocket opened")
        print(self.current_user)
        print(self.locale)
        # self.write_message("hello||okok")
        self.user = ""
        # self.mo = Plh()

    def on_message(self, message):
        print("message is :", message)
        message = message.split('||')
        if message[0] == 'name':
            t = time.time()
            mes = time.strftime("%Y%m%d%H%M%S", time.localtime(t)) + str(t).split('.')[0]
            self.write_message("name||" + mes)
            print('name: ', mes)
        if message[0] == 'pre':
            file_name = message[1]
            print('file name is ', file_name)
            mes = self.mo.pred("./" + file_name)
            print(type(mes))
            mess = str(mes)
            print(type(mess))
            self.write_message("result||" + mess)
        if message[0] == 'upload':
            self.write_message("result||emm")

    def on_close(self):
        print('socked closed')


# class Plh:
#     def __init__(self):
#         print('bigan load model')
#         self.model = load_model("./sim")
#         self.model.summary()
#
#     def pred(self, pre_dir):
#         img = load_img(pre_dir, target_size=(299, 299))
#         arr = img_to_array(img) / 255.0
#         arr = arr.reshape(1, 299, 299, 3)
#         pre = self.model.predict(arr)
#         classes = ['叶斑病', '灰斑病', '健康', '花叶病毒病', '锈病']
#         print(str(pre) + classes[np.argmax(pre)])
#         return (str(pre) + classes[np.argmax(pre)])

class Plh:
    def __init__(self):
        print('begin load model')
        self.model = tf.lite.Interpreter(model_path="./sss.lite")
        self.model.allocate_tensors()

    def pred(self, pre_dir):
        input_details = self.model.get_input_details()
        output_details = self.model.get_output_details()
        img = load_img(pre_dir, target_size=(299, 299))
        arr = img_to_array(img) / 255.0
        arr = arr.reshape(1, 299, 299, 3)
        self.model.set_tensor(input_details[0]['index'], arr)
        self.model.invoke()
        output_data = self.model.get_tensor(output_details[0]['index'])
        print(output_data)
        classes = ['叶斑病', '灰斑病', '健康', '花叶病毒病', '锈病']
        print("aaaaa", str(output_data) + classes[np.argmax(output_data)])
        return(classes[np.argmax(output_data)])


class ProfileHadler(tornado.web.RequestHandler, ABC):

    def get(self):
        print('get::')

    def post(self):
        print('post::')
        # argu_data = self.request.arguments.keys()
        # print(argu_data)
        meta = self.request.files['file'][0]
        print(meta.keys())
        filename = meta['filename']
        print(filename)
        cont_type = meta['content_type']
        print(cont_type)
        suffix = meta['filename'].split('.')[-1]
        print('suffix', suffix)
        with open(filename, 'wb') as f:
            f.write(meta['body'])
        print('saved, file name is ', file_name)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/web", WebSocket, {'model': Plh()}),
        (r"/post", ProfileHadler)
    ])
    application.listen(21567)
    print('begin listening')
    tornado.ioloop.IOLoop.current().start()
