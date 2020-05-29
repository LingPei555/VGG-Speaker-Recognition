import os
from random import choice
import random
test_data_path='../test_wav'
txt_data_path='../meta/vox1_test.txt'
def generate_txt(data_path,txt_path):
    id= os.listdir(data_path)
    list=[]
    f=open(txt_path,'w')
    for id_num in id:
        id_path = os.path.join(data_path, id_num)
        parent = os.listdir(id_path)
        for parent_num in parent:
            _=os.path.join(id_path,parent_num)
            parent_path=os.path.join(id_num,parent_num)
            child=os.listdir(_)
            for child_num in child:
                audio_path=os.path.join(parent_path, child_num)
                final_path=audio_path.replace('\\','/')
                list.append(final_path)
    for i in range(len(list)):
        for j in range(4):
            if j%2==0:
                same_id=list[i].split('/')[0]
                same_parent=list[i].split('/')[1]
                list1=os.path.join(data_path,same_id)
                list1_dir=os.listdir(list1)
                b=random.sample(list1_dir,2)
                if b[0]==same_parent:
                    dif_parent=b[1]
                else:
                    dif_parent=b[0]
                add_parent1=os.path.join(same_id,dif_parent)
                list2=os.path.join(data_path,add_parent1)
                list2_dir=os.listdir(list2)
                add_child1=os.path.join(add_parent1,choice(list2_dir))
                add_child_path1=add_child1.replace('\\','/')
                f.write(str(1) + ' ' + str(list[i])+' '+str(add_child_path1))
                f.write('\n')
            else:
                a=random.sample(id,2)
                if a[0]==same_id:
                    dif_id=a[1]
                else:
                    dif_id=a[0]
                list3=os.path.join(data_path,dif_id)
                list3_dir=os.listdir(list3)
                add_parent2=os.path.join(dif_id,choice(list3_dir))
                list4=os.path.join(data_path,add_parent2)
                list4_dir=os.listdir(list4)
                add_child2=os.path.join(add_parent2,choice(list4_dir))
                add_child_path2=add_child2.replace('\\','/')
                f.write(str(0) + ' ' + str(list[i])+' '+str(add_child_path2))
                f.write('\n')
generate_txt(test_data_path,txt_data_path)



