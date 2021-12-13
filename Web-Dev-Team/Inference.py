import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
import csv
import sys

model_path = 'model.tflite'

#Load the labels into a list
classes = ['RedRose', '???']
label_map = {1: 'RedRose'}
for label_id, label_name in label_map.items():
    classes[label_id-1] = label_name

# Define a list of colors for visualization
COLORS = np.random.randint(0, 255, size=(len(classes), 3), dtype=np.uint8)

def create_csv(results) :
    data = [("#", "Bounding box coordinates", "Accuracy")]
    for i in range(len(results)):
        coordinates = str(results[i]["bounding_box"])
        accuracy = str(round(results[i]["score"],2))
        data.append((f"Rose #{i+1}", coordinates, accuracy,))
        #print(data)
    with open('inferencia.csv','w',newline='') as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerows(data)

def preprocess_image(image_path, input_size):
    """Preprocess the input image to feed to the TFLite model"""
    img = tf.io.read_file(image_path)
    img = tf.io.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.uint8)
    original_image = img
    resized_img = tf.image.resize(img, input_size)
    resized_img = resized_img[tf.newaxis, :]
    return resized_img, original_image


def set_input_tensor(interpreter, image):
    """Set the input tensor."""
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image


def get_output_tensor(interpreter, index):
    """Returns the output tensor at the given index."""
    output_details = interpreter.get_output_details()[index]
    tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
    return tensor


def detect_objects(interpreter, image, threshold):
    """Returns a list of detection results, each a dictionary of object info."""
    # Feed the input image to the model
    set_input_tensor(interpreter, image)
    interpreter.invoke()

    # Get all outputs from the model
    boxes = get_output_tensor(interpreter, 1)
    classes = get_output_tensor(interpreter, 3)
    scores = get_output_tensor(interpreter, 0)
    count = int(get_output_tensor(interpreter, 2))

    results = []
    Nroses = 0
    for i in range(count):
        if scores[i] >= threshold:
            result = {
            'bounding_box': boxes[i],
            'class_id': classes[i],
            'score': scores[i]
            }
            results.append(result)
            Nroses+=1

    print('Number of Red Roses: ', Nroses)
    create_csv(results);
    return results


def run_odt_and_draw_results(image_path, interpreter, threshold=0.5):
    """Run object detection on the input image and draw the detection results"""
    # Load the input shape required by the model
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

    # Load the input image and preprocess it
    preprocessed_image, original_image = preprocess_image(
      image_path,
      (input_height, input_width)
    )

    # Run object detection on the input image
    results = detect_objects(interpreter, preprocessed_image, threshold=threshold)

    # Plot the detection results on the input image
    original_image_np = original_image.numpy().astype(np.uint8)
    for obj in results:
        # Convert the object bounding box from relative coordinates to absolute
        # coordinates based on the original image resolution
        ymin, xmin, ymax, xmax = obj['bounding_box']
        xmin = int(xmin * original_image_np.shape[1])
        xmax = int(xmax * original_image_np.shape[1])
        ymin = int(ymin * original_image_np.shape[0])
        ymax = int(ymax * original_image_np.shape[0])

        # Find the class index of the current object
        class_id = int(obj['class_id'])

        # Draw the bounding box and label on the image
        color = [int(c) for c in COLORS[class_id]]
        cv2.rectangle(original_image_np, (xmin, ymin), (xmax, ymax), color, 2)
        # Make adjustments to make the label visible for all objects
        y = ymin - 15 if ymin - 15 > 15 else ymin + 15
        label = "{}: {:.0f}%".format(classes[class_id], obj['score'] * 100)
        cv2.putText(original_image_np, label, (xmin, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Return the final image
    original_uint8 = original_image_np.astype(np.uint8)
    return original_uint8

DETECTION_THRESHOLD = 0.5
#InputImagePath = sys.argv[1] #'/home/juanchx/Documentos/UNIVERSIDAD/InputRoses.png'
#nameofInput=InputImagePath.split("/")[-1]
#InputImagePath2 = '/home/juanchx/Documentos/UNIVERSIDAD/web/'+nameofInput+'AL.png'  #directory where the system is
#InputImagePathInput= InputImagePath2.split("/")[:-1]
#InputImagePathInput='/'.join(InputImagePathInput)+"/"+nameofInput
arg1 = sys.argv[1]
InputImagePath =  './media/' + arg1
InputImagePath2 =  './media/img.png'

Paths=[["InputImage","OuTputImage"],[InputImagePath,InputImagePath2]]

with open('inferenciapath.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=";")
    writer.writerows(Paths)
    #print(Paths)
#InputImagePathInput= "imagenrepetida.png"


im = Image.open(InputImagePath)
im.thumbnail((512, 512), Image.ANTIALIAS)
im.save(InputImagePath, 'PNG')

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Run inference and draw detection result on the local copy of the original file
detection_result_image = run_odt_and_draw_results(
    InputImagePath,
    interpreter,
    threshold=DETECTION_THRESHOLD
)

# Show the detection result
print(InputImagePath)
print(InputImagePath2)
im=Image.fromarray(detection_result_image)
im.save(InputImagePath2, 'PNG')
#Image.fromarray(detection_result_image)
#cargar los datos en un archivo csv
'''
for i in results:

with oepn('inferencia.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=";")
    writer.
'''
