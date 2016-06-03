from re import sub
from page import Page
from colours import colour_print
from printer import instance as printer
from time import strftime
import screen


class JigPage(Page):
    def __init__(self,page_num):
        super(JigPage, self).__init__(page_num)
        self.in_index = False
        self.title = "SCORPIONS"
        self.tagline = "SCORPIONS"

    def generate_content(self):
        import urllib2
        content = colour_print(printer.text_to_ascii("SCORPIONS",fill=True, vertical_condense=True))
        content += "\n"
        jig = """
       `.'##';.`                                                   
       +@#@@#; #@.      :#,                                        
         .+@#+# .+,      `',   :#`                                 
          `:+#';';;':    ;+',  ,#.   :+           `,,,,,,          
              .`#; ,+;   :;', `+#,  :+,  `     .;#+.+:  ,@'#;`     
                 ++++,   +'+: `#;  ;',   +.   :#:'';.;@'.#` ,',    
                  ;;`;'  ',;; .#` :#;     ;##@#,          `#::':   
                  ;#++` .:,:..@; ,#:  .+'  .,.             '` ;;   
                  .;.`# .:::..'@:;;;;;;:                    +#+:   
                 ` :@+#+';#;;+,+,+@#+++;```                +`,#;   
                 '##'`;. '.;;.# ,:`,;;'+####+,        `;++@,;##:   
                 +#,,' # ;`:; `, '.';.;,@;;;;,:;''::,,'' .''.      
               `+':`.+`'`;`:; `, ,.;:,: @#@#,,';@:...,'#@++        
                :#++@+.#`+'+;,+.;+,':.'';#;##;;+:+;:`:,            
               .#@@@#'@'##;`,#+;@:+..+@@+@@##+.                    
               `+@@####++:;#+,,:;:;#@#+'@+:`                       
                  ;+'#:@;##+#@#;#+#;,.`                            
                 ,';;' +.':.,'',':,'+:`                            
              `.#:`,,  :',:;,`:`'`  ,#+                            
           .``#` ;.   .#' '',.`#.  `,''                            
       `;##@#,@''.   ,;',.:+:`;;@`   ``                            
    `++@@+,`,'+   .:,'@. .'+,.#+                                   
    `##@++##+:    ,''`  ,'#..#'                                    
      ,.                         

"""
        content += jig
        
        self.content = content

page = JigPage("116")
