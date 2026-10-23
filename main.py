from manim import *

# Vertical 9:16 for Shorts / Reels / TikTok
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30

BG = "#0B0F1A"
GOLD = "#FFD166"
CYAN = "#4CC9F0"
RED = "#FF5A5F"

# Uses Text only (no LaTeX needed). Keep everything inside y = -5.5 .. +5.5
# so Shorts/Reels buttons and captions never cover it.


class PointNineRepeating(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ---------- 1. HOOK (0-5s) ----------
        claim = Text("0.999...  =  1", font_size=84, weight=BOLD)
        claim.move_to(UP * 1.5)
        sub = Text("Most people say NO.", font_size=44, color=RED)
        sub.next_to(claim, DOWN, buff=0.8)

        self.play(Write(claim), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.6)
        self.play(claim.animate.set_color(GOLD), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(claim), FadeOut(sub), run_time=0.5)

        # ---------- 2. PROOF 1: thirds (5-15s) ----------
        tag1 = Text("PROOF 1", font_size=40, color=CYAN, weight=BOLD)
        tag1.move_to(UP * 5)

        l1 = Text("1/3  =  0.333...", font_size=62)
        l2 = Text("x 3", font_size=54, color=GOLD)
        l3 = Text("3/3  =  0.999...", font_size=62)
        l4 = Text("3/3  =  1", font_size=62, color=GOLD)

        stack = VGroup(l1, l2, l3).arrange(DOWN, buff=0.7).move_to(UP * 1.2)
        l4.move_to(l3)

        self.play(FadeIn(tag1), run_time=0.4)
        self.play(Write(l1), run_time=1.2)
        self.wait(0.6)
        self.play(FadeIn(l2, shift=DOWN * 0.2), run_time=0.6)
        self.play(Write(l3), run_time=1.2)
        self.wait(1.0)
        self.play(Transform(l3, l4), run_time=1.0)
        self.play(Indicate(l3, color=GOLD), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(stack), FadeOut(tag1), run_time=0.5)

        # ---------- 3. PROOF 2: the vanishing gap (15-29s) ----------
        tag2 = Text("PROOF 2", font_size=40, color=CYAN, weight=BOLD)
        tag2.move_to(UP * 5)
        self.play(FadeIn(tag2), run_time=0.4)

        bar_w, bar_h = 7.0, 0.9
        outline = Rectangle(width=bar_w, height=bar_h, color=WHITE, stroke_width=4)
        outline.move_to(UP * 1.5)
        left = outline.get_left()

        def fill_bar(frac):
            r = Rectangle(
                width=bar_w * frac,
                height=bar_h,
                fill_color=CYAN,
                fill_opacity=0.9,
                stroke_width=0,
            )
            r.move_to(left + RIGHT * (bar_w * frac) / 2)
            return r

        label_one = Text("1", font_size=44).next_to(outline, UP, buff=0.3).align_to(outline, RIGHT)
        steps = [
            ("0.9", "0.1"),
            ("0.99", "0.01"),
            ("0.999", "0.001"),
            ("0.9999", "0.0001"),
        ]
        fracs = [0.9, 0.99, 0.999, 0.9999]

        fill = fill_bar(fracs[0])
        val = Text(f"Filled: {steps[0][0]}", font_size=50)
        gap = Text(f"Gap: {steps[0][1]}", font_size=50, color=RED)
        info = VGroup(val, gap).arrange(DOWN, buff=0.5).move_to(DOWN * 1.8)

        self.play(Create(outline), FadeIn(label_one), run_time=0.8)
        self.play(FadeIn(fill), FadeIn(info), run_time=0.8)
        self.wait(0.6)

        for (v, g), f in zip(steps[1:], fracs[1:]):
            new_fill = fill_bar(f)
            new_val = Text(f"Filled: {v}", font_size=50).move_to(val)
            new_gap = Text(f"Gap: {g}", font_size=50, color=RED).move_to(gap)
            self.play(
                Transform(fill, new_fill),
                Transform(val, new_val),
                Transform(gap, new_gap),
                run_time=0.9,
            )
            self.wait(0.4)

        # Go to infinity: the gap is zero
        full = fill_bar(1.0)
        val_end = Text("Filled: 0.999...", font_size=50).move_to(val)
        gap_end = Text("Gap: 0", font_size=60, color=GOLD, weight=BOLD).move_to(gap)
        self.play(
            Transform(fill, full),
            Transform(val, val_end),
            Transform(gap, gap_end),
            run_time=1.2,
        )
        self.play(Indicate(gap, color=GOLD), run_time=0.8)
        no_gap = Text("No gap = same number.", font_size=48, color=GOLD)
        no_gap.move_to(DOWN * 4.2)
        self.play(FadeIn(no_gap, shift=UP * 0.2), run_time=0.6)
        self.wait(1.4)
        self.play(
            *[FadeOut(m) for m in (outline, fill, label_one, val, gap, no_gap, tag2)],
            run_time=0.5,
        )

        # ---------- 4. COMMENT BAIT (29-37s) ----------
        q1 = Text("Still disagree?", font_size=64, weight=BOLD)
        q2 = Text("Name ONE number", font_size=58, color=CYAN)
        q3 = Text("between 0.999... and 1.", font_size=58, color=CYAN)
        q4 = Text("Comment it.", font_size=64, color=GOLD, weight=BOLD)
        block = VGroup(q1, q2, q3, q4).arrange(DOWN, buff=0.6).move_to(UP * 0.8)

        self.play(Write(q1), run_time=0.8)
        self.play(FadeIn(q2, shift=UP * 0.2), FadeIn(q3, shift=UP * 0.2), run_time=0.8)
        self.wait(1.0)
        self.play(Write(q4), run_time=0.6)
        self.wait(2.0)