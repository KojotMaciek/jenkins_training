largest = None
smallest = None
count = 0
total = 0

#Sprawdzam czy wartosci startowe są None - to taki test, jakby np ten kod byl czescią czegoś większego
if largest is None and smallest is None:

    while True:
        #pytam o liczbę
        num = raw_input('Enter a number: ')
        
        #jak mi sie znudzi podawanie licz to zabawa się kończy
        if num == "done" : break
        
        #prubujemy to co user podał zamienić na floata, jak poda zle to pyta znowu z komunikatem
        try:
            num = float(num)
        except:
            print 'Invalid input' 
            continue
        #jak podal user liczbe to doliczamy to do zliczarki    
        count = count + 1
        
        #wartosci startowe są None więc, żeby to ruszyło trzeba None zastąpić pierwszą podaną liczbą
        if largest is None and smallest is None:    
            largest = num
            smallest = num    
            
        #tutaj jest sortowanie, czyli sprawdza czy to co podałem jest mniejsze/większe od poprzednio podanej    
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
            
        #sumowanie podanych liczb
        total = total + num
        
        #wyciąganie średniej
        average = float("%.2f" % (total / count))
        
else:
    print "Not none values"

print "Maximum is", largest
print "Minimum is", smallest
print "Count is", count
print "Average is", average