from page import Page
from ceefax import Ceefax
import config

class ObitPage(Page):
    def __init__(self, n):
        super(ObitPage, self).__init__(n)
        self.importance = 4
        self.title = "Obituaries"
        self.index_num = "260-269"

    def generate_content(self):
        self.print_image(
            "-yyyyyyyy--------yyyyyy--------yyyyyyyyy-------yyyyyyyyy----yyyyyyyyy----------\n"
            "-yyyyyyyy--------yyyyyy--------yyyyyyyyy-------yyyyyyyyy----yyyyyyyyy----------\n"
            "-ybbbbbby----------ybby----------ybbybby---------ybbbbyy------ybbbbby----------\n"
            "-ybbyybby-yyyyyyyy-ybby-yyyyyyyy-ybbybby-yyyyyyy-ybbybby-yyyy-ybbyyyy-yyyyyyyy-\n"
            "-ybbyybby-yyyyyyyy-ybby-yyyyyyyy-ybbybby-yyyyyyy-ybbbbyy-yyyy-ybbbbyy-yyyyyyyy-\n"
            "-ybbyybby-ybbbbbyy-ybby-ybbbbbby-ybbybby-yybbbyy-ybbybby-ybby-ybbyyyy-ybbbbbyy-\n"
            "-ybbbbbby-ybbyybby-ybby-yyybbyyy-ybbbbby-ybbybby-ybbybby-ybby-ybbbbby-ybbyyyyy-\n"
            "-yyyyyyyy-ybbbbbyy-yyyy-yyybbyyy-yyyyyyy-ybbbbby-yyyyyyy-ybby-yyyyyyy-ybbbbbyy-\n"
            "-yyyyyyyy-ybbyybby-yyyy-yyybbyyy-yyyyyyy-ybbybby-yyyyyyy-ybby-yyyyyyy-yyyybbyy-\n"
            "----------ybbbbbyy------yyybbyyy---------ybbybby---------ybby---------ybbbbbyy-\n"
            "--------yyyyyyyyyy----yyyyyyyyyy-------yyyyyyyyy-------yyyyyy-------yyyyyyyyyy-\n"
            "--------yyyyyyyyyy----yyyyyyyyyy-------yyyyyyyyy-------yyyyyy-------yyyyyyyyyy-",1)
        self.print_image(
            "-wwwwwww-wwwwwwwwwwwwwwwwwwwww-wwwwww-wwwwwww\n"
            "ww-----www-----ww-----ww-----www----www--w--w\n"
            "w--www--ww--wwwww--wwwww--wwwww--ww--ww--w--w\n"
            "w--wwwwwww----www----www----www------www---ww\n"
            "w--www--ww--wwwww--wwwww--www-w--ww--ww--w--w\n"
            "ww-----www-----ww-----ww--w---w--ww--ww--w--w\n"
            "-wwwwwww-wwwwwwwwwwwwwwwwww---wwwwwwwwwwwwwww\n"
            "---------------------------------------------",9,16)
        self.print_image(
            "--www-wwww-wwwwwwwww-----------wwwwwwwwwwww-wwwwwwwww-\n"
            "-ww-www---ww-----w-w-----------w----ww----www-ww----ww\n"
            "-w--ww--w--wwww--w-www--wwwwww-w-ww--w-ww--w--ww-ww--w\n"
            "-ww-www----www--ww-w-ww-w----w-www--ww-w-w-ww-wwww--ww\n"
            "-ww-wwww--www--www----w-wwwwww-ww--www--ww-ww-www--www\n"
            "-w---ww--www--ww-www-ww--------w-----ww----w---w-----w\n"
            "-wwwwwwwwwwwwww----www---------wwwwwwwwwwwwwwwwwwwwwww\n"
            "------------------------------------------------------",14,11)
        self.add_newline()

i_p = ObitPage("260")
