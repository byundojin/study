import base64

class Base64Facade():
    def encode(str):
        return base64.b64encode(str.encode("utf-8")).decode("utf-8")
    def decode(str):
        return base64.b64decode(str.encode("utf-8")).decode("utf-8")
    
msg = "this is facade"
code_msg = Base64Facade.encode(msg)
print(code_msg)
print(Base64Facade.decode(code_msg))