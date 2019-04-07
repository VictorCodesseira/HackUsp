import numpy as np
import pandas as pd
import pycep_correios
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

########################################################

def dist_ll(p1, p2):
	''' Calcula a distancia entre dois pontos '''
	return geodesic((p1[0],p1[1]),(p2[0],p2[1])).km 

def transform_CEP(cep):
	'''
	Pega o CEP informado e transforma em Latitude e Longitude. CUIDADO: ALGUNS CEP'S NÃO FUNCIONAM
	'''
	cep = str(cep)
	endereco = pycep_correios.consultar_cep(cep)
	geolocator = Nominatim(user_agent="Juberweb")
	loc = geolocator.geocode(endereco['end'] + ', ' + endereco['cidade'])
	return loc.latitude, loc.longitude

def vq(df_points, df_center):
	'''
	Aqui tenta realizar a função vq so scipy
	'''
	centers = np.zeros(df_points.shape[0], dtype='int')
	dist = np.zeros(df_points.shape[0])
	for i in range(df_points.shape[0]):
		index_ = df_points.index.values[i]
		dist_df = df_center.apply(dist_ll, axis=1, args=(df_points.loc[index_],)).values
		centers[i] = np.argmin(dist_df)
		dist[i] = dist_df.min()
	return centers, dist

def redefine_pas_mot(df_pas, df_mot, count_max = 4, dist_max = 2):
	'''
	Aqui excluimos as pessoas que querem carona que estão muito longe, é decidido as caronas com pessoas com mais de 4 caronas.
	Obs: pas = passageiro / mot = motorista
	'''
	centers, dist = vq(df_pas, df_mot)
	unique, counts = np.unique(centers, return_counts=True)

	index = df_pas[dist>dist_max].index.values

	df_pas = df_pas.drop(index)

	centers, dist = vq(df_pas, df_mot)

	unique, counts = np.unique(centers, return_counts=True)
	print(counts)

	index = np.array([])

	ride = {}

	for center in unique[counts>count_max]:
		print(df_pas[centers==center].index.values[dist[centers==center].argsort()[:4]])
		ride[center] = df_pas[centers==center].index.values[dist[centers==center].argsort()[:4]]
		index = np.concatenate([index,df_pas[centers==center].index.values[dist[centers==center].argsort()[:4]]])

	if index.size == 0:
		return df_pas, df_mot, ride

	return df_pas.drop(index), df_mot.drop(df_mot.index.values[unique[counts>count_max]]), ride

def form_last_ride(df_pas, df_mot):
	'''
	Aqui calcula as viagens que possuem menos de 4 pessoas
	'''
	centers, dist = vq(df_pas, df_mot)
	unique, counts = np.unique(centers, return_counts=True)

	ride = {}
	index = np.array([])

	for center in unique:
		ride[center] = df_pas[centers==center].index.values[dist[centers==center].argsort()[:4]]
		index = np.concatenate([index,df_pas[centers==center].index.values[dist[centers==center].argsort()[:4]]])

	return df_pas.drop(index), df_mot.drop(df_mot.index.values[unique[counts>count_max]]), ride

#########################################################

pessoas = pd.read_csv("dados_pessoas.csv") # Lê dados

df_pessoas = pd.DataFrame(pessoas['CEP'].apply(transform_CEP).tolist()) # Transforma o CEP em latitude e longitude
df_pessoas.columns = ['latitude', 'longitude']
df = pd.concat([df_pessoas, pessoas['Motorista']], axis=1)

df_mot = df[df['Motorista'] == 1][['latitude','longitude']].reset_index(drop=True) # Separa as classes
df_pas = df[df['Motorista'] == 0][['latitude','longitude']].reset_index(drop=True)

count_max = 4

rides = {}

while True:
	df_pas, df_mot, ride = redefine_pas_mot(df_pas, df_mot) # Vai tentando arrumar as caronas com mais que 4 pessoas
	if not bool(ride):
		break
	rides.update(ride) # update nas caronas e seus respectivos motoristas/passageiros

df_pas, df_mot, ride = form_last_ride(df_pas, df_mot) # Arruma as caronas com até 4 pessoas
rides.update(ride)

print(rides) # Aqui são as caronas resultantes da semana
print(df_pas) # Aqui são as pessoas que não conseguiram carona