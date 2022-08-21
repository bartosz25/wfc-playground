Check the demo video: https://www.youtube.com/watch?v=7u262G3biU4 

1. Start Storage Account: Azurite > Start (Visual Studio)

2. Start Storage Explorer: from UI


3. Start the function - PyCharm's terminal:
```
func start
```

4. Test the function:
- call 3 time to notice the state store in the blob: http://localhost:7071/api/event_handler?run_id=123456&hellos_count=2
- call to see the orchestration http://localhost:7071/api/event_handler?run_id=654321&hellos_count=2 
