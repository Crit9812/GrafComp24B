from manim import *

class Vectores(Scene):
    def construct(self):
        # Crear el plano
        plane = NumberPlane(x_range=[-20, 20, .1], y_range=[-20, 20, .1], background_line_style={"stroke_opacity": 0.4})
        self.play(Create(plane))

        # Escalar la vista de la cámara ajustando el ancho del frame
        self.camera.frame_width = 2  # Ajusta este valor para acercar o alejar la escena

        # Definir los vectores a y b
        vector_a = np.array([.75, -2.25, 0])
        vector_b = np.array([-.5, 1.5, 0])
        
        # Crear los vectores en el gráfico
        vec_a = Arrow(ORIGIN, vector_a, color=BLUE, buff=0)
        vec_b = Arrow(ORIGIN, vector_b, color=RED, buff=0)
        
        # Añadir los vectores a la escena
        self.play(GrowArrow(vec_a), GrowArrow(vec_b))
        
        # Etiquetas de los vectores
        label_a = MathTex(r"\vec{a} = \langle 6, -18 \rangle").next_to(vec_a, DOWN)
        label_b = MathTex(r"\vec{b} = \langle -4, 12 \rangle").next_to(vec_b, UP)
        self.play(Write(label_a), Write(label_b))
        
        # Identificar componentes de a y b
        a1_text = MathTex(r"a_1 = 6").next_to(label_a, DOWN)
        a2_text = MathTex(r"a_2 = -18").next_to(a1_text, DOWN)
        b1_text = MathTex(r"b_1 = -4").next_to(label_b, UP)
        b2_text = MathTex(r"b_2 = 12").next_to(b1_text, UP)
        
        self.play(Write(a1_text), Write(a2_text), Write(b1_text), Write(b2_text))

        # Cálculo del producto punto
        producto_punto = 6 * (-4) + (-18) * 12
        result_text = MathTex(r"\vec{a} \cdot \vec{b} = 6 \times -4 + (-18) \times 12 = " + str(producto_punto))
        result_text.next_to(a2_text, DOWN)
        self.play(Write(result_text))
        
        # Determinar si los vectores son perpendiculares
        if producto_punto == 0:
            conclusion = Text("Los vectores son perpendiculares.", color=GREEN).to_edge(DOWN)
        else:
            conclusion = Text("Los vectores no son perpendiculares.", color=RED).to_edge(DOWN)
        
        # Mostrar la conclusión
        self.play(Write(conclusion))
        self.wait(2)
