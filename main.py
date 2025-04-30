vie = 7
mot_cacher = 'neuille'
mot_reveler = "_" * len(mot_cacher)
while mot_reveler != mot_cacher and vie > 0 : 
  lettre = input("Donne t'as lettre : ")
  
  if len(lettre) > 1 :
    print("donne que une seule lettre  ! ")
  
  if lettre in mot_cacher: 
      for i in range(len(mot_cacher)):
        if mot_cacher[i] == lettre:
          mot_reveler = mot_reveler[:i] + lettre + mot_reveler[i + 1:]
  else:
    vie = vie - 1 
    
  if mot_reveler == mot_cacher:
    print("Bravo tu a trouver le mot : ", mot_cacher)
  elif vie == 0:
    print("tu as perdu !  :(")
  else:
    print("votre mot est", mot_reveler)
    print("nombre de vie : ", vie)
  
    
  