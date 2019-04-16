import os

os.chdir('C:\\Users\\Jasvinder Singh\\Desktop\\ALL_PSV_FILES')

for name in os.listdir('C:\\Users\\Jasvinder Singh\\Desktop\\ALL_PSV_FILES'):

    if name.startswith('GLMA_SATL_MO_Sls_FnCmp') and len(name) == 36:
        os.rename(name,name[:26]+'20190408-ETL-'+ name[26:])

    elif name.startswith('GLMA_SATL_CTRY_HLDY') and len(name) == 33:
        os.rename(name,name[:23]+'20190408-ETL-'+ name[23:])

    elif name.startswith('GLMA_SATL_MO_Sls') and len(name) == 30:
        os.rename(name,name[:20]+'20190408-ETL-'+ name[20:])

    elif name.startswith('GLMA_SATL_MO_Sls_Anlt') and len(name) == 35:
        os.rename(name,name[:25]+'20190408-ETL-'+ name[25:])

    elif name.startswith('GLMA_SATL_Sls') and len(name) == 27:
        os.rename(name,name[:17]+'20190408-ETL-'+ name[17:])

    elif name.startswith('GLMA_SATL_Sls_Anlt') and len(name) == 32:
        os.rename(name,name[:22]+'20190408-ETL-'+ name[22:])
    else:
        pass