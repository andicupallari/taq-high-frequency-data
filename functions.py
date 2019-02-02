#%% For each stock, get opening price: 
import numpy as np
pseries['ref price']=np.nan
def get_open_price(frame):
    frame['ref price'].iloc[0]=priceopenprint.loc[frame['SYM_ROOT'].iloc[10],'PRICE']
    return frame

data=pseries.groupby('SYM_ROOT').apply(get_open_price)


#%%
from datetime import timedelta
def calculate_ref_price(frame):
    frame=frame.drop(columns=['EX', 'TR_SCOND'])
    frame.set_index('datetime',inplace=True)
    for index in frame.index:
        if frame.loc[index,'ref price'].notnull():
            frame['ref price'].loc[index:index+timedelta(seconds=30)]=frame['ref price'].at[index]
            
            
        
    
    return frame
data.groupby('SYM_ROOT').apply(calculate_ref_price)