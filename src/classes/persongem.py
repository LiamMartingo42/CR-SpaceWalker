import pygame

class Astronauta:
    def __init__(self, LARGURA_TELA, ALTURA_TELA, CORES):
        self.z = LARGURA_TELA * 2
        self.som = pygame.mixer.Sound("src/sounds/audio_musica.mp3")
        self.volume = 0.1
        self.som.set_volume(self.volume)  
        self.som.play(-1)  
        self.altura_tela = ALTURA_TELA
        self.largura_tela = LARGURA_TELA
        
    def update(self, velocidade):
        self.z -= velocidade / 2  
        self.volume = min(1.0, max(0.01, velocidade / 100))  
        self.som.set_volume(self.volume)

    def draw(self, tela: pygame.Surface, pos_x):
        if self.z > 0:
            raio = int(self.largura_tela / self.z * 100)
            if raio > 0:
                cx = int(self.largura_tela//2 - (pos_x / self.z) * self.largura_tela/2)
                pygame.draw.circle(tela, (0, 100, 200), (cx, ALTURA_TELA//2 + raio + 100), raio)

                # Desenha "continentes" verdes sobre o oceano
                # Calcula as coordenadas dos continentes em relação ao centro do círculo
                continente_offset_x = cx - raio
                continente_offset_y = (ALTURA_TELA // 2 + raio + 100) - raio
                
                continent1_points = [
                    (continente_offset_x + int((raio + 15) * 0.5), continente_offset_y + int((raio + 15) * 0.3)),
                    (continente_offset_x + int((raio + 15) * 0.7), continente_offset_y + int((raio + 15) * 0.4)),
                    (continente_offset_x + int((raio + 15) * 0.6), continente_offset_y + int((raio + 15) * 0.6)),
                    (continente_offset_x + int((raio + 15) * 0.4), continente_offset_y + int((raio + 15) * 0.5))
                ]
                pygame.draw.polygon(tela, VERDE, continent1_points)

                continent2_points = [
                    (continente_offset_x + int((raio + 25) * 0.2), continente_offset_y + int((raio + 25) * 0.7)),
                    (continente_offset_x + int((raio + 25) * 0.3), continente_offset_y + int((raio + 25) * 0.9)),
                    (continente_offset_x + int((raio + 25) * 0.5), continente_offset_y + int((raio + 25) * 0.8)),
                    (continente_offset_x + int((raio + 25) * 0.4), continente_offset_y + int((raio + 25) * 0.6))
                ]
                pygame.draw.polygon(tela, VERDE, continent2_points)

                continent3_points = [
                    (continente_offset_x + int((raio + 30) * 0.8), continente_offset_y + int((raio + 30) * 0.4)),
                    (continente_offset_x + int((raio + 30) * 0.9), continente_offset_y + int((raio + 30) * 0.6)),
                    (continente_offset_x + int((raio + 30) * 0.7), continente_offset_y + int((raio + 30) * 0.7)),
                    (continente_offset_x + int((raio + 30) * 0.6), continente_offset_y + int((raio + 30) * 0.5))
                ]
                pygame.draw.polygon(tela, VERDE, continent3_points)

                continent4_points = [
                    (continente_offset_x + int((raio + 30) * 0.95), continente_offset_y + int((raio + 30) * 0.65)),
                    (continente_offset_x + int((raio + 30) * 0.9), continente_offset_y + int((raio + 30) * 0.26)),
                    (continente_offset_x + int((raio + 30) * 0.8), continente_offset_y + int((raio + 30) * 0.2)),
                    (continente_offset_x + int((raio + 30) * 0.8), continente_offset_y + int((raio + 30) * 0.3))
                ]
                pygame.draw.polygon(tela, VERDE, continent4_points)

                continent5_points = [
                    (continente_offset_x + int((raio + 20) * 0.2), continente_offset_y + int((raio + 20) * 0.6)),
                    (continente_offset_x + int((raio + 20) * 0.3), continente_offset_y + int((raio + 20) * 0.5)),
                    (continente_offset_x + int((raio + 20) * 0.8), continente_offset_y + int((raio + 20) * 0.55)),
                    (continente_offset_x + int((raio + 20) * 0.5), continente_offset_y + int((raio + 20) * 0.95))
                ]
                pygame.draw.polygon(tela, VERDE, continent5_points)
                
                continent6_points = [
                    (continente_offset_x + int((raio + 30) * 0.5), continente_offset_y + int((raio + 30) * 0.65)),
                    (continente_offset_x + int((raio + 25) * 0.5), continente_offset_y + int((raio + 20) * 0.45)),
                    (continente_offset_x + int((raio + 30) * 0.9), continente_offset_y + int((raio + 30) * 0.98)),
                    (continente_offset_x + int((raio + 20) * 0.70), continente_offset_y + int((raio + 20) * 0.76))
                ]
                pygame.draw.polygon(tela, VERDE, continent6_points)
        fonte = pygame.font.Font(None, 36)
        texto_volume = fonte.render(f'Volume: {self.volume:.1%}', True, BRANCO)
        tela.blit(texto_volume, (self.largura_tela - 400, 100))
