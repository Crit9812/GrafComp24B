from manim import *

class VectoresOrtogonalidadParalelismo(Scene):
    def construct(self):
        # Paso 1: Mostrar los vectores en formato de texto
        vec_a_texto = MathTex(r"a = 4\hat{i} - \hat{j}", font_size=36).to_edge(UP, buff=1)
        vec_b_texto = MathTex(r"b = 2\hat{i} + 8\hat{j}", font_size=36).next_to(vec_a_texto, DOWN)
        self.play(Write(vec_a_texto), Write(vec_b_texto))
        
        # Paso 2: Identificar componentes
        texto_componentes = Tex("Identificar los componentes:", font_size=30).next_to(vec_b_texto, DOWN, buff=0.5)
        componentes_a = MathTex(r"a_1 = 4,", r"a_2 = -1", font_size=30).next_to(texto_componentes, DOWN)
        componentes_b = MathTex(r"b_1 = 2,", r"b_2 = 8", font_size=30).next_to(componentes_a, DOWN)
        self.play(Write(texto_componentes), Write(componentes_a), Write(componentes_b))
        
        # Paso 3: Aplicar cálculo del producto punto
        texto_producto_punto = MathTex(r"a_1 \cdot b_1 + a_2 \cdot b_2 = 4 \cdot 2 + (-1) \cdot 8 = 0", font_size=30).next_to(componentes_b, DOWN)
        self.play(Write(texto_producto_punto))
        
        # Paso 4: Graficar el plano y los vectores
        self.wait(1)
        self.play(FadeOut(texto_componentes, componentes_a, componentes_b, texto_producto_punto, vec_a_texto, vec_b_texto))
        
        # Crear el plano cartesiano
        plano = NumberPlane(
            x_range=[-10, 10, 1],    # Rango para el eje X
            y_range=[-10, 10, 1],    # Rango para el eje Y
            x_length=10,             # Largo del eje X en pantalla
            y_length=10,             # Largo del eje Y en pantalla
            axis_config={"color": GREY},            # Color de los ejes
            background_line_style={"stroke_color": BLUE, "stroke_width": 1} # Color y grosor de la cuadrícula
        )
        
        # Añadir el plano al escenario
        self.play(Create(plano))
        
        # Crear los vectores con Vector y dibujarlos usando Create
        vector_a = Vector([2, -0.5], color=BLUE)  # Vector "a" con componentes [4, -1]
        vector_b = Vector([1, 4], color=GREEN)  # Vector "b" con componentes [2, 8]

        vector_aX = Vector([2, 0], color=GREY, stroke_width=1)  # Vector "a" con componentes [4, -1]
        vector_aY = Vector([0, -0.5], color=GREY, stroke_width=1)  # Vector "b" con componentes [2, 8]
        vector_bX = Vector([1, 0], color=GREY, stroke_width=1)  # Vector "a" con componentes [4, -1]
        vector_bY = Vector([0, 4], color=GREY, stroke_width=1) 
        
        # Dibujar los vectores en el plano usando Create en lugar de GrowArrow
        self.play(Create(vector_a), Create(vector_b))
        self.play(Create(vector_aX), Create(vector_aY))
        self.play(Create(vector_bX), Create(vector_bY))
        
        # Añadir etiquetas a los vectores
        etiqueta_a = MathTex(r"\vec{a}", font_size=24).next_to(vector_a.get_end(), RIGHT, buff=0.1).set_color(BLUE)
        etiqueta_b = MathTex(r"\vec{b}", font_size=24).next_to(vector_b.get_end(), RIGHT, buff=0.1).set_color(GREEN)
        self.play(Write(etiqueta_a), Write(etiqueta_b))
        
        
        # Paso 6: Responder la pregunta
        respuesta_texto = Tex("Los vectores son ortogonales porque su producto punto es cero.", font_size=30).to_edge(DOWN, buff=1)
        self.play(Write(respuesta_texto))
        
        self.wait(2)

