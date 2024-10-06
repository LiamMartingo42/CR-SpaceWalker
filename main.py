import time
import pygame
import random
import math
import cv2


# Constantes
## Configuração de Tela
LARGURA_TELA = 1000
ALTURA_TELA = 700
## Configuração de Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (34, 139, 34)  

# Inicializando o jogo
pygame.init()
pygame.mixer.init() 


class Estrela:
    def __init__(self):
        self.x = random.uniform(-LARGURA_TELA/2, LARGURA_TELA/2)
        self.y = random.uniform(-ALTURA_TELA/2, ALTURA_TELA/2)
        self.z = random.uniform(0, LARGURA_TELA)
        self.color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))

    def update(self, velocidade):
        self.z -= velocidade
        if self.z <= 0:
            self.z = LARGURA_TELA
            self.x = random.uniform(-LARGURA_TELA/2, LARGURA_TELA/2)
            self.y = random.uniform(-ALTURA_TELA/2, ALTURA_TELA/2)
            self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(2, 255))

    def draw(self, tela, pos_x):
        if self.z != 0:
            sx = int(((self.x - pos_x) / self.z) * LARGURA_TELA/2 + LARGURA_TELA/2)
            sy = int((self.y / self.z) * ALTURA_TELA/2 + ALTURA_TELA/2)
            raio = max(1, int((LARGURA_TELA - self.z) / 100))
            # Desenha apenas se estiver na tela
            if 0 <= sx <= LARGURA_TELA and 0 <= sy <= ALTURA_TELA:
                pygame.draw.circle(tela, self.color, (sx, sy), raio)

