from typing import Callable, Sequence
from manim import *

config.background_color = "#282808"

# Ordem:
# 1 - _01_IntroCirculoCentral
# 2 - _02_IntroQuestao
# 3 - _03_Licao1QueCirculoEEsse
# 4 - _04_Licao1OQueEUmaFuncao
# 5 - _05_Licao1MasEOCirculo
# 6 - _06_Licao2OQueEComposicao
# 10 - Grafico

ASSINATURA_TEXTO = """
	<b><i>u/zekkious</i> @ Eu 'tô aqui</b>
	
	Estudando na <b>UFABC</b>, e usando <b>Arch :: Manjaro :: BigLinux</b>, <i>btw</i>.
"""
ASSINATURA = MarkupText(
	"".join(
		map(
			lambda l: l.strip(" \t\n"),
			ASSINATURA_TEXTO.strip(" \t\n").splitlines(True)
		)
	)
)

TITULO = MarkupText(
	"Function <u><b>re</b></u>composition",
	font_size = 36
).move_to(3.5 * UP)

class _01_IntroCirculoCentral(Scene):
	def construct(self):
		# circulo = MathTex("\circ").scale(5).move_to(ORIGIN)
		# self.play(Write(circulo))
		circulo = Circle().scale(3.5).move_to(ORIGIN).set_stroke(WHITE, opacity = 1)
		self.play(Create(circulo))
		self.wait(4)

class _02_IntroQuestao(Scene):
	def construct(self):
		questao_el = Tex(
			 "How can you,\\\\",
			r"from the function $f(x) = x + 1$,\\",
			 "arrive at any function in the form\\\\",
			r"$g(x) = a_n x^n + a_{n - 1} x^{n - 1} + \cdots + a_0 x^0 = a_k x^k$\\",
			 "?"
		).move_to(ORIGIN)
		questao_el_alt = Tex(
			r"How can you, from the function $f(x) = x + 1$, ",
			 "arrive at any function\\\\in the form ",
			r"$g(x) = a_n x^n + a_{n - 1} x^{n - 1} + \cdots + a_0 x^0 = a_k x^k$ ?",
			font_size = 36
		)
		self.play(Write(questao_el))
		self.wait(45)
		self.play(Transform(questao_el, questao_el_alt))
		self.remove(questao_el)
		self.play(questao_el_alt.animate.move_to(3 * UP))
		
		dica_el = Tex(
			 "Giving a direction to the problem,\\\\",
			 "you can use any number ",
			r"($\mathbb N, \mathbb Z, \mathbb R, \mathbb C$...).\\",
			 "Does it seem easy?"
		).move_to(ORIGIN)
		self.play(Write(dica_el))
		self.wait(15)
		
		balanco_el = Tex(
			r"To balance it, there's no operator,\\other than this circle."
		).next_to(dica_el, DOWN, buff = 0.5)
		self.play(Write(balanco_el))
		self.wait(10)

class _03_Licao1QueCirculoEEsse(Scene):
	def construct(self):
		titulo_el = Text("Lesson", font_size = 144).move_to(ORIGIN)
		self.play(Write(titulo_el))
		self.wait(2)
		self.remove(titulo_el)
		
		circulo = Circle().scale(3).move_to(ORIGIN).set_stroke(WHITE, opacity = 1)
		self.play(Create(circulo))
		self.play(circulo.animate.move_to(DOWN).scale(2/3))
		texto_el = Text("What circle is this?", font_size = 96).next_to(circulo, 2 * UP)
		self.play(Write(texto_el))
		self.wait(4)

class _04_Licao1OQueEUmaFuncao(Scene):
	def construct(self):
		titulo_el = Text(
			"What is a function?",
			font_size = 96
		)
		grupo = VGroup(titulo_el)
		
		self.play(Write(titulo_el))
		self.wait(2)
		self.play(titulo_el.animate.scale(1 / 2).move_to(UP * 3.5))
		
		texto1 = Tex(
			"For the purposes of this video,\\\\",
			"we shall assume a function is just a set of rules\\\\",
			"that map elements of one set, to another."
		)
		grupo += texto1
		self.play(Write(texto1))
		self.wait(10)
		texto2 = Tex(
			r"Just like $x\mapsto x + 1$ or $x, y\mapsto x^2 - y^2$"
		).next_to(texto1, DOWN, buff = 1)
		grupo += texto2
		self.play(Write(texto2))
		self.wait(10)

