from manim import *

class VectoresOrtogonal(Scene):
    def construct(self):
        # Primeros vectores: Parte 1
        vec_a_texto = MathTex(r"a = 4\hat{i} - \hat{j}", font_size=36).to_edge(UP, buff=1)
        vec_b_texto = MathTex(r"b = 2\hat{i} + 8\hat{j}", font_size=36).next_to(vec_a_texto, DOWN)
        self.play(Write(vec_a_texto), Write(vec_b_texto))

        #texto_componentes = Tex("Identificar los componentes:", font_size=30).next_to(vec_b_texto, DOWN, buff=0.5)
        componentes_a = MathTex(r"a_1 = 4,", r"a_2 = -1", font_size=30).next_to(vec_b_texto, DOWN)
        componentes_b = MathTex(r"b_1 = 2,", r"b_2 = 8", font_size=30).next_to(componentes_a, DOWN)
        self.play(Write(componentes_a), Write(componentes_b))

        # Producto punto
        texto_producto_punto = MathTex(r"a_1 \cdot b_1 + a_2 \cdot b_2 = 4 \cdot 2 + (-1) \cdot 8 = 0", font_size=30).next_to(componentes_b, DOWN)
        self.play(Write(texto_producto_punto))

        # Limpieza de textos para graficar
        self.wait(1)
        self.play(FadeOut( componentes_a, componentes_b, texto_producto_punto, vec_a_texto, vec_b_texto))

        # Plano cartesiano y vectores en la primera parte
        plano = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": GREY},
            background_line_style={"stroke_color": BLUE, "stroke_width": 1}
        )
        self.play(Create(plano))

        vector_a = Vector([2, -0.5], color=BLUE)
        vector_b = Vector([1, 4], color=GREEN)
        self.play(Create(vector_a), Create(vector_b))

        etiqueta_a = MathTex(r"\vec{a}", font_size=24).next_to(vector_a.get_end(), RIGHT, buff=0.1).set_color(BLUE)
        etiqueta_b = MathTex(r"\vec{b}", font_size=24).next_to(vector_b.get_end(), RIGHT, buff=0.1).set_color(GREEN)
        self.play(Write(etiqueta_a), Write(etiqueta_b))

        respuesta_texto = Tex("Son ortogonales", color=GREEN).to_edge(DOWN)
        self.play(Write(respuesta_texto))
        self.wait(2)

        # Parte 2: Segundo conjunto de vectores
        self.play(FadeOut(plano, vector_a, vector_b, etiqueta_a, etiqueta_b, respuesta_texto))

        # Crear el plano
        plane = NumberPlane(
            x_range=[-20, 20, .1], 
            y_range=[-20, 20, .1],
            background_line_style={"stroke_opacity": 0.4}
        )
        self.play(Create(plane))

        # Ajuste de cámara para acercar vista
        self.camera.frame_width = 10

        # Definir vectores a y b
        vector_a = np.array([0.75, -2.25, 0])
        vector_b = np.array([-0.5, 1.5, 0])

        vec_a = Arrow(ORIGIN, vector_a, color=BLUE, buff=0)
        vec_b = Arrow(ORIGIN, vector_b, color=RED, buff=0)
        self.play(GrowArrow(vec_a), GrowArrow(vec_b))

        # Etiquetas y componentes
        label_a = MathTex(r"\vec{a} = \langle 6, -18 \rangle").next_to(vec_a, DOWN)
        label_b = MathTex(r"\vec{b} = \langle -4, 12 \rangle").next_to(vec_b, UP)
        self.play(Write(label_a), Write(label_b))

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

        # Determinación de perpendicularidad
        if producto_punto == 0:
            conclusion = Text("Los vectores son perpendiculares.", color=GREEN).to_edge(DOWN)
        else:
            conclusion = Text("Los vectores no son perpendiculares.", color=RED).to_edge(DOWN)
        
        # Mostrar la conclusión final
        self.play(Write(conclusion))
        self.wait(2)
