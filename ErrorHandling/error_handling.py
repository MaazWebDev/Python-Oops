file = open('youtube.txt','w')

try:
    file.write('Welcome To Youtube')
finally:
    file.close()

with open('youtube.txt','w') as file:
    file.write('Welcome To My Python')