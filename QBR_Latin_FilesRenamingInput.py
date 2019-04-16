import os

os.chdir('C:\\Users\\Jasvinder Singh\\Desktop\\ALL_PSV_FILES2') #change the directory

cc = input("What is the country code?") #input for what country files you would like to rename

for name in os.listdir('C:\\Users\\Jasvinder Singh\\Desktop\\ALL_PSV_FILES2'): #for a specific file in the directory, we would like to rename in the manner below

    if name.startswith('GLMA_SATL_MO_Sls_FnCmp_' + str(cc) + '_') and len(name) == 36:
        os.rename(name, name[:26] + '20190408-ETL-' + name[26:])

    elif name.startswith('GLMA_SATL_CTRY_HLDY_'+ str(cc) + '_') and len(name) == 33:
        os.rename(name,name[:23]+'20190408-ETL-'+ name[23:])

    elif name.startswith('GLMA_SATL_MO_Sls_'+ str(cc) + '_') and len(name) == 30:
        os.rename(name,name[:20]+'20190408-ETL-'+ name[20:])

    elif name.startswith('GLMA_SATL_MO_Sls_Anlt_'+ str(cc) + '_') and len(name) == 35:
        os.rename(name,name[:25]+'20190408-ETL-'+ name[25:])

    elif name.startswith('GLMA_SATL_Sls_'+ str(cc) + '_') and len(name) == 27:
        os.rename(name,name[:17]+'20190408-ETL-'+ name[17:])

    elif name.startswith('GLMA_SATL_Sls_Anlt_'+ str(cc) + '_') and len(name) == 32:
        os.rename(name,name[:22]+'20190408-ETL-'+ name[22:])
    else:
        pass