class Astronauta:
    def __init__(self):
        self.z = LARGURA_TELA * 2
        self.som = pygame.mixer.Sound("src/sounds/audio_musica.mp3")
        self.volume = 0.1
        self.som.set_volume(self.volume)  
        self.som.play(-1)  
        
    def update(self, velocidade):
        self.z -= velocidade / 2  
        self.volume = min(1.0, max(0.01, velocidade / 100))  
        self.som.set_volume(self.volume)

    def draw(self, tela: pygame.Surface, pos_x):
        if self.z > 0:
            raio = int(LARGURA_TELA / self.z * 100)
            if raio > 0:
                cx = int(LARGURA_TELA//2 - (pos_x / self.z) * LARGURA_TELA/2)
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
        tela.blit(texto_volume, (LARGURA_TELA - 400, 100))

class ObjetoIdentificado:
    
    def __init__(self):
        self.x = (LARGURA_TELA - 150)
        self.y = random.randint(70, ALTURA_TELA - 100)
        self.raio = 25
        self.cor = VERMELHO
        self.visivel = False
        self.tempo_ultimo_spawn = time.time()
        self.alpha = 255 
    
    def update(self):
        if time.time() - self.tempo_ultimo_spawn > 10:
            self.visivel = True
            self.tempo_ultimo_spawn = time.time()
            self.x = random.randint(70, LARGURA_TELA - 150)
            self.y = random.randint(70, ALTURA_TELA - 100)
            self.cor = random.choice([VERMELHO, AZUL])
            self.alpha = 50 
    
    def draw(self, tela):
        if self.visivel:
            if self.alpha < 255:
                self.alpha += 5
            cor_atual = (self.cor[0], self.cor[1], self.cor[2], self.alpha)
            surface = pygame.Surface((self.raio * 2, self.raio * 2), pygame.SRCALPHA)
            pygame.draw.circle(surface, cor_atual, (self.raio, self.raio), self.raio)
            tela.blit(surface, (self.x - self.raio, self.y - self.raio))
    
    def click(self, pos_mouse, astronauta):
        if self.visivel:
            distancia = math.sqrt((pos_mouse[0] - self.x) ** 2 + (pos_mouse[1] - self.y) ** 2)
            if distancia <= self.raio:
                self.visivel = False
                astronauta.som.stop()
                return True
        return False

class VisualizarObjeto:
    def __init__(self):
        self.imagem = pygame.image.load('src/images/Estrela-.png') 
        self.imagem = pygame.transform.scale(self.imagem, (300, 300))  
        # self.video = cv2.VideoCapture('video_exemplo.mp4') 
        self.mostrar_video = False
        self.texto = "Estrela L1527       O Telescópio Espacial James Webb capturou imagens detalhadas da formação dessa estrela jovem conhecida como L1527, localizada na região de formação estelar de Touro. Esta protoestrela está envolvida por um disco de gás e poeira, material que eventualmente pode dar origem a planetas. As imagens revelam fluxos de gás em forma de ampulheta, esculpidos pela estrela em crescimento, proporcionando insights sem precedentes sobre os primeiros estágios da vida estelar."
        self.input_ativo = False
        self.input_texto = ""
        self.fonte = pygame.font.Font(None, 24)
    
    def update(self):
        # Alterna entre mostrar imagem ou vídeo
        self.mostrar_video = not self.mostrar_video

    def handle_eventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if 400 <= evento.pos[0] <= 700 and 300 <= evento.pos[1] <= 350:
                self.input_ativo = True
            else:
                self.input_ativo = False
        elif evento.type == pygame.KEYDOWN:
            if self.input_ativo:
                if evento.key == pygame.K_RETURN:
                    print(f"Texto digitado: {self.input_texto}")
                    self.input_texto = ""
                elif evento.key == pygame.K_BACKSPACE:
                    self.input_texto = self.input_texto[:-1]
                else:
                    self.input_texto += evento.unicode

    def draw(self, tela):
            if self.mostrar_video:
                ret, frame = self.video.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.transpose(frame)
                    frame_surface = pygame.surfarray.make_surface(frame)
                    frame_surface = pygame.transform.scale(frame_surface, (300, 300))
                    tela.blit(frame_surface, (50, 200))
            else:
                tela.blit(self.imagem, (50, 200))

            # Desenha o texto com quebra de linhas
            texto_renderizado = self.texto.split(" ")
            linhas = []
            linha_atual = ""
            for palavra in texto_renderizado:
                if self.fonte.size(linha_atual + palavra)[0] < 400:
                    linha_atual += palavra + " "
                else:
                    linhas.append(linha_atual)
                    linha_atual = palavra + " "
            linhas.append(linha_atual)
            y_offset = 250
            for linha in linhas:
                texto_surface = self.fonte.render(linha, True, BRANCO)
                tela.blit(texto_surface, (400, y_offset))
                y_offset += 30

def screen1():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("SpaceWalker")
    cabine_image = pygame.image.load('src/images/imagem_janela.png').convert_alpha()
    cabine_image = pygame.transform.scale(cabine_image, (LARGURA_TELA, ALTURA_TELA))
    
    estrelas = [Estrela() for _ in range(500)]
    astronauta = Astronauta()
    objeto_identificado = ObjetoIdentificado()

    pos_x = 0
    movement_x = 0
    velocidade_horizontal = 10 

    # Loop principal da tela 1
    executando = True
    clock = pygame.time.Clock()
    velocidade = 5

    while executando:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    executando = False
                elif evento.key == pygame.K_UP:
                    velocidade += 1
                elif evento.key == pygame.K_DOWN:
                    velocidade = max(1, velocidade - 1)
                elif evento.key == pygame.K_LEFT:
                    movement_x = -1
                elif evento.key == pygame.K_RIGHT:
                    movement_x = 1
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and movement_x == -1:
                    movement_x = 0
                elif evento.key == pygame.K_RIGHT and movement_x == 1:
                    movement_x = 0
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  
                    if objeto_identificado.click(evento.pos,astronauta):
                        print("Objeto identificado clicado!")
                        screen2()
                        return

        # Atualização da posição horizontal (independente da velocidade)
        pos_x += movement_x * velocidade_horizontal


        for estrela in estrelas:
            estrela.update(velocidade)
        astronauta.update(velocidade)
        objeto_identificado.update()

        tela.fill(PRETO)
        for estrela in estrelas:
            estrela.draw(tela, pos_x)
        astronauta.draw(tela, pos_x)
        objeto_identificado.draw(tela)

        tela.blit(cabine_image, (0, 0)) 
        
        pygame.display.flip()

def screen2():
    nova_tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    nova_tela.fill(PRETO) 

    visual_objeto = VisualizarObjeto()
    clock = pygame.time.Clock()
    
    executando = True
    while executando:
        clock.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    executando = False
            visual_objeto.handle_eventos(evento)

        visual_objeto.draw(nova_tela)
        pygame.display.flip()

screen1()
pygame.quit()