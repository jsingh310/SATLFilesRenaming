import os

os.chdir('C:\\Users\\Jasvinder Singh\\Desktop\\CRG Groups Pre-Renaming May Run') #change the directory

cc = input("What is the country code?") #input for what country files you would like to rename

date = input("What is the date?")

jobid = input("What is the ETL job ID?")

crg = input("What is the CRG code?")

for name in os.listdir('C:\\Users\\Jasvinder Singh\\Desktop\\CRG Groups Pre-Renaming May Run'): #for a specific file in the directory, we would like to rename in the manner below

    if name.startswith('GLMA_SATL_MO_Sls_FnCmp_' + str(cc) + '_') and len(name) == 36: #includes.psv
        os.rename(name, name[:26] + str(date) + '-ETL-' + name[26:])

    elif name.startswith('GLMA_SATL_CTRY_HLDY_'+ str(cc) + '_') and len(name) == 33:
        os.rename(name,name[:23]+ str(date) + '-ETL-' + name[23:])

    elif name.startswith('GLMA_SATL_MO_Sls_'+ str(cc) + '_') and len(name) == 30:
        os.rename(name,name[:20]+ str(date) + '-ETL-' + name[20:])

    elif name.startswith('GLMA_SATL_MO_Sls_Anlt_'+ str(cc) + '_') and len(name) == 35:
        os.rename(name,name[:25]+ str(date) + '-ETL-' + name[25:])

#Now automation for CRG Groups
    elif name.startswith('GLMA_SATL_MO_Sls_Anlt_'+ str(cc) + '_' + str(date) + '_' + str(jobid) + '_' + str(crg)) and len(name) == 49:
        names = name.split("_")
        GLMA = names[0]
        for i in range(1, len(names)):
            if (i < 6):
                GLMA = GLMA + "_" + names[i]
            elif (i == 6):
                GLMA = GLMA + "_" + names[i] + "-ETL-"
            elif (i == 7):
                GLMA = GLMA + names[i]
            else:
                GLMA = GLMA + "_" + names[i]
        os.replace(name,GLMA)

    elif name.startswith('GLMA_SATL_MO_Sls_' + str(cc) + '_' + str(date) + '_' + str(jobid) + '_' + str(crg)) and len(name) == 44:
        names = name.split("_")
        GLMA = names[0]
        for i in range(1, len(names)):
            if (i < 5):
                GLMA = GLMA + "_" + names[i]
            elif (i == 5):
                GLMA = GLMA + "_" + names[i] + "-ETL-"
            elif (i == 6):
                GLMA = GLMA + names[i]
            else:
                GLMA = GLMA + "_" + names[i]
        os.replace(name, GLMA)

    elif name.startswith('GLMA_SATL_Sls_Anlt_' + str(cc) + '_' + str(date) + '_' + str(jobid) + '_' + str(crg)) and len(name) == 46:
        names = name.split("_")
        GLMA = names[0]
        for i in range(1, len(names)):
            if (i < 5):
                GLMA = GLMA + "_" + names[i]
            elif (i == 5):
                GLMA = GLMA + "_" + names[i] + "-ETL-"
            elif (i == 6):
                GLMA = GLMA + names[i]
            else:
                GLMA = GLMA + "_" + names[i]
        os.replace(name,GLMA)

    elif name.startswith('GLMA_SATL_Sls_' + str(cc) + '_' + str(date) + '_' + str(jobid) + '_' + str(crg)) and len(name) == 41:
        names = name.split("_")
        GLMA = names[0]
        for i in range(1, len(names)):
            if (i < 4):
                GLMA = GLMA + "_" + names[i]
            elif (i == 4):
                GLMA = GLMA + "_" + names[i] + "-ETL-"
            elif (i == 5):
                GLMA = GLMA + names[i]
            else:
                GLMA = GLMA + "_" + names[i]
        os.replace(name, GLMA)

    elif name.startswith('GLMA_SATL_MO_Sls_FnCmp_' + str(cc) + '_' + str(date) + '_' + str(jobid) + '_' + str(crg)) and len(name) == 50:
        names = name.split("_")
        GLMA = names[0]
        for i in range(1, len(names)):
            if (i < 6):
                GLMA = GLMA + "_" + names[i]
            elif (i == 6):
                GLMA = GLMA + "_" + names[i] + "-ETL-"
            elif (i == 7):
                GLMA = GLMA + names[i]
            else:
                GLMA = GLMA + "_" + names[i]
        os.replace(name,GLMA)

    else:
        pass
