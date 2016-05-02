from page import Page
from colours import colour_print
from printer import instance as printer
from random import choice
from textwrap import wrap

class TubePage(Page):
    def __init__(self,page_num):
        super(TubePage, self).__init__(page_num)
        self.title = "Tube Line Status"

    def generate_content(self):
        import tubestatus
        content = colour_print(printer.text_to_ascii("Tube Lines"))
        content += "\n"
        # Create a new status object for retrieving data
        current_status = tubestatus.Status()
        # Get a list of tube lines
        lines = current_status.list_lines()
        # Loop through the lines and print the status of each one
        lines_tube = [lines[i] for i in [1,2,12,4,10,0,3,14,5,7,11]]
        lines_other = [lines[i] for i in [8,6,13,9]]
        colours_tube = [self.colours.Background.YELLOW,
                        self.colours.Background.RED,
                        self.colours.Background.YELLOW+self.colours.Style.BLINK,
                        self.colours.Background.GREEN,
                        self.colours.Background.MAGENTA+self.colours.Style.BLINK,
                        self.colours.Style.BLINK,
                        self.colours.Background.MAGENTA,
                        self.colours.Background.DEFAULT,
                        self.colours.Background.BLUE,
                        self.colours.Background.BLUE+self.colours.Style.BLINK,
                        self.colours.Background.CYAN+self.colours.Style.BLINK]
        colours_tube_text = [self.colours.Foreground.WHITE, 
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.BLACK,
                        self.colours.Foreground.BLACK,
                        self.colours.Foreground.BLACK,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.WHITE,
                        self.colours.Foreground.BLACK]
                        
        colours_other = [self.colours.Background.CYAN,
                        self.colours.Background.YELLOW,
                        self.colours.Background.BLUE,
						self.colours.Background.GREEN+self.colours.Style.BLINK]  
        colours_other_text = [self.colours.Foreground.BLACK, 
                        self.colours.Foreground.BLACK,
                        self.colours.Foreground.WHITE,
						self.colours.Foreground.BLACK]
                        
        mapping = [ ('There is a GOOD SERVICE on the rest of the line.', ''), 
                    ('GOOD SERVICE on the rest of the line.', ''),
                    ('There is a GOOD SERVICE on all other routes.', ''), 
                    ('GOOD SERVICE on all other routes.', ''),
                    ('GOOD SERVICE on other London Overground routes.', ''),
                    ('GOOD SERVICE on other London Overground routes', ''),                    
                    ('The service will resume again at 0615 on Monday.', ''), 
                    ('The service will resume again at 0615 tomorrow.', ''),
                    ('The service will resume again at 0615.', ''), 
                    ('Train service will resume at 06:15 tomorrow.', ''),
                    ('No service between ', ''),
                    #('Minor delays ', ''),
                    (' due to planned engineering work.', ''),
                    (' due to planned work.', ''),   
                    #('due to ', ''),                    
                    ('King\'s Cross St. Pancras', 'KX'),
                    ('Kings Cross St. Pancras', 'KX'),
                    ('Tottenham Court Road', 'TCR'),
                    ('Highbury & Islington', 'H&I'),
					('Harrow & Wealdstone', 'H&W'),
                    ('Cross', 'X'),
                    ('Road', 'Rd'),    
                    ('Square', 'Sq'),
                    ('Street', 'St'),                                        
                    ('Junction', 'Jn'),  
                    ('Town', 'Tn'),   
                    ('Park', 'Pk'),
                    ('Lane', 'Ln'),
					('Hill', 'Hl'),
					('Central','Ctl'),
					('North ','N '),
					('South ','S '),
					('East ','E '),
					('West ','W '),
                    (' and ','-'),
                    ('between ',''),
                    (' to ','-')]   
        
        content_bad_service = ""
        content_good_service = ""
        linei = 0
        for line in lines_tube + lines_other:
            contentT = "\n  "
            contentT += colours_tube[linei] + colours_tube_text[linei]
            #line = line.replace("and","&")
            contentT += " " + str(line).replace("and","&") +" "*(20-len(str(line).replace("and","&")))
            contentT += self.colours.Background.DEFAULT
            desc = current_status.get_status(line).description
            if desc == "Good Service":
                contentT += self.colours.Foreground.GREEN+self.colours.Style.BOLD
            elif desc == "Minor Delays":
                contentT += self.colours.Foreground.YELLOW+self.colours.Style.BOLD
            elif desc == "Part Closure":
                contentT += self.colours.Foreground.YELLOW
            else:
                contentT += self.colours.Foreground.RED+self.colours.Style.BOLD
            full_description = " "
            full_description += current_status.get_status(line).description
            description = current_status.get_status(line).status_details
            for k, v in mapping:
                description = description.replace(k, v)
            if len(description)>1:
                full_description += ": " + description
            contentT += wrap(full_description,56)[0] 
            for line in wrap(full_description,56)[1:]:
                contentT += "\n"+" "*24 + line  
                
            contentT += self.colours.Foreground.DEFAULT

            if desc == "Good Service":
			    content_good_service+=contentT
            else
                content_bad_service+=contentT
            linei += 1
        #content += "\n"
        linei = 0
        '''
        for line in lines_other:
            contentT += "\n  "
            content += colours_other[linei] + colours_other_text[linei]            
            content += " " + str(line).replace("and","&") +" "*(20-len(str(line).replace("and","&")))
            content += self.colours.Background.DEFAULT
            desc = current_status.get_status(line).description
            if desc == "Good Service":
                content += self.colours.Foreground.GREEN+self.colours.Style.BOLD
            elif desc == "Minor Delays":
                content += self.colours.Foreground.YELLOW+self.colours.Style.BOLD
            elif desc == "Part Closure":
                content += self.colours.Foreground.YELLOW
            else:
                content += self.colours.Foreground.RED+self.colours.Style.BOLD
            full_description = " "
            full_description += current_status.get_status(line).description            
            description = current_status.get_status(line).status_details
            for k, v in mapping:
                description = description.replace(k, v)
            if len(description)>1:
                full_description += ": " + description
            content += wrap(full_description,56)[0] 
            for line in wrap(full_description,56)[1:]:
                content += "\n"+" "*24 + line
            
            content += self.colours.Foreground.DEFAULT
            linei += 1        
        '''
        content += content_bad_service + "\n" + content_good_service

        self.content = content

page = TubePage("101")
