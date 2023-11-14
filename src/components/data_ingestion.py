import tensorflow as tf
import os
import sys
from src.exception import CustomException
from src.logger import logging
#from sklearn.model_selection import train_test_split
from dataclasses import dataclass



'''datadir="D:\\Potato disease\\artifacts"

dataset= tf.keras.preprocessing.image_dataset_from_directory(
    datadir,
    shuffle= True,
    image_size= (256,256),
    batch_size= 32
)
logging.info("Loading dataset")'''

@dataclass
class dataingestionconfig:
    train_data_path= os.path.join('artifacts','train_data')
    test_data_path= os.path.join ('artifacts','test_data')
    
class dataingestion:
    def __init__(self):
        self.ingestion_config= dataingestionconfig()
    
    def initiate_data_ingestion(self):
        
            dataset=tf.keras.preprocessing.image_dataset_from_directory(
                "D:\\Potato disease\\artifacts",
                logging.info("reading images dataset"),
                shuffle=True,
                batch_size=32,
                image_size=(256,256)
            )
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
    def data_split(ds, train_split=0.8, val_split=0.1, test_split=0.1, shuffle=True,shuffle_size=10000):
            


            
            dataset=tf.keras.preprocessing.image_dataset_from_directory(
                "D:\\Potato disease\\artifacts",
                logging.info("reading images dataset"),
                shuffle=True,
                batch_size=32,
                image_size=(256,256)
            )
            #train_ds= dataset.take(54)
            #test_ds= dataset.skip(54)
            #val_ds= test_ds.take(6)

            
    
            ds_size=len(dataset)


            #if shuffle:
                #ds= ds.shuffle(shuffle_size,seed=12)

            train_data= int(train_split*ds_size)
            val_size= int(val_split*ds_size)

            train_ds=ds.take(train_data)
            val_ds= ds.take(val_size)
            test_ds=ds.skip(train_data).skip(val_size)
                    
            return train_ds,val_ds,test_ds
        

if __name__=="__main__":
    obj=dataingestion()
    train_data,test_data=obj.data_split()


    


