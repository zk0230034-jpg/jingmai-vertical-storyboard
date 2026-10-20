"""Build the standalone Jingmai prompt from the skill's canonical references."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCE_NAMES = (
    "workflow.md",
    "director-plan-compiler.md",
    "narrative-shot-selection.md",
    "pacing-and-shot-density.md",
    "cinematic-language.md",
    "camera-movement-lexicon.md",
    "shot-size-angle-composition.md",
    "focus-light-sound.md",
    "performance-direction.md",
    "action-choreography.md",
    "martial-arts-vocabulary.md",
    "vfx-design.md",
    "method-examples.md",
    "output-contract.md",
    "directing-and-revision.md",
    "quality-gates.md",
    "counterfactual-tests.md",
)

INTRO = """# 镜脉竖屏短剧分镜提示词模板 V9.0｜叙事驱动的镜头语言版

将本模板完整交给目标AI，再提供真实剧本和已确认的集数、模型、制作方向、导演方案与重点。AI须把剧本视为唯一剧情事实源，把本文视为工作规则。本文没有可直接复制到作品的人物、招式、台词或能力设定；任何案例只用来理解方法。缺少剧本时仅邀请用户提供，不虚构分析。

目标是可表演、可剪辑、可供视频模型执行的镜头。专业术语必须附可见执行，镜头语言为人物、信息与动作服务。V9.0的核心不是增加术语使用次数，而是建立“剧情变化→观看任务→演员与空间行动→可选摄影/光声手段→连续性和容量检验”的选择能力。用户已给出的选择不要重问，未回复不算确认。以下知识库是候选工具，不是每Part必须用满的清单；普通文戏不套动作或特效清单，普通动作不为炫技增添不存在的流派和能力。
"""


def build() -> str:
    sections = [INTRO.rstrip()]
    for name in REFERENCE_NAMES:
        source = ROOT / "references" / name
        sections.append(source.read_text(encoding="utf-8").strip())
    return "\n\n---\n\n".join(sections) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Target Markdown file")
    args = parser.parse_args()
    target = args.output.resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build(), encoding="utf-8", newline="\n")
    print(f"Built {target}")


if __name__ == "__main__":
    main()
