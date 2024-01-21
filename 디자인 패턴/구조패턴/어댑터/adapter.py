import service

# 대충 인터패이스라 생각 하셈
class ClientInterface():
    def call_service(data:int):
        pass

class Adapter(service.Service, ClientInterface):
    def call_service(self, data:int):
        special_data = str(data)
        return Adapter.service(special_data)
    
# 다중상속 되는 언어만 가능
class ExistingClass():
    def call_service(data:int):
        pass

class Adapter2(service.Service, ExistingClass):
    def call_service(self, data:int):
        special_data = str(data)
        return Adapter2.service(special_data)