class _05_Licao1MasEOCirculo(Scene):
	def construct(self):
		titulo_el = Text(
			"Ok, but the circle...",
			font_size = 96
		)
		grupo = VGroup(titulo_el)
		
		self.play(Write(titulo_el))
		self.wait(2)
		self.play(titulo_el.animate.scale(1 / 2).move_to(UP * 3.5))
		
		texto1 = Tex(
			 "In function notation,\\\\",
			 "if we have something like ",
			r"'$f(x) = 3x - 1$',\\",
			 "we can see it as a shorthand for ",
			r"'$f\circ(x) = 3x - 1$',\\",
			r'where we tend to ommit the "$\underline\circ$"',
			 " (composition operator)."
		)
		grupo += texto1
		self.play(Write(texto1))
		self.wait(20)
		self.wait(2)

class _06_Licao2OQueEComposicao(Scene):
	def construct(self):
		titulo_el = Text(
			"Lesson",
			font_size = 144
		).move_to(ORIGIN)
		self.play(Write(titulo_el))
		self.wait(2)
		self.remove(titulo_el)
		
		circulo = Circle().scale(2).move_to(ORIGIN).set_stroke(WHITE, opacity = 1)
		self.play(Create(circulo))
		self.play(
			circulo.animate.scale(0.60).move_to(2 * DOWN)
		)
		texto1_el = Text(
			"What is function composition?",
			font_size = 80
		).next_to(circulo, 8 * UP)
		self.play(Write(texto1_el))
		self.wait(2)
		texto2_el = Tex(
			r"$f\circ g\circ h\circ j\circ k\circ l\circ m\circ n\circ o\circ p\circ o\circ q\circ r$"
		).move_to(
			point_or_mobject = ORIGIN,
			aligned_edge = LEFT
		)
		self.play(Write(texto2_el), run_time = 4)
		
		titulo2_el = Text(
			"Function composition",
			font_size = 36
		).move_to(3.5 * UP)
		self.play(Transform(texto1_el, titulo2_el))

class _07_Licao2ExplicacaoComposicao(Scene):
	def construct(self):
		titulo_el = MarkupText(
			"<u>Function composition</u>",
			font_size = 36
		).move_to(3.5 * UP)
		self.add(titulo_el)
		
		texto1_el = Tex(
			"Function composition is not an operation in the values,\\\\",
			"but an operation in the rules themselves.",
			font_size = 48
		).move_to(ORIGIN)
		self.play(Write(texto1_el), run_time = 5)
		self.wait(5)
		self.play(texto1_el.animate.scale(3/4).move_to(UP * 2))
		
		texto2_el = Tex(
			 "For example: ",
			r"$(x\mapsto x^2)\circ(x\mapsto\sqrt x)$",
			r" gives us $x\mapsto x$ ",
			r"(for $x\in\mathbb R_+$).",
			font_size = 36
		)
		self.play(Write(texto2_el))
		self.wait(16)
		
		texto3_el = Tex(
			 "As well, ",
			r"$(x\mapsto\sqrt x)\circ(x\mapsto x^2)$",
			r" gives us $x\mapsto x$ ",
			r"(for $x\in\mathbb C$)",
			font_size = 36
		).next_to(texto2_el, DOWN * 2)
		self.play(Write(texto3_el))
		self.wait(15)
		self.remove(texto2_el, texto3_el)
		self.wait(1)
		
		texto4_el = Tex(
			 "Another one:\\\\",
			r"$f\circ x = ax + b, g\circ x = cx + d$:\\",
			r"$f\circ g\circ x = a(cx + d) + b = (ac) x + (ad + b)$\\",
			r"$g\circ f\circ x = c(ax + b) + d = (ca) x + (cb + d)$"
		)
		self.play(Write(texto4_el))
		self.wait(30)
		self.remove(texto1_el, texto4_el)
		
		texto5_el = Text(
			"What does these cases show?",
			font_size = 48
		).move_to(3 * UP)
		self.play(Write(texto5_el))
		self.wait(3)
		
		fonte : dict = { "font_size": 28 }
		
		grupo = (
			VGroup()
			+ Text("In general:", **fonte)
			+ Text("1. The composition operation is not commutative", **fonte)
			+ Text("2. If", **fonte)
			+ Tex(r"$f\circ x\equiv a_i x^i\in\mathcal P_n\circ x$", **fonte)
			+ Text("_. And", **fonte)
			+ Tex(r"$g\circ x\equiv a_j x^j\in\mathcal P_m\circ x$", **fonte)
			+ Text("_. Then", **fonte)
			+ Tex(r"$f\circ g, g\circ f\in\mathcal P_{n \times m}\circ x$", **fonte)
		).arrange(
			DOWN,
			center = False,
			aligned_edge = LEFT
		).move_to(ORIGIN)
		
		texto_anterior : SVGMobject = None
		for texto in grupo:
			if isinstance(texto, Tex):
				texto.next_to(
					texto_anterior,
					DOWN + 5 * RIGHT,
					aligned_edge = LEFT
				)
			texto_anterior = texto
		
		self.play(Write(grupo), run_time = 4)
		# .move_to(
		# 	point_or_mobject = 5 * LEFT + 2 * UP
		# )
		# for texto in grupo:
		# 	if texto_anterior is not None:
		# 		texto.next_to(
		# 			texto_anterior,
		# 			DOWN
		# 		)
		# 	self.play(Write(texto), run_time = 0.5)
		# 	texto_anterior = texto
		
		self.wait(30)

