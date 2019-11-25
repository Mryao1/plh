from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.nn import softmax
from tensorflow.keras.losses import sparse_categorical_crossentropy
import tensorflow_hub as hub
from tensorflow.keras.preprocessing.image import load_img, img_to_array


class Pre:
    def load(self):
        print('bigan load model')
        module = hub.Module("6ea043b1bb751a9fdf5e9214bef8fcee38778e51")
        # r"C:\Users\Mry\AppData\Local\Temp\tfhub_modules\
        resnet = hub.KerasLayer(module, input_shape=(299, 299, 3), output_shape=[1536])
        model = Sequential([
            resnet,
            Dense(5, activation=softmax)
        ])
        model.compile(optimizer='adam', loss=sparse_categorical_crossentropy, metrics=['accuracy'])
        model.summary()
        model.load_weights("resn_wights.keras")
        # r"E:\Deep learning\pest\model\
        return model


    def predic(self, model, pre_dir):
        print('bigan predict')
        img = load_img(pre_dir, target_size=(299, 299))
        arr = img_to_array(img) / 255.0
        arr = arr.reshape(1, 299, 299, 3)
        pre = model.predict(arr)
        print(pre)



#if __name__ == '__main__':
    pre_dir = r'E:\Deep learning\pest\train\cclsf\0a6f13299144c56e5d0b7eb062680b88.jpg'
    classes = ['cclsf', 'cztd', 'healthy', 'mdmv', 'pp']
    p = Pre()
    model = p.load()
    pre = p.predic(model, pre_dir)
    print(classes[np.argmax(pre)])
