# (c) Wladislaw Waag, 2022-2025
import os, shutil, string

output_dir="_build"
        
def proceed_language(language, language_short):
    if not os.path.exists(os.path.join(output_dir, language_short)):
        os.makedirs(os.path.join(output_dir, language_short));
    f_faqset=open("./faqset_"+language_short+".txt", "r", encoding="utf-8")
    faqset_text=f_faqset.read().split("\n")
    f_faqset.close()
    faq_title=""
    faq_subtitle=""
    sections=[]
    questions=[]
    index=0;
    last_section=-1;
    for line in faqset_text:
        if line[0:9]=="####T####":
            faq_title=line[9:]
        elif line[0:9]=="####U####":
            faq_subtitle=line[9:]
        elif line[0:3]=="###":
            sections.append(line[8:]);
        elif line[0:2]=="##":
            dictfrage={}
            dictfrage["section"]=int(line[2:4])
            if(last_section==dictfrage["section"]):
                index=index+1;
            else:
                index=1;
            last_section=dictfrage["section"];
            dictfrage["question"]=line[6:].split("##")[0]
            if(len(line[6:].split("##"))>1):
                dictfrage["url"]=line[6:].split("##")[1]
            else:
                dictfrage["url"]="tab"+str(dictfrage["section"])+"faq"+str(index)
            dictfrage["answer"]=""
            questions.append(dictfrage);
        else:
            if len(questions)>0 and len(line)>0:
                if len(questions[-1]["answer"])>0:
                    insertbr="<br>"
                else:
                    insertbr=""
                questions[-1]["answer"]=questions[-1]["answer"]+insertbr+line
    #print(questions)
  
    #generate sections page
    sectn=0;
    for sect in sections:
        html_questions=""
        html_sections=""
        sectn=sectn+1;
        
        secnumber=0;
        for section in sections:
            secnumber=secnumber+1;
            tab_href='tab'+str(secnumber)+'.html';
            if(secnumber==1):
                tab_href='index.html';
            html_sections=html_sections+'<a href="'+tab_href+'" class="nav-link'+(" active" if secnumber==sectn else "")+'" aria-selected="'+("true" if secnumber==sectn else "false")+'" aria-controls="tab'+str(secnumber)+'">'+section+'</a>\n';
        qustionnumber=0;
        for question in questions:
            if(question["section"]==sectn):
                qustionnumber=qustionnumber+1;
                html_questions=html_questions+'<li><a href="'+question["url"]+'.html">'+question["question"]+'</a></li>\n';
        
        #print(html_sections)
        #print(html_questions)    
        dict={}
        dict["TITLE"]=faq_title;
        dict["SUBTITLE"]=faq_subtitle;    
        dict["SECTIONS"]=html_sections; 
        dict["QUESTIONS"]=html_questions; 
        f_template=open("faq_template_"+language_short+".html", "r", encoding="utf-8")
        template=string.Template(f_template.read())
        tab_href='tab'+str(sectn)+'.html';
        if(sectn==1):
            tab_href='index.html';
        f_index= open(os.path.join(output_dir, language_short, tab_href),"w+", encoding="utf-8")
        f_index.write(template.substitute(dict))
        f_index.close()
        f_template.close()
        
    #generate question pages
    questn=0;
    for quest in questions:
        questn=questn+1;
        html_sections="";
        secnumber=0;
        for section in sections:
            secnumber=secnumber+1;
            tab_href='tab'+str(secnumber)+'.html';
            if(secnumber==1):
                tab_href='index.html';
            html_sections=html_sections+'<a href="'+tab_href+'" class="nav-link'+(" active" if secnumber==quest["section"] else "")+'" aria-selected="'+("true" if secnumber==quest["section"] else "false")+'" aria-controls="tab'+str(secnumber)+'">'+section+'</a>\n';
        
        html_questions=""
        qustionnumber=0;
        for question in questions:
            qustionnumber=qustionnumber+1;
            if(question["section"]==quest["section"]):
                html_questions=html_questions+'<li'+(' itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"' if qustionnumber==questn else'')+'><a href="'+question["url"]+'.html"><span'+(' itemprop="text"'  if qustionnumber==questn else'')+'>'+question["question"]+'</span></a>\n';
                if(qustionnumber==questn):
                    QAnswer = question["answer"].replace("WLED Compile Helper",'<a href="https://wled-compile.github.io" target="_blank" rel="noopener">WLED Online Compiler</a>').replace("WLED Calculator",'<a href="https://wled-calculator.github.io" target=”_blank” rel="noopener">WLED Calculator</a>').replace("WLED Installer",'<a href="https://wled-install.github.io" target=”_blank” rel="noopener">WLED Installer</a>').replace("fertige WLED Controller",'<a href="https://shop.myhome-control.de" target=”_blank” rel="noopener">fertige WLED Controller</a>').replace("fertigen WLED Controller",'<a href="https://shop.myhome-control.de" target=”_blank” rel="noopener">fertigen WLED Controller</a>').replace("ready-made WLED controllers",'<a href="https://shop.myhome-control.de" target=”_blank” rel="noopener">ready-made WLED controllers</a>').replace("LED FX",'<a href="https://github.com/LedFx/LedFx" target=”_blank” rel="noopener">LED FX</a>').replace("xLights",'<a href="http://xlights.org/" target=”_blank” rel="noopener">xLights</a>').replace("готовый WLED-контроллер",'<a href="https://shop.myhome-control.de" target=”_blank” rel="noopener">готовый WLED-контроллер</a>').replace("готові WLED-контролери",'<a href="https://shop.myhome-control.de" target=”_blank” rel="noopener">готові WLED-контролери</a>').replace("WLED-калькулятора",'<a href="https://wled-calculator.github.io" target=”_blank” rel="noopener">WLED-калькулятора</a>').replace("WLED-калькулятор",'<a href="https://wled-calculator.github.io" target=”_blank” rel="noopener">WLED-калькулятор</a>').replace('ABC! WLED V43 & compatible','<a href="https://shop.myhome-control.de/Ethernet-Adapter-fuer-WLED-Controller/HW10016" target=”_blank” rel="noopener">ABC! WLED V43 & compatible</a>').replace('ABC! WLED V43 Controller','<a href="https://shop.myhome-control.de/Ethernet-Adapter-fuer-WLED-Controller/HW10016" target=”_blank” rel="noopener">ABC! WLED V43 Controller</a>').replace('PWM Board','<a href="https://shop.myhome-control.de/WLED-PWM-Board/HW10024" target=”_blank” rel="noopener">PWM Board</a>').replace('PWM board','<a href="https://shop.myhome-control.de/WLED-PWM-Board/HW10024" target=”_blank” rel="noopener">PWM board</a>').replace('Switch Board','<a href="https://shop.myhome-control.de/ABC-WLED-Switch-Board/HW10021" target=”_blank” rel="noopener">Switch Board</a>');
                    for picnumber in range(100):
                            QAnswer=QAnswer.replace('[pic'+str(picnumber)+']', '<img src="../pictures/pic'+str(picnumber)+'.jpg" class="img-fluid">')
                    html_questions=html_questions+'<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><div itemprop="text"><p>'+QAnswer+'</div></div>\n'
                    
                    
                html_questions=html_questions+'</li>\n';
        
        #print(html_sections)
        #print(html_questions)    
        dict={}
        dict["TITLE"]=faq_title;
        dict["SUBTITLE"]=faq_subtitle;    
        dict["SECTIONS"]=html_sections; 
        dict["QUESTIONS"]=html_questions; 
        f_template=open("faq_template_"+language_short+".html", "r", encoding="utf-8")
        template=string.Template(f_template.read())
        f_index= open(os.path.join(output_dir, language_short, quest["url"].replace(" ","_").replace("?","")+".html"),"w+", encoding="utf-8")
        f_index.write(template.substitute(dict))
        f_index.close()
        f_template.close()
   
    
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
shutil.copyfile("index.css", os.path.join(output_dir,"index.css"))
shutil.copyfile("index.html", os.path.join(output_dir,"index.html"))
shutil.copyfile("google86f84e541110ff0a.html", os.path.join(output_dir,"google86f84e541110ff0a.html"))
shutil.copyfile("sitemap.xml", os.path.join(output_dir,"sitemap.xml"))
if os.path.exists(os.path.join(output_dir,'pictures')):
    shutil.rmtree(os.path.join(output_dir,'pictures'))
shutil.copytree('pictures',os.path.join(output_dir,'pictures'))

proceed_language("deutsch", "de");
proceed_language("english", "en");
proceed_language("russian", "ru");
proceed_language("ukrain", "ua");
                




