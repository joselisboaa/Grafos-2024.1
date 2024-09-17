def stableMatching(n, menPreferences, womenPreferences):
    # Lista de homens solteiros (inicialmente todos os homens)
    unmarriedMen = list(range(n))
    
    # Lista para armazenar o cônjuge de cada homem (inicialmente vazio)
    manSpouse = [None] * n
    
    # Lista para armazenar o cônjuge de cada mulher (inicialmente vazio)
    womanSpouse = [None] * n
    
    # Lista que rastreia quantas propostas cada homem fez (começam com 0)
    nextManChoice = [0] * n
    
    # Enquanto houver homens solteiros:
    while unmarriedMen:
        # Pegamos um homem que está solteiro
        he = unmarriedMen[0]
        
        # Preferências do homem "he"
        hisPreferences = menPreferences[he]
        
        # A próxima mulher que ele irá propor (de acordo com suas preferências)
        she = hisPreferences[nextManChoice[he]]
        
        # Preferências da mulher "she"
        herPreferences = womenPreferences[she]
        
        # O cônjuge atual da mulher (pode ser None)
        currentHusband = womanSpouse[she]
        
        if currentHusband is None:
            womanSpouse[she] = he
            manSpouse[he] = she
            unmarriedMen.pop(0)
        
        else:
            if herPreferences.index(he) < herPreferences.index(currentHusband):
                womanSpouse[she] = he
                manSpouse[he] = she
                unmarriedMen[0] = currentHusband
            else:
                unmarriedMen[0] = he
        
        nextManChoice[he] += 1
    
# Now "he" proposes to "she".
       # Decide whether "she" accepts, and update the following fields
       # 1. manSpouse
       # 2. womanSpouse
       # 3. unmarriedMen
       # 4. nextManChoice
          
   # Note that if you don't update the unmarriedMen list,
   # then this algorithm will run forever.
   # Thus, if you submit this default implementation,
   # you may receive "SUBMIT ERROR".
    return manSpouse
  
# You might want to test your implementation on the following two tests:
assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])