class _08_Licao3OQueERecomposicao(Scene):
	def construct(self):
		titulo_el = Text(
			"Lesson",
			font_size = 144
		).move_to(ORIGIN)
		self.play(Write(titulo_el))
		self.wait(2)
		self.remove(titulo_el)
		
		circulo = (
			Circle().scale(2).move_to(ORIGIN)
		).set_stroke(
			WHITE,
			opacity = 1
		)
		self.play(Create(circulo))
		self.play(
			circulo.animate.scale(0.60).move_to(2 * DOWN)
		)
		
		texto1_el = MarkupText(
			"What is function <u><b>re</b></u>composition?",
			font_size = 72
		).next_to(circulo, 8 * UP)
		self.play(Write(texto1_el))
		self.wait(2)
		
		texto_anterior: Tex = None; texto_proximo: Tex
		
		contagem: int = 10
		duration: float = 5.0
		for i in range(contagem + 1):
			texto_proximo = Tex(
				r"$f\overset{" + (
					"" if i == 0 else str(i)
				) + r"}\circ " + (
					r"f\circ " * (contagem - i)
				) + "$"
			).move_to(
				point_or_mobject = ORIGIN,
				aligned_edge = LEFT
			)
			
			if texto_anterior is None:
				self.play(Write(texto_proximo), run_time = 4)
			else:
				self.play(
					Transform(texto_anterior, texto_proximo),
					run_time = duration / contagem
				)
				self.remove(texto_anterior)
			
			texto_anterior = texto_proximo
		
		self.play(Transform(texto1_el, TITULO))
		self.wait(1)

class _09_Licao3ExplicacaoRecomposicao(Scene):
	def construct(self):
		self.add(TITULO)
		
		texto1 = MarkupText(
			"As multiplication is the recursive or iterative version of addition,\n"
			+ " and addition is the recursive of finding the successor (adding 1),\n"
			+ " <i>recomposition</i> is, multiple times, composing a function with itself.",
			font_size = 24
		).move_to(UP).scale(.75)
		self.play(Write(texto1), run_time = 3)
		self.wait(16)
		
		texto2 = Tex(
			 "With the start at $1$, ",
			r"we have $f\circ x = f\overset 1\circ x$",
			font_size = 40
		).next_to(texto1, DOWN, buff = 1)
		self.play(Write(texto2))
		self.wait(10)
		
		self.remove(texto1)
		self.play(texto2.animate.move_to(2 * UP))
		
		texto3 = Tex(
			r"Examples:\\[\baselineskip]",
			r"If $f\circ x\equiv \mathrm{succ}\circ x = x + 1$,\\",
			r"Then $f\overset 2\circ x = (x\mapsto x + 1)\circ f\circ x = (x + 1) + 1 = x + 2$\\[\baselineskip]",
			r"If $g\circ x\equiv kx$,\\",
			r"Then $g\overset 2\circ x = (x\mapsto kx)\circ g\circ x = k(kx) = k^2 x$",
			font_size = 40,
			# tex_environment = "align",
			arg_separator = "~\\\n"
		).next_to(texto2, DOWN, buff = 1)
		self.play(Write(texto3), run_time = 5)
		self.wait(15)

