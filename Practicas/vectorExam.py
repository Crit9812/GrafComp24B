from manim import *

class VectorAnalysis(ThreeDScene):  # Cambiamos de Scene a ThreeDScene
    def construct(self):
        # Definición de θ (puedes cambiar este valor)
        theta = PI / 4  # 45 grados como ejemplo

        # Definición de los vectores
        u = np.array([np.cos(theta), np.sin(theta), -1])
        v = np.array([np.sin(theta), -np.cos(theta), 0])

        # Mostrar coordenadas de los vectores
        u_text = MathTex(r"\vec{u} = \langle \cos\theta, \sin\theta, -1 \rangle").to_edge(UP)
        v_text = MathTex(r"\vec{v} = \langle \sin\theta, -\cos\theta, 0 \rangle").next_to(u_text, DOWN)
        
        self.play(Write(u_text), Write(v_text))
        self.wait(2)

        # Grafico 3D
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes)

        # Representacin de los vectores
        vector_u = Arrow3D(start=ORIGIN, end=u, color=BLUE)
        vector_v = Arrow3D(start=ORIGIN, end=v, color=RED)

        self.play(Create(vector_u), Create(vector_v))
        self.wait(2)

        # Identificar si son ortogonales o paralelos
        dot_product = np.dot(u, v)
        cross_product = np.cross(u, v)

        if np.isclose(dot_product, 0):
            conclusion = MathTex(r"\vec{u} \text{ y } \vec{v} \text{ son ortogonales.}").to_edge(DOWN)
        elif np.isclose(cross_product, np.zeros(3)).all():
            conclusion = MathTex(r"\vec{u} \text{ y } \vec{v} \text{ son paralelos.}").to_edge(DOWN)
        else:
            conclusion = MathTex(r"\vec{u} \text{ y } \vec{v} \text{ no son ortogonales ni paralelos.}").to_edge(DOWN)

        self.play(Write(conclusion))
        self.wait(2)
