import os
# path = '/home/sensebio/Downloads/PNG/'
# files = os.listdir(path)
path = os.getcwd()
# print(path)
for count, filename in enumerate(os.listdir(path)):
    new_name = filename.replace(" ", "_")
    # print(new_name)
    os.rename(os.path.join(path, filename), os.path.join(path,new_name))

