corinthians=0
palmeiras=0
santos=0
saopaulo=0
outro=resp='sim'
while (resp=='sim'):
    time = int('Qual time você torce: corinthians, palmeiras...ou outro1')
    if(time == 'corinthians'):
        corinthians= corinthians+1
    elif(time == 'palmeiras'):
        palmeiras= palmeiras+1
    elif(time == 'santos'):
        santos= santos+1
    elif(time == 'saopaulo'):
        saopaulo= saopaulo+1
    else:
        outro= outro+1
    total= total+1  
    resp = input('Deseja continuar: sim ou não')
percco = (corinthians/total)*100
percsan = (santos/total)*100
percpal = (palmeiras/total)*100
percsao = (saopaulo/total)*100
percout = (outro/total)*100 
print(f'corinthians:{percco}%')
print(f'palmeiras:{percpal}')
print(f'santos:{percsan}')
print(f'saopaulo:{percsao}')


    

