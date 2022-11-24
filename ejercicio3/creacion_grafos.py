from grafo import Maravilla, Grafo, insertar_arista, insertar_vertice

#creacion de las maravillas, que serán los vértices de cada grafo

estatuadeZeus = Maravilla("Estatua de Zeus", "Grecia", "Natural")
templodeArtemisa = Maravilla("Templo de Artemisa", "Turquia", "Natural")
mausoleo_halicarnaso = Maravilla("Mausoleo Halicarnaso", "Turquia", "Natural")
jardines_colgantes = Maravilla("Jardines colgantes", "Irak", "Natural")
coloso_rodas = Maravilla("Coloso de Rodas", "Grecia", "Natural")
faro_alejandria = Maravilla("Faro de Alejandria", "Egipto", "Natural")
piramide = Maravilla("Piramide de Guiza", "Egipto", "Natural")

ciudaddepetra = Maravilla("Ciudad de Petra", "Jordania", "Arquitectonica")
tajmahal = Maravilla("Taj Mahal", "India", "Arquitectonica")
machupicchu = Maravilla("Machu Picchu", "Peru", "Arquitectonica")
chichenitza = Maravilla("Piramide de Chichen Itza", "Mexico", "Arquitectonica")
coliseo = Maravilla("Coliseo de Roma", "Italia", "Arquitectonica")
muralla_china = Maravilla("Gran Muralla China", "China", "Arquitectonica")
cristo = Maravilla("Estatua de Cristo Redentor", "Brasil", "Arquitectonica")

#creaccion del grafo de las maravillas naturales 

grafo_naturales = Grafo(False)

insertar_vertice(grafo_naturales, estatuadeZeus)
insertar_vertice(grafo_naturales, templodeArtemisa)
insertar_vertice(grafo_naturales, mausoleo_halicarnaso)
insertar_vertice(grafo_naturales, jardines_colgantes)
insertar_vertice(grafo_naturales, coloso_rodas)
insertar_vertice(grafo_naturales, faro_alejandria)
insertar_vertice(grafo_naturales, piramide)

insertar_arista(grafo_naturales, 1000, "Estatua de Zeus", "Templo de Artemisa")
insertar_arista(grafo_naturales, 2000, "Estatua de Zeus", "Mausoleo Halicarnaso")
insertar_arista(grafo_naturales, 3000, "Estatua de Zeus", "Jardines colgantes")
insertar_arista(grafo_naturales, 4000, "Estatua de Zeus", "Coloso de Rodas")
insertar_arista(grafo_naturales, 5000, "Estatua de Zeus", "Faro de Alejandria")
insertar_arista(grafo_naturales, 6000, "Estatua de Zeus", "Piramide de Guiza")

insertar_arista(grafo_naturales, 3000, "Templo de Artemisa", "Mausoleo Halicarnaso")
insertar_arista(grafo_naturales, 3000, "Templo de Artemisa", "Jardines colgantes")
insertar_arista(grafo_naturales, 5000, "Templo de Artemisa", "Coloso de Rodas")
insertar_arista(grafo_naturales, 5000, "Templo de Artemisa", "Faro de Alejandria")
insertar_arista(grafo_naturales, 7000, "Templo de Artemisa", "Piramide de Guiza")

insertar_arista(grafo_naturales, 4000, "Mausoleo Halicarnaso", "Jardines colgantes")
insertar_arista(grafo_naturales, 1000, "Mausoleo Halicarnaso", "Coloso de Rodas")
insertar_arista(grafo_naturales, 2000, "Mausoleo Halicarnaso", "Faro de Alejandria")
insertar_arista(grafo_naturales, 3000, "Mausoleo Halicarnaso", "Piramide de Guiza")

insertar_arista(grafo_naturales, 2000, "Jardines colgantes", "Coloso de Rodas")
insertar_arista(grafo_naturales, 5000, "Jardines colgantes", "Faro de Alejandria")
insertar_arista(grafo_naturales, 2000, "Jardines colgantes", "Piramide de Guiza")

insertar_arista(grafo_naturales, 8000, "Coloso de Rodas", "Faro de Alejandria")
insertar_arista(grafo_naturales, 1000, "Coloso de Rodas", "Piramide de Guiza")

insertar_arista(grafo_naturales, 1000, "Faro de Alejandria", "Piramide de Guiza")

#creacion del grafo de las maravillas arquitectonicas

grafo_arquitectonicas = Grafo(False)

insertar_vertice(grafo_arquitectonicas, ciudaddepetra)
insertar_vertice(grafo_arquitectonicas, tajmahal)
insertar_vertice(grafo_arquitectonicas, machupicchu)
insertar_vertice(grafo_arquitectonicas, chichenitza)
insertar_vertice(grafo_arquitectonicas, coliseo)
insertar_vertice(grafo_arquitectonicas, muralla_china)
insertar_vertice(grafo_arquitectonicas, cristo)

insertar_arista(grafo_arquitectonicas, 1000, "Ciudad de Petra", "Taj Mahal")
insertar_arista(grafo_arquitectonicas, 2000, "Ciudad de Petra", "Machu Picchu")
insertar_arista(grafo_arquitectonicas, 4000, "Ciudad de Petra", "Piramide de Chichen Itza")
insertar_arista(grafo_arquitectonicas, 5000, "Ciudad de Petra", "Coliseo de Roma")
insertar_arista(grafo_arquitectonicas, 6000, "Ciudad de Petra", "Gran Muralla China")
insertar_arista(grafo_arquitectonicas, 7000, "Ciudad de Petra", "Estatua de Cristo Redentor")

insertar_arista(grafo_arquitectonicas, 5000, "Taj Mahal", "Machu Picchu")
insertar_arista(grafo_arquitectonicas, 3000, "Taj Mahal", "Piramide de Chichen Itza")
insertar_arista(grafo_arquitectonicas, 2000, "Taj Mahal", "Coliseo de Roma")
insertar_arista(grafo_arquitectonicas, 1000, "Taj Mahal", "Gran Muralla China")
insertar_arista(grafo_arquitectonicas, 2000, "Taj Mahal", "Estatua de Cristo Redentor")

insertar_arista(grafo_arquitectonicas, 4000, "Machu Picchu", "Piramide de Chichen Itza")
insertar_arista(grafo_arquitectonicas, 1000, "Machu Picchu", "Coliseo de Roma")
insertar_arista(grafo_arquitectonicas, 2000, "Machu Picchu", "Gran Muralla China")
insertar_arista(grafo_arquitectonicas, 3000, "Machu Picchu", "Estatua de Cristo Redentor")

insertar_arista(grafo_arquitectonicas, 2000, "Piramide de Chichen Itza", "Coliseo de Roma")
insertar_arista(grafo_arquitectonicas, 5000, "Piramide de Chichen Itza", "Gran Muralla China")
insertar_arista(grafo_arquitectonicas, 7000, "Piramide de Chichen Itza", "Estatua de Cristo Redentor")

insertar_arista(grafo_arquitectonicas, 7000, "Coliseo de Roma", "Gran Muralla China")
insertar_arista(grafo_arquitectonicas, 3000, "Coliseo de Roma", "Estatua de Cristo Redentor")

insertar_arista(grafo_arquitectonicas, 3000, "Gran Muralla China", "Estatua de Cristo Redentor")

#Nota las distancias son inventadas