class _10_Licao3PropriedadesDaRecomposicao(Scene):
	def construct(self):
		self.add(TITULO)
		
		titulo = Tex(
			r"Let's see what we get with $f\circ x = x + 1$:"
		).next_to(TITULO, DOWN, buff = 0.5)
		self.play(Write(titulo), run_time = 2)
		
		# Sem narração
		texto1 = Tex(
			 "$$",
			r"\begin{aligned}",
			r"f\overset{1}{\circ} x &= x + 1\\",
			r"f\overset{2}{\circ} x &= x + 2\\",
			r"f\overset{\vdots}{\circ} x &= x + \vdots\\",
			r"f\overset{n}{\circ} x &= x + n",
			r"\end{aligned}",
			 "$$",
			arg_separator = "\n"
		)
		self.play(Write(texto1), run_time = 5)
		self.wait(10)
		
		# Sem narração
		texto2 = Tex(
			 "$$" + \
			r"f\overset n\circ f\overset m\circ x" + \
			r"&= f\overset n\circ(x\mapsto x + m)\\" + \
			r"&= (x + m) + n\\" + \
			r"&= x + (m + n)\\" + \
			r"&= f\overset{m + n}\circ x\\" + \
			 "$$",
			tex_environment = "align"
		)
		self.play(
			Transform(texto1, texto2),
			run_time = 2
		)
		self.wait(10)
		self.remove(texto2)
		
		texto2 = Tex(
			 "If $n = +1$, we have $f$\\\\",
			 "If $n > +1$, we have $f$ applied to itself various times\\\\",
			r"If $n = \;0$, we have the identity function, ",
			r"$f\overset 0\circ x = x + 0 = \mathrm{id} x$\\",
			 "If $n = -1$, we have the reverse function\\",
			r"$f\overset{- 1}\circ x = x + (- 1) = x - 1$\\\\",
			 "- Composing with $f$: ",
			r"$f\circ\left(f\overset{-1}\circ x\right) = (x - 1) + 1 = x$",
			 "- - Corolary: ",
			r"$f\overset n\circ f\overset{- n}\circ = f\overset{n - n}\circ = f\overset 0\circ = \mathrm{id}$",
			tex_environment = "align"
		)
		self.play(Write(texto2), run_time = 5)
		self.wait(30)

class _11_Licao3CasoNotavelDaRecomposicao(Scene):
	def construct(self):
		self.add(TITULO)
		
		titulo = Tex(
			 "Notable case"
		).next_to(TITULO, DOWN, buff = 0.5)
		self.play(Write(titulo), run_time = 2)
		
		texto1 = Tex(
			r"""
			\mathrm{sen}\circ\mathrm{arcsen}
			&= \left(
				\mathrm{sen}\overset{+1}\circ
			\right)\circ\left(
				\mathrm{sen}\overset{-1}\circ
			\right)\\
			&= \mathrm{sen}\overset 0\circ = \mathrm{id}\\
			&= \left(
				\mathrm{sen}\overset{-1}\circ
			\right)\circ\left(
				\mathrm{sen}\overset{+1}\circ
			\right)\\
			&= \mathrm{arcsen}\circ\mathrm{sen}
			""",
			tex_environment = "align"
		)
		self.play(
			Write(texto1),
			run_time = 2
		)
		self.wait(10)
		
		texto2 = Tex(
			r"""
			\mathrm{*}\circ\mathrm{arc*}
			&= \left(
				\mathrm{*}\overset{+1}\circ
			\right)\circ\left(
				\mathrm{*}\overset{-1}\circ
			\right)\\
			&= \mathrm{*}\overset 0\circ = \mathrm{id}\\
			&= \left(
				\mathrm{*}\overset{-1}\circ
			\right)\circ\left(
				\mathrm{*}\overset{+1}\circ
			\right)\\
			&= \mathrm{arc*}\circ\mathrm{*}
			""",
			tex_environment = "align"
		)
		self.play(
			Transform(texto1, texto2),
			run_time = 5
		)
		self.wait(15)
		# Notable case
		# What I particularly like about this case,
		# is that it shows us
		# another way of representing the `arc` functions;
		# another way of showing the same already known thing,
		# but putting into evidence another logic

