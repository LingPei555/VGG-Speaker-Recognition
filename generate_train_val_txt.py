import os
from sklearn.model_selection import train_test_split

path='../train_wav'
train_txt='../meta/vox2_train.txt'
val_txt='../meta/vox2_val.txt'
def generate_txt(path):
    datasets = os.listdir(path)
    i = 0
    data_list=[]
    label=[]
    for dataset in datasets:
        dataset_path = os.path.join(path, dataset)
        second_datasets = os.listdir(dataset_path)
        for second_dataset in second_datasets:
            audio_path = os.path.join(dataset_path, second_dataset)
            audio_path2 = os.path.join(dataset, second_dataset)
            audio_datasets = os.listdir(audio_path)
            for audio_dataset in audio_datasets:
                audio = os.path.join(audio_path2, audio_dataset)
                audio_path = audio.replace('\\', '/')
                data_list.append(audio_path)
                label.append(i)
        i += 1
    return data_list,label

def write_txt(x,y,txt_path):
    txt=open(txt_path,'w')
    for j in range(len(x)):
        txt.write(str(x[j])+' '+str(y[j]))
        txt.write('\n')
    txt.close()


dataset,labels=generate_txt(path)
x_train,x_val,y_train,y_val=train_test_split(dataset,labels,test_size=0.2,random_state=1)
write_txt(x_train,y_train,train_txt)
write_txt(x_val,y_val,val_txt)


