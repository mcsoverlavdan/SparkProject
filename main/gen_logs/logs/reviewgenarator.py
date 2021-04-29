import pandas as pd
import time
import os
import sys
class NewReviews:

    def __init__(self):
        self.data =None
        self.lengthval =0

    def getting_data(self):
        data1 = pd.read_csv('Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv')
        features = ['name','asins', 'brand', 'primaryCategories', 'reviews.doRecommend', 'reviews.numHelpful', 'reviews.rating', 'reviews.title', 'reviews.text']
        data_df = data1[features].copy()

        data_df.dropna(inplace=True)
        data_df.reset_index(inplace=True)
        temp_data=data_df['reviews.text'].head(10)
        self.data=temp_data
        self.lengthval=len(self.data)

        # print(self.data)
        # print(self.lengthval)
        

    def write_qps(self, dest, qps):
        sleep = 1.0 / qps
        while True:
            self.write(dest, 1)
            time.sleep(sleep)
    
    def write(self, dest, count):
        for i in range(count):
            if self.lengthval>1:
                data =self.data[self.lengthval-1]
                self.lengthval-=1
            else:
                data="over"
            dest.write("%(i)s \"\n" %
                {'i':data})
            dest.flush()


a=NewReviews()
a.getting_data()

a.write_qps(sys.stdout, 1)