# (c) Wladislaw Waag, 2022-2023 
import os, shutil, string

output_dir="_build"
        
def proceed_language(language, language_short, filename):
    f_faqset=open("./faqset_"+language_short+".txt", "r", encoding="utf-8")
    faqset_text=f_faqset.read().split("\n")
    f_faqset.close()
    faq_title=""
    faq_subtitle=""
    sections=[]
    questions=[]
    for line in faqset_text:
        if line[0:9]=="####T####":
            faq_title=line[9:]
        elif line[0:9]=="####U####":
            faq_subtitle=line[9:]
        elif line[0:3]=="###":
            sections.append(line[8:])
        elif line[0:2]=="##":
            dictfrage={}
            dictfrage["section"]=int(line[2:4])
            dictfrage["question"]=line[6:]
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
    
    html_sections=""
    html_questions=""
    
    secnumber=0;
    for section in sections:
        secnumber=secnumber+1;
        html_sections=html_sections+'<a href="#tab'+str(secnumber)+'" class="nav-link'+(" active" if secnumber==1 else "")+'" data-bs-toggle="pill" role="tab" aria-controls="tab'+str(secnumber)+'" aria-selected="'+("true" if secnumber==1 else "false")+'">'+section+'</a>\n';
        
        html_questions=html_questions+'<div class="tab-pane'+((" show active" if secnumber==1 else ""))+'" id="tab'+str(secnumber)+'" role="tabpanel" aria-labelledby="tab'+str(secnumber)+'"><div class="accordion" id="accordion-tab-'+str(secnumber)+'">\n';
        qustionnumber=0;
        for question in questions:
            if question["section"]==secnumber:
                qustionnumber=qustionnumber+1;
                QAnswer = question["answer"].replace("WLED Calculator",'<a href="https://wled-calculator.github.io" target=”_blank” rel="noopener">WLED Calculator</a>').replace("WLED Installer",'<a href="https://wled-install.github.io" target=”_blank” rel="noopener">WLED Installer</a>').replace("fertige WLED Controller",'<a href="https://shop.myhome-control.de" target=”_blank” rel="noopener">fertige WLED Controller</a>').replace("ready-made WLED controllers",'<a href="https://shop.myhome-control.de" target=”_blank” rel="noopener">ready-made WLED controllers</a>');
                
                html_questions=html_questions+'<div class="accordion-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">\n<div class="accordion-header" id="accordion-tab-'+str(secnumber)+'-heading-'+str(qustionnumber)+'">\n<h5>\n<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-tab-'+str(secnumber)+'-content-'+str(qustionnumber)+'" aria-expanded="false" aria-controls="accordion-tab-'+str(secnumber)+'-content-'+str(qustionnumber)+'">'+'<a href="#tab'+str(secnumber)+'faq'+str(qustionnumber)+'"><div itemprop="name">'+question["question"]+'</div></a>'+'</button>\n</h5>\n</div>\n<div class="collapse'+(" show" if qustionnumber==1 else "")+'" id="accordion-tab-'+str(secnumber)+'-content-'+str(qustionnumber)+'" aria-labelledby="accordion-tab-'+str(secnumber)+'-heading-'+str(qustionnumber)+'" data-bs-parent="#accordion-tab-'+str(secnumber)+'">\n<div class="accordion-body" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><div itemprop="text"><p>'+QAnswer+'</p></div>\n</div>\n</div>\n</div>\n'
        html_questions=html_questions+'</div></div>\n';
        
    #print(html_sections)
    #print(html_questions)    
    dict={}
    dict["TITLE"]=faq_title;
    dict["SUBTITLE"]=faq_subtitle;    
    dict["SECTIONS"]=html_sections; 
    dict["QUESTIONS"]=html_questions; 
    f_template=open("faq_template_"+language_short+".html", "r", encoding="utf-8")
    template=string.Template(f_template.read())
    f_index= open(os.path.join(output_dir,filename),"w+", encoding="utf-8")
    f_index.write(template.substitute(dict))
    f_index.close()
    f_template.close()
   
    
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
shutil.copyfile("index.css", os.path.join(output_dir,"index.css"))
shutil.copyfile("google86f84e541110ff0a.html", os.path.join(output_dir,"google86f84e541110ff0a.html"))

proceed_language("deutsch", "de", "index.html");
proceed_language("english", "en", "en.html");
                
