from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.conf import settings
# from pest import test

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.nn import softmax
from tensorflow.keras.losses import sparse_categorical_crossentropy
import tensorflow_hub as hub
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np


class Pre:
    def load(self):
        print('bigan load model')
        #module = hub.Module(r"E:\Deep learning\pest\model\inception_model")
        module = hub.Module('/root/inception_model')

        resnet = hub.KerasLayer(module, input_shape=(299, 299, 3), output_shape=[2048])
        model = Sequential([
            resnet,
            Dense(5, activation=softmax)
        ])
        model.compile(optimizer='adam', loss=sparse_categorical_crossentropy, metrics=['accuracy'])
        model.summary()
        model.load_weights('/root/inceptionv16_wights.keras')

        return model

    def predic(self, model, pre_dir):
        print('bigan predict')
        img = load_img(pre_dir, target_size=(299, 299))
        arr = img_to_array(img) / 255.0
        arr = arr.reshape(1, 299, 299, 3)
        pre = model.predict(arr)
        classes = ['叶斑病', '灰斑病', '健康', '花叶病毒病', '锈病']
        return (classes[np.argmax(pre)])


#P = Pre()
#model = P.load()
def index(request):
    return render(request, 'myapp/register.html')


def upload(request):
    if request.method == 'POST':
        img = request.FILES['testimg']
        imgname = '%s/%s' % (settings.MEDIA_ROOT, img.name)
        with open(imgname, 'wb') as f:
            for fimg in img.chunks():
                f.write(fimg)
        P = Pre()
        model = P.load()
        name = P.predic(model, imgname)

    # 应该加到这里
    return render(request, 'myapp/upload.html')
