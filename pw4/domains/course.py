class Course:
    def __init__(self, course_id="", name="", credits=0):
        self.__idc = course_id
        self.__namec = name
        self.__credits = credits

    def get_idc(self): return self.__idc
    def get_namec(self): return self.__namec
    def get_credits(self): return self.__credits

    def list(self):
        print(f"ID: {self.__idc} | Course: {self.__namec} | Credits: {self.__credits}")