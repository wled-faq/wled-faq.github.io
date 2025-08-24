# (c) Wladislaw Waag, 2022-2025
import os, shutil, string
        
def proceed_language(language, language_short):
    f_faqset=open("./faqset_"+language_short+".txt", "r", encoding="utf-8")
    faqset_text=f_faqset.read().split("\n")
    f_faqset.close()
    faq_title=""
    faq_subtitle=""
    sections=[]
    questions=[]
    index=0;
    last_section=-1;
    f_faqset=open("./faqset_"+language_short+"_.txt", "w", encoding="utf-8")
    
    for line in faqset_text:
        if line[0:9]=="####T####":
            f_faqset.write(line+'\n');
        elif line[0:9]=="####U####":
            f_faqset.write(line+'\n');
        elif line[0:3]=="###":
            f_faqset.write(line+'\n');
        elif line[0:2]=="##":
            dictfrage={}
            dictfrage["section"]=int(line[2:4])
            if(last_section==dictfrage["section"]):
                index=index+1;
            else:
                index=1;
            last_section=dictfrage["section"];
            dictfrage=line[6:].split("##")[0]
            f_faqset.write(line+'##'+dictfrage.replace(" ","_").replace("?","").replace("ä","ae").replace("ü","ue").replace("ö","oe").replace("Ä","Ae").replace("Ü","Ue").replace("Ö","Oe").replace("ß","ss").replace(".","").replace(",","").replace("(","").replace(")","").replace("-","_").replace("\"","").replace("'","_").replace("„","").replace("“","")+'\n');
        else:
            f_faqset.write(line+'\n');
    f_faqset.close()
    

proceed_language("deutsch", "de");
proceed_language("english", "en");
                




