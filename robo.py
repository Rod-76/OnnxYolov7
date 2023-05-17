from roboflow import Roboflow
rf = Roboflow(api_key="JFT1i8n3TmgoKWO6TVax")
project = rf.workspace().project("white-oyster-mushroom")
model = project.version(1).model
img = "49.jpg"

# infer on a local image
print(model.predict(img, confidence=40, overlap=30).json())

# visualize your prediction
model.predict(img, confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())