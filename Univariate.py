class Univariate():

 def Univariate(dataset):
    quan=[]
    qual=[]
    for columnName in dataset.columns:
        #print(columnName)
        if(dataset[columnName].dtype=='O'):
            #print("qual")
            qual.append(columnName)
        else:
            #print("quan")
            quan.append(columnName)
    return quan,qual   

def freq_Table(columnName, dataset):
    freq_table_df = pd.DataFrame()
    freq_table_df["Unique_Values"] = dataset[columnName].value_counts().index
    freq_table_df["Frequency"] = dataset[columnName].value_counts().values  
    freq_table_df["Relative_Frequency"] = freq_table_df["Frequency"] / len(dataset) 
    freq_table_df["Cumsum"] = freq_table_df["Relative_Frequency"].cumsum() 
    return freq_table_df

def Univariate(dataset,quan):
    descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
    for columnName in quan:
        descriptive.loc["Mean", columnName]=dataset[columnName].mean()
        descriptive.loc["Median", columnName]=dataset[columnName].median()
        descriptive.loc["Mode", columnName]=dataset[columnName].mode()[0]
        descriptive.loc["Q1:25%", columnName]=dataset.describe()[columnName]["25%"]
        descriptive.loc["Q2:50%", columnName]=dataset.describe()[columnName]["50%"]
        descriptive.loc["Q3:75%", columnName]=dataset.describe()[columnName]["75%"]
        descriptive.loc["Q4:100%", columnName]=dataset.describe()[columnName]["max"]
        descriptive.loc["IQR", columnName]= descriptive.loc["Q3:75%", columnName]-descriptive.loc["Q1:25%", columnName]
        descriptive.loc["1.5rule", columnName]=1.5* descriptive.loc["IQR", columnName]
        descriptive.loc["Lesser", columnName]=descriptive.loc["Q1:25%", columnName]-descriptive.loc["1.5rule", columnName]
        descriptive.loc["Greater", columnName]=descriptive.loc["Q3:75%", columnName]+descriptive.loc["1.5rule", columnName]
        descriptive.loc["Min", columnName]=dataset[columnName].min()
        descriptive.loc["Max", columnName]=dataset[columnName].max()
    return descriptive

def Outlier_Column(quan, dataset, descriptive):
    for columnName in quan:
        if dataset[columnName].min() < descriptive[columnName]["Lesser"]:
            lesser.append(columnName)

        if dataset[columnName].max() > descriptive[columnName]["Greater"]:
            greater.append(columnName)

    return lesser, greater

def replace_outliers(dataset, lesser, greater, descriptive):
    for columnName in lesser:
        dataset.loc[dataset[columnName] < descriptive.loc["Lesser", columnName], columnName] = descriptive.loc["Lesser", columnName]
    
    for columnName in Greater:
        dataset.loc[dataset[columnName] > descriptive.loc["Greater", columnName], columnName] = descriptive.loc["Greater", columnName]
    
    return descriptive


