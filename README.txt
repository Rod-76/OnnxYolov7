--Install miniconda
https://docs.conda.io/en/latest/miniconda.html#windows-installers


--Open Anaconda Prompt as Administrator then type
conda -V


--Update the conda environment 
conda update conda


--Create anaconda virtual environment
conda create -n pythonenv python=3.10


--Activate virtual environment
conda activate pythonenv

# To deactivate an active environment
conda deactivate


--Go to AI Directory
cd C:\Users\jemar\Desktop\Python Projects\OpenCV\RoboFlow\OnnxYolov7\


--Install requirements
pip install -r requirements.txt


--Download test model(optional)
wget https://github.com/Rod-76/OnnxYolov7/releases/download/onnx/yolov7.onnx


--Run main program
python onnxTest.py