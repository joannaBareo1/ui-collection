"""ToolTammy ManimGX demo — agent-speed math/motion plate for reels."""
import manimgx as m

class TammyManimGXDemo(m.Scene):
    def construct(self):
        # Title plate
        title = m.Text("ToolTammy × ManimGX", font_size=48, color=m.TEAL)
        sub = m.Text("animation engine for agents", font_size=28, color=m.GRAY_B)
        sub.next_to(title, m.DOWN, buff=0.3)
        badge = m.Text("90× faster math video", font_size=22, color=m.YELLOW)
        badge.next_to(sub, m.DOWN, buff=0.45)

        self.play(m.Write(title), run_time=0.8)
        self.play(m.FadeIn(sub, shift=m.UP * 0.2), run_time=0.5)
        self.play(m.FadeIn(badge), run_time=0.4)
        self.wait(0.3)

        group = m.VGroup(title, sub, badge)
        self.play(group.animate.scale(0.55).to_edge(m.UP), run_time=0.6)

        # Simple animated identity: circle + axes + moving dot (crush content vibe)
        axes = m.Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=7,
            y_length=4,
            axis_config={"color": m.GRAY_C},
        ).shift(m.DOWN * 0.3)
        curve = axes.plot(lambda x: 0.6 * m.np.sin(2 * x) + 0.3 * x, color=m.PINK)
        dot = m.Dot(color=m.TEAL, radius=0.1)
        label = m.MathTex(r"f(x)=0.6\sin(2x)+0.3x", font_size=32, color=m.WHITE)
        label.next_to(axes, m.DOWN, buff=0.25)

        self.play(m.Create(axes), run_time=0.6)
        self.play(m.Create(curve), m.Write(label), run_time=0.9)
        self.add(dot)
        self.play(m.MoveAlongPath(dot, curve), run_time=2.0, rate_func=m.linear)
        self.wait(0.25)

        tag = m.Text("drop into reels · open source", font_size=24, color=m.GRAY_A)
        tag.to_edge(m.DOWN)
        self.play(m.FadeIn(tag), run_time=0.4)
        self.wait(0.5)
