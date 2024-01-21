import adapter

adapter1:adapter.ClientInterface = adapter.Adapter()
print(adapter1.call_service(123))
adapter2:adapter.ExistingClass = adapter.Adapter2()
print(adapter2.call_service(456))
