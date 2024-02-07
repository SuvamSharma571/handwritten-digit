import tensorflow as tf

__model = None

def get_prediction(image):
    x = image
    my_pred = __model.predict(x)
    prediction = my_pred == tf.math.reduce_max(my_pred)
    number_pred = tf.math.argmax(prediction, axis=1)
    return number_pred


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model
    if __model is None:
        __model = tf.keras.models.load_model('mnist_model.h5')
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()