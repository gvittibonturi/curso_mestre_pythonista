def make_album(artist_name, album_title, faixa=''):
	"""Devolve informações do artista e album misical"""
	musician_album = {'name': artist_name, 'album': album_title}
	if faixa:
		musician_album['faixa'] = faixa
	return(musician_album)
	
	
active = True	
while active:
	print("\nPlease teel the artist name:")
	print("(enter 'q' at any time to stop)")
	
	ar_name = input("Artist name: ")
	if ar_name == 'q':
		active = False
		break
	else:
		 ar_name_true = ar_name
		
	al_name = input("Album name: ")
	if al_name == 'q':
		active = False
		break
	else:
		 al_name_true = al_name
	
		
musician = make_album(ar_name_true, al_name_true)
print(musician.values())

# musician = make_album('Paul Macartnay', 'The Beathes')
# print(musician.values())

# musician = make_album('David Gilmore', 'Pigs', faixa='Another Pig')
# print(musician.values())