class _12_ExtensaoAlemDaNecessidade(Scene):
	def construct(self):
		titulo2_el = MarkupText(
			"Extension beyond necessity",
			font_size = 36
		).move_to(3.5 * UP)
		self.play(Write(titulo2_el))
		
		texto1 = Tex(
			 "If ",
			r"$f\overset n\circ = f\circ f\circ f\cdots$,",
			 " then:\\\\\\\\",
			r"$f\overset{\underline{2}}{\circ\circ}$",
			r"$\leftarrow f{2\over\circ^2}$",
			r"$= f\overset{f}\circ$"
		).move_to(2 * UP)
		self.play(Write(texto1))
		self.wait(0)
		
		texto2 = Tex(
			r"For $f\circ x = x + 1$, we have:\\",
			r"$f\overset 2{\overline{\circ\circ}} x$",
			r"$= f\overset{f\circ x}\circ x$",
			r"$= f\overset{x + 1}\circ x$",
			r"$= x + (x + 1) = 2x + 1$\\",
			r"$f\overset 3{\overline{\circ\circ}} x$",
			r"$= f\overset{f\overset{f\circ x}\circ x}\circ x$",
			r"$= f\overset{f\overset{x + 1}\circ x}\circ x$",
			r"$= f\overset{2x + 1}\circ x$",
			r"$= x + (2x + 1) = 3x + 1$\\",
			r"$\vdots$",
			r"$f\overset n{\overline{\circ\circ}} x$",
			r"$= f\overset{f\overset\vdots\circ x}\circ x = nx + 1$",
			r"$\vdots$"
		)
		self.play(Write(texto2), run_time = 5)
		self.wait(0)
		
		texto3 = Tex(
			r"$f\overset 2{\overline{\circ\circ\circ}} x$",
			r"$= f\overset{2}{\overline{\circ^3}} x$",
			r"$= f\overset{\underline{f\circ x}}{\circ^2} x$",
			r"$= (f\circ x) x + 1 = (x + 1)x + 1 = x^2 + x + 1$"
		).next_to(
			texto2,
			DOWN,
			buff = 0
		)
		self.play(Write(texto3))
		self.wait(0)
		
		texto4 = Tex(
			r"$\therefore f\overset m{\overline{\circ^n}} x\in\mathcal P_n\circ x$,",
			r" where $\mathcal P_n\circ x$ is the set of all polynomials, on $x$, with degree up to $n$."
		)
		self.remove(texto2)
		self.play(texto3.animate.move_to(2 * UP))
		self.play(Write(texto4))

class _13_Agradecimentos(Scene):
	def construct(self):
		self.add(
			ASSINATURA.move_to(2 * DOWN, RIGHT)
		)
		
		texto1 = MarkupText(
			"<i>Cool!</i>\n" + \
			"With a polynomial of degree 1, we can construct polynomials of any (natural) degree!\n" + \
			"But can we construct <u>every</u> polynomial? <i>Well...</i>\n" + \
			"Can we construct every <s>analytic</s> function? <i>With Taylor series, and then de Pade series and...</i>\n" + \
			"\nWhat about the main question on the video?\n..."
		).move_to(3 * UP)
		self.play(
			Write(texto1),
			run_time = 10
		)
		self.wait(0 + 5)
		
		texto2 = MarkupText(
			"<i>I <u>don't</u> have an answer for that.</i>\n\n" + \
			"Yet."
		).next_to(
			texto1,
			DOWN
		)
		self.play(
			Write(texto2)
		)
		self.wait(5)
		
		texto3 = Tex(
			r"By the next episode, we might be seeing one of those:\\",
			r"$$\left[1 + {1\over x}\right]\overset n\circ$$\\",
			r"(Some) Especial cases of $f\overset n\circ$, where $n\notin\Z$\\",
			r"Something being calculated like it's important\\",
			 "Reinko Venema's n-D complex structures (aka. 3D Complex Numbers.net)\\\\",
			 "This, but in Portuguese"
		)
		self.play(Write(texto3))
		self.wait(0)

class Grafico(Scene):
	def construct(self):
		x_min = -2; x_max = 2
		x_extends = 2
		
		plano = NumberPlane(
			x_range = [x_min, x_max, 0.5], x_length = 10,
			y_range = [-2, 2, 0.5], y_length = 6
		).add_coordinates()
		legenda = plano.get_axis_labels(
			x_label = "x", y_label = "f\circ x"
		)
		
		k = ValueTracker(x_min - x_extends)
		
		func = plano.plot(
			function = lambda x: 1 + 1 / x,
			discontinuities = [0],
			x_range = [ x_min - x_extends, x_max + x_extends ],
			dt = 1e-2,
			color = ORANGE
		)
		legenda_func = MathTex(
			"f\circ x = 1 + {1\over{x}}"
		).scale(0.4).next_to(func, RIGHT, buff = -1.5)
		
		slope = always_redraw(
			lambda: plano.get_secant_slope_group(
				x = k.get_value(), graph = func,
				dx = 1e-3, secant_line_color = GREEN, secant_line_length = 6
			)
		)
		
		ponto = always_redraw(
			lambda: Dot().move_to(
				plano.c2p(k.get_value(), func.underlying_function(k.get_value()))
			)
		)
		
		self.play(DrawBorderThenFill(plano))
		self.play(Write(func))
		self.add(legenda, legenda_func)
		self.wait()
		self.add(slope, ponto)
		self.wait()
		self.play(k.animate.set_value(x_max + x_extends), run_time = 4)

