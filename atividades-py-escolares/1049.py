animal = {
    'vertebrado' : {
        'ave': {
                'onivoro':"pomba",
                'carnivoro':"aguia"
            }, 
        'mamífero': {
            'onivoro':"homem",
            'herbivoro':"lagarta"
        }
        
    },
    'invertebrado' : {
        'anilideo': {
                'hematofogo':"pulga",
                'herbivoro':"lagarta"
            }, 
        'anelideo': {
            'hematofogo':"sanguessuga",
            'onivoro':"minhoca"
        }
        
    }    
}

n1 = input()
n2 = input()
n3 = input()

if n1 == 'vertebrado' and n2 == 'ave'and n3 == 'carnivoro' :
    print("aguia")
elif n1 == 'vertebrado' and n2 == 'ave' and n3 == 'onivoro' :
    print("pomba")
elif n1 == 'vertebrado' and n2 == 'mamifero' and n3 == 'onivoro' :
    print("homem")
elif n1 == 'vertebrado' and n2 == 'mamifero' and n3 == 'herbivoro' :
    print("vaca")
elif n1 == 'invertebrado' and n2 == 'inseto' and n3 == 'hematofago' :
    print("pulga")
elif n1 == 'invertebrado' and n2 == 'inseto' and n3 == 'herbivoro' :
    print("lagarta")
elif n1 == 'invertebrado' and n2 == 'anelideo' and n3 == 'hematofago' :
    print("sanguessuga")
elif n1 == 'invertebrado' and n2 == 'anelideo' and n3 == 'onivoro' :
    print("minhoca")