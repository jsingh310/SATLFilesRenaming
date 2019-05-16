import os

os.chdir('C:\\Users\\Jasvinder Singh\\Desktop\\ETL_20190508_161923') #change the directory

cc = input("What is the country code?") #input for what country files you would like to rename

date = input("What is the date?") #What is the date for the run?

jobid = input("What is the ETL job ID?") #What is the ETL job run id?

for name in os.listdir('C:\\Users\\Jasvinder Singh\\Desktop\\ETL_20190508_161923'): #for a specific file in the directory, we would like to rename in the manner below

    if name.startswith('GLMA_SATL_MO_Sls_FnCmp_' + str(cc) + '_') and len(name) == 36: #If file name beings with GLMA_SATL_MO_Sls_FnCmp_ and has a country code CC and the length is 36 characters then rename
        os.rename(name, name[:26] + str(date) + '-ETL-' + name[26:])

    elif name.startswith('GLMA_SATL_CTRY_HLDY_'+ str(cc) + '_') and len(name) == 33:
        os.rename(name,name[:23]+ str(date) + '-ETL-' + name[23:])

    elif name.startswith('GLMA_SATL_MO_Sls_'+ str(cc) + '_') and len(name) == 30:
        os.rename(name,name[:20]+ str(date) + '-ETL-' + name[20:])

    elif name.startswith('GLMA_SATL_MO_Sls_Anlt_'+ str(cc) + '_') and len(name) == 35:
        os.rename(name,name[:25]+ str(date) + 'ETL-' + name[25:])

    elif name.startswith('GLMA_SATL_Sls_'+ str(cc) + '_') and len(name) == 27:
        os.rename(name,name[:17]+ str(date) + '-ETL-' + name[17:])

    elif name.startswith('GLMA_SATL_Sls_Anlt_'+ str(cc) + '_') and len(name) == 32:
        os.rename(name,name[:22]+ str(date) + '-ETL-' + name[22:])
    else:
        pass
