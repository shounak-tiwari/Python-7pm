from datetime import datetime

# current date print using datetime 


x = datetime.now()

result = x.strftime("%Y %m %M %H %w")
print(result)