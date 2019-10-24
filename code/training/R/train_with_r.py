import os
from azureml.core.run import Run

run = Run.get_context()

os.system("Rscript r_train.r && ls -ltr model.rds")

# upload the model file explicitly into artifacts
model_name = "model.rds"
run.upload_file(name="./outputs/" + model_name, path_or_stream=model_name)
print("Uploaded the model {} to experiment {}".format(
    model_name, run.experiment.name))
# dirpath = os.getcwd()
# print(dirpath)
print("Following files are uploaded ")
print(run.get_file_names())

run.complete()